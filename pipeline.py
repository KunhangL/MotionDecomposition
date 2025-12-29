import copy
import json
from os.path import join as pjoin

from utils import load_dict_from_message, load_text_from_message, APICaller
from config import positions_map, body_part_group
from prompts.system import system_prompt
from prompts.high_level_planning import high_level_planning_prompts
from prompts.step_iterative_refinement import functions_prompts, body_part_positions_prompts, body_part_hierarchical_questions_prompts

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



class BodyPartsStates:

    def __init__(self):
        self.tmp_states = {body_part: "neutral" for body_part in positions_map.keys()}
        self.states = copy.deepcopy(self.tmp_states)

    def display_changed_body_parts(self): # Show changed body parts states before copying the tmp states to final states
        changed_body_parts_states = {}
        for body_part in self.tmp_states.keys():
            if self.tmp_states[body_part] != self.states[body_part]:
                changed_body_parts_states[body_part] = [self.states[body_part], self.tmp_states[body_part]]
        return changed_body_parts_states

    def update_tmp_states(self, body_part, next_pos): # Update the tmp states
        self.tmp_states[body_part] = next_pos

    def reset_tmp_states(self, body_part):
        self.tmp_states[body_part] = self.states[body_part]

    def reset_tmp_states_all(self):
        for body_part in self.tmp_states.keys():
            self.reset_tmp_states(body_part)

    def update_final_states(self):
        self.states = copy.deepcopy(self.tmp_states)



class Pipeline:

    def __init__(self, args):
        self.api_caller = APICaller(
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            timeout=args.timeout,
            max_retries=args.max_retries
        )
        self.body_parts_states = BodyPartsStates() # Keep track of the states of body parts
        self.step_n = 0 # Indicate the current number of the step. Initialized as 0.
        self.messages_buffer = {"system_message": SystemMessage(system_prompt)} # Store messages
        self.summarized_steps_plans = [] # Store the summarized animation plan for each step
        self.mode = "initial" # ["initial", "reflection"]
        self.max_attempts = args.max_attempts # The maximal number of times to generate a plan for each step
        self.motion_instruction = args.motion_instruction

        # Configure the constrained generation
        self.gold = args.gold
        self.gold_motion_plans_folder_path = args.gold_motion_plans_folder_path
        self.only_hp = args.only_hp
        self.motion_i = args.motion_i

        # Querying strategic options
        self.high_level_planning_mode = args.high_level_planning_mode # ["in_one_go", "piece_by_piece"]
        self.body_part_description = args.body_part_description
        self.body_part_reflection = args.body_part_reflection
        self.next_position_planning_mode = args.next_position_planning_mode # ["hierarchical", "one_by_one", "all"]

        self.log = {"motion_instruction": args.motion_instruction, "step_planning_trace": []} # Store the planning trace
        print("**Motion Instruction**")
        print(args.motion_instruction)


    def _start_new_step(self):
        self.step_n += 1
        print(f"========== Step {self.step_n} ==========")


    @staticmethod
    def _customize_json_schema(json_schema_template, options): # Customize the array in the json schema with given choices of next positions
        customized_json_schema = copy.deepcopy(json_schema_template)
        customized_json_schema["properties"]["next_position"]["enum"] = options
        return customized_json_schema


    def run(self):
        # High-level Planning
        self.get_high_level_plan()
        if not self.only_hp:
            n_steps = self.high_level_plan["number_of_steps"]
            # Iterative Refinement
            for _ in range(n_steps):
                self._start_new_step()
                step_accepted = False
                while not step_accepted:
                    try:
                        self.get_step_info()
                        step_accepted = True
                    except Exception as e:
                        print(f"**************Error**************: {e}--->Replanning Step{self.step_n}")
                        del self.log["step_planning_trace"][-1] # Remove the last erroneous step planning trace
                        self.body_parts_states.reset_tmp_states_all()
                        continue


    # Get the high-level plan
    def get_high_level_plan(self):
        
        if self.gold: # Use the golden high-level plans for constrained generation
            with open(pjoin(self.gold_motion_plans_folder_path, f"summarized_steps_plans_{self.motion_i}.json"), "r", encoding="utf8") as f:
                gold_summarized_steps_plans = json.load(f)
                self.high_level_plan = {"number_of_steps": len(gold_summarized_steps_plans), "steps": gold_summarized_steps_plans}
                for step in self.high_level_plan["steps"]:
                    del step["changed_body_parts_states"]

        else: # Normal high-level planning
            messages = [self.messages_buffer["system_message"]]

            if self.high_level_planning_mode == "in_one_go":
                self.messages_buffer["hp_user_message"] = HumanMessage(high_level_planning_prompts["in_one_go"]["prompt"] % self.motion_instruction)
                messages.append(self.messages_buffer["hp_user_message"])
                self.messages_buffer["hp_assistant_message"] = AIMessage(self.api_caller(messages, json_schema=high_level_planning_prompts["in_one_go"]["json_schema"]))
                self.high_level_plan = load_dict_from_message(self.messages_buffer["hp_assistant_message"])

            elif self.high_level_planning_mode == "piece_by_piece":
                self.high_level_plan = {"steps": []}
                self.messages_buffer["hp_setup_user_message"] = HumanMessage(high_level_planning_prompts["piece_by_piece"]["setup"]["prompt"] % self.motion_instruction)
                messages.append(self.messages_buffer["hp_setup_user_message"])
                is_end = False
                step_n = 0
                while not is_end:
                    step_n += 1

                    # Asking the movement of relevant body parts
                    self.messages_buffer["hp_movement_user_message"] = HumanMessage(high_level_planning_prompts["piece_by_piece"]["movement"]["prompt"] % step_n)
                    messages.append(self.messages_buffer["hp_movement_user_message"])
                    self.messages_buffer["hp_movement_assistant_message"] = AIMessage(self.api_caller(messages))
                    messages.append(self.messages_buffer["hp_movement_assistant_message"])
                    # Asking the initial states of relevant body parts
                    self.messages_buffer["hp_initial_state_user_message"] = HumanMessage(high_level_planning_prompts["piece_by_piece"]["initial_state"]["prompt"] % step_n)
                    messages.append(self.messages_buffer["hp_initial_state_user_message"])
                    self.messages_buffer["hp_initial_state_assistant_message"] = AIMessage(self.api_caller(messages))
                    messages.append(self.messages_buffer["hp_initial_state_assistant_message"])
                    # Asking the final states of relevant body parts
                    self.messages_buffer["hp_final_state_user_message"] = HumanMessage(high_level_planning_prompts["piece_by_piece"]["final_state"]["prompt"] % step_n)
                    messages.append(self.messages_buffer["hp_final_state_user_message"])
                    self.messages_buffer["hp_final_state_assistant_message"] = AIMessage(self.api_caller(messages))
                    messages.append(self.messages_buffer["hp_final_state_assistant_message"])
                    
                    # Timing this step
                    self.messages_buffer["hp_timing_user_message"] = HumanMessage(high_level_planning_prompts["piece_by_piece"]["timing"]["prompt"] % step_n)
                    messages.append(self.messages_buffer["hp_timing_user_message"])
                    self.messages_buffer["hp_timing_assistant_message"] = AIMessage(self.api_caller(messages, json_schema=high_level_planning_prompts["piece_by_piece"]["timing"]["json_schema"]))
                    messages.append(self.messages_buffer["hp_timing_assistant_message"])
                    # Check if this step is the end of the motion
                    self.messages_buffer["hp_is_end_user_message"] = HumanMessage(high_level_planning_prompts["piece_by_piece"]["is_end"]["prompt"])
                    messages.append(self.messages_buffer["hp_is_end_user_message"])
                    self.messages_buffer["hp_is_end_assistant_message"] = AIMessage(self.api_caller(messages, json_schema=high_level_planning_prompts["piece_by_piece"]["is_end"]["json_schema"]))
                    messages.append(self.messages_buffer["hp_is_end_assistant_message"])
                    if load_dict_from_message(self.messages_buffer["hp_is_end_assistant_message"])["is_end"] == "yes":
                        is_end = True
                        self.high_level_plan["number_of_steps"] = step_n
                    # Update high_level_plan
                    if step_n == 1:
                        start_time = 0
                        end_time = load_dict_from_message(self.messages_buffer["hp_timing_assistant_message"])["timing"]
                    else:
                        start_time = self.high_level_plan["steps"][step_n - 2]["time_range"][1]
                        end_time = start_time + load_dict_from_message(self.messages_buffer["hp_timing_assistant_message"])["timing"]
                    self.high_level_plan["steps"].append(
                        {
                            "step_number": step_n,
                            "time_range": [start_time, end_time],
                            "initial_state": load_text_from_message(self.messages_buffer["hp_initial_state_assistant_message"]),
                            "final_state": load_text_from_message(self.messages_buffer["hp_final_state_assistant_message"]),
                            "step_text": load_text_from_message(self.messages_buffer["hp_movement_assistant_message"])
                        }
                    )

            else:
                raise ValueError("Please check high_level_planning_mode!")

        self._update_summarized_steps_plans(mode="high_level_plan")
        self.log["high_level_plan"] = self.high_level_plan
        print("**High Level Plan**")
        print(json.dumps(self.high_level_plan, indent=2))
        print("\n")


    # Step-based iterative refinement
    def get_step_info(self):
        self.log["step_planning_trace"].append({"step_number": self.step_n, "body_parts": {}})
        self.messages_buffer["step_high_level_plan_user_message"] = HumanMessage(
            functions_prompts["step_high_level_plan"]["prompt"] % (
                self.motion_instruction,
                self.step_n,
                self.high_level_plan["steps"][self.step_n - 1]["initial_state"],
                self.high_level_plan["steps"][self.step_n - 1]["final_state"],
                self.high_level_plan["steps"][self.step_n - 1]["step_text"]
            )
        ) # The high-level plan for this step
        for body_parts in body_part_group:
            main_messages = [
                self.messages_buffer["system_message"],
                self.messages_buffer["step_high_level_plan_user_message"]
            ]
            for body_part in body_parts:

                print(f"<--- {body_part} --->")
                self.log["step_planning_trace"][-1]["body_parts"][body_part] = []

                self.mode = "initial"
                body_part_plan_acceptable = False
                cnt = 0

                while not body_part_plan_acceptable:
                    cnt += 1
                    self.log["step_planning_trace"][-1]["body_parts"][body_part].append({"attempt": cnt})
                    if cnt == self.max_attempts:
                        body_part_plan_acceptable = True

                    planned_next_position = self.get_body_part_info(copy.deepcopy(main_messages), body_part)

                    if self.body_part_reflection: # Turn on the body part reflection
                        if load_dict_from_message(self.messages_buffer[f"reflection_judgement_step{self.step_n}_assistant_message"])["judgement"] == "no" or body_part_plan_acceptable:
                            body_part_plan_acceptable = True
                            if self.body_part_description:
                                main_messages.extend([
                                    self.messages_buffer[f"{body_part}_language_user_message"],
                                    self.messages_buffer[f"{body_part}_language_assistant_message"]
                                ])
                            if self.next_position_planning_mode in ["hierarchical", "one_by_one"]:
                                main_messages.extend(self.messages_buffer[f"{body_part}_choice_messages"])
                            else:
                                main_messages.extend([
                                    self.messages_buffer[f"{body_part}_choice_user_message"],
                                    self.messages_buffer[f"{body_part}_choice_assistant_message"]
                                ])
                            print("\n")
                        else:
                            self.mode = "reflection"
                            self.messages_buffer[f"correction_step{self.step_n}_user_message"] = HumanMessage(
                                functions_prompts["correction"]["prompt"] % (
                                    load_text_from_message(self.messages_buffer[f"reflection_analysis_step{self.step_n}_assistant_message"]),
                                    body_part,
                                    planned_next_position,
                                    self.step_n
                                )
                            )
                            self.body_parts_states.reset_tmp_states(body_part)
                    else: # Turn off the body part reflection
                        body_part_plan_acceptable = True
                        if self.body_part_description:
                            main_messages.extend([
                                self.messages_buffer[f"{body_part}_language_user_message"],
                                self.messages_buffer[f"{body_part}_language_assistant_message"]
                            ])
                        if self.next_position_planning_mode in ["hierarchical", "one_by_one"]:
                            main_messages.extend(self.messages_buffer[f"{body_part}_choice_messages"])
                        else:
                            main_messages.extend([
                                self.messages_buffer[f"{body_part}_choice_user_message"],
                                self.messages_buffer[f"{body_part}_choice_assistant_message"]
                            ])
                        print("\n")

        self._update_summarized_steps_plans(mode="body_parts_info")
        print(f"**States Changes of Step{self.step_n}**")
        print(json.dumps(self.summarized_steps_plans[self.step_n - 1]["changed_body_parts_states"], indent=2))
        print("\n\n")
        self.body_parts_states.update_final_states()


    def get_body_part_info(self, messages, body_part):
        if self.body_part_reflection:
            if self.mode == "reflection":
                messages.append(self.messages_buffer[f"correction_step{self.step_n}_user_message"])
                print(f"---------- Correction ----------")
        last_position = self.body_parts_states.states[body_part]

        if self.body_part_description:
            self.messages_buffer[f"{body_part}_language_user_message"] = HumanMessage(
                functions_prompts["planning"]["language"]["prompt"] % (
                    body_part,
                    last_position,
                    body_part_positions_prompts[body_part][last_position],
                    self.step_n
                )
            )
            messages.append(self.messages_buffer[f"{body_part}_language_user_message"])
            self.messages_buffer[f"{body_part}_language_assistant_message"] = AIMessage(self.api_caller(messages))
            messages.append(self.messages_buffer[f"{body_part}_language_assistant_message"])
            planned_language_description = load_text_from_message(self.messages_buffer[f"{body_part}_language_assistant_message"])
            print(f"**Planned Language Description**\n{planned_language_description}")
            self.log["step_planning_trace"][-1]["body_parts"][body_part][-1]["planned_language_description"] = planned_language_description

        planned_next_position = self.choose_next_position(body_part, last_position, messages)
        print(f"**Planned Next Position**\n{planned_next_position}")
        self.log["step_planning_trace"][-1]["body_parts"][body_part][-1]["planned_next_position"] = planned_next_position

        if self.body_part_reflection:
            self.get_reflection(messages, body_part)

        return planned_next_position


    def choose_next_position(self, body_part, last_position, messages):

        if self.next_position_planning_mode == "hierarchical": # Asking questions hierarchically
            self.messages_buffer[f"{body_part}_choice_messages"] = []
            question_options = body_part_hierarchical_questions_prompts[body_part]
            is_end = False
            while not is_end:
                self.messages_buffer[f"{body_part}_choice_messages"].append(
                    HumanMessage(question_options["question"] % list(question_options["options"].keys()))
                )
                messages.append(self.messages_buffer[f"{body_part}_choice_messages"][-1])
                self.messages_buffer[f"{body_part}_choice_messages"].append(
                    AIMessage(
                        self.api_caller(
                            messages,
                            self._customize_json_schema(
                                body_part_hierarchical_questions_prompts["json_schema"],
                                list(question_options["options"].keys())
                            )
                        )
                    )
                )
                messages.append(self.messages_buffer[f"{body_part}_choice_messages"][-1])
                next_position = load_dict_from_message(self.messages_buffer[f"{body_part}_choice_messages"][-1])["next_position"]
                if type(question_options["options"][next_position]) == str: # Reaching the final planned next position
                    planned_next_position = question_options["options"][next_position]
                    is_end = True
                question_options = question_options["options"][next_position]

        elif self.next_position_planning_mode == "one_by_one": # Asking questions about each position one by one
            self.messages_buffer[f"{body_part}_choice_messages"] = []
            is_end = False
            while not is_end:
                for next_position in body_part_positions_prompts[body_part].keys():
                    self.messages_buffer[f"{body_part}_choice_messages"].append(
                        HumanMessage(
                            functions_prompts["planning"]["yes_no_choice"]["prompt"] % (
                                body_part,
                                last_position,
                                body_part_positions_prompts[body_part][last_position],
                                next_position,
                                body_part_positions_prompts[body_part][next_position]
                            )
                        )
                    )
                    messages.append(self.messages_buffer[f"{body_part}_choice_messages"][-1])
                    self.messages_buffer[f"{body_part}_choice_messages"].append(
                        AIMessage(
                            self.api_caller(
                                messages,
                                functions_prompts["planning"]["yes_no_choice"]["json_schema"]
                            )
                        )
                    )
                    messages.append(self.messages_buffer[f"{body_part}_choice_messages"][-1])
                    if load_dict_from_message(self.messages_buffer[f"{body_part}_choice_messages"][-1])["judgement"] == "yes":
                        planned_next_position = next_position
                        is_end = True
                        break
                    elif load_dict_from_message(self.messages_buffer[f"{body_part}_choice_messages"][-1])["judgement"] == "no":
                        continue
                    else:
                        raise ValueError("The LLM doesn't return valid responses for next-position choice!")

        elif self.next_position_planning_mode == "all": # Asking about all positions in one go
            self.messages_buffer[f"{body_part}_choice_user_message"] = HumanMessage(
                functions_prompts["planning"]["choice"]["prompt"] % (
                    body_part,
                    body_part_positions_prompts[body_part],
                    last_position
                )
            )
            messages.append(self.messages_buffer[f"{body_part}_choice_user_message"])
            self.messages_buffer[f"{body_part}_choice_assistant_message"] = AIMessage(
                self.api_caller(
                    messages,
                    self._customize_json_schema(
                        functions_prompts["planning"]["choice"]["json_schema"],
                        list(body_part_positions_prompts[body_part].keys())
                    )
                )
            )
            messages.append(self.messages_buffer[f"{body_part}_choice_assistant_message"])
            planned_next_position = load_dict_from_message(self.messages_buffer[f"{body_part}_choice_assistant_message"])["next_position"]

        else:
            raise ValueError("Please check next_position_planning_mode!")
        
        self.body_parts_states.update_tmp_states(body_part, planned_next_position)

        return planned_next_position # The number of trials


    def get_reflection(self, messages, body_part):
        self.messages_buffer[f"reflection_analysis_step{self.step_n}_user_message"] = HumanMessage(functions_prompts["reflection"]["analysis"]["prompt"])
        messages.append(self.messages_buffer[f"reflection_analysis_step{self.step_n}_user_message"])
        self.messages_buffer[f"reflection_analysis_step{self.step_n}_assistant_message"] = AIMessage(self.api_caller(messages))
        messages.append(self.messages_buffer[f"reflection_analysis_step{self.step_n}_assistant_message"])
        self.messages_buffer[f"reflection_judgement_step{self.step_n}_user_message"] = HumanMessage(functions_prompts["reflection"]["judgement"]["prompt"])
        messages.append(self.messages_buffer[f"reflection_judgement_step{self.step_n}_user_message"])
        self.messages_buffer[f"reflection_judgement_step{self.step_n}_assistant_message"] = AIMessage(
            self.api_caller(
                messages,
                functions_prompts["reflection"]["judgement"]["json_schema"]
            )
        )
        messages.append(self.messages_buffer[f"reflection_judgement_step{self.step_n}_assistant_message"])
        
        print(f"**Reflection**")
        reflection = load_text_from_message(self.messages_buffer[f"reflection_analysis_step{self.step_n}_assistant_message"])
        print(reflection)
        self.log["step_planning_trace"][-1]["body_parts"][body_part][-1]["reflection"] = reflection
        print("**Need Correction?**")
        reflection_judgement = load_dict_from_message(self.messages_buffer[f"reflection_judgement_step{self.step_n}_assistant_message"])["judgement"]
        print(reflection_judgement)
        self.log["step_planning_trace"][-1]["body_parts"][body_part][-1]["reflection_judgement"] = reflection_judgement


    def _update_summarized_steps_plans(self, mode):
        if mode == "high_level_plan":
            for i in range(self.high_level_plan["number_of_steps"]):
                self.summarized_steps_plans.append(self.high_level_plan["steps"][i])
        elif mode == "body_parts_info":
            self.summarized_steps_plans[self.step_n - 1]["changed_body_parts_states"] = self.body_parts_states.display_changed_body_parts()
        else:
            raise ValueError("Please specify the mode!!!")