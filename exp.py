import os
import json
import argparse
from pipeline import Pipeline



def main(args):

    with open(args.motion_instructions_path, "r", encoding="utf8") as rf:
        motion_instructions = json.load(rf)

    for motion_i, motion_instruction in enumerate(motion_instructions):
        if motion_i >= args.start_motion_i:
            if not args.debug:
                args.motion_instruction = motion_instruction["motion_instruction"]
            args.motion_i = motion_i

            # Initialization
            pipeline = Pipeline(args)
            # Run the pipeline
            pipeline.run()

            if not os.path.exists(args.results_folder_path):
                os.mkdir(args.results_folder_path)

            with open(os.path.join(args.results_folder_path, args.summarized_steps_plans_filename % motion_i), "w", encoding="utf8") as f:
                json.dump(pipeline.summarized_steps_plans, f, ensure_ascii=False, indent=2)

            with open(os.path.join(args.results_folder_path, args.log_filename % motion_i), "w", encoding="utf8") as f:
                json.dump(pipeline.log, f, ensure_ascii=False, indent=2)
            
            if args.debug:
                break # Just run once for the debugged motion instruction



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # General
    parser.add_argument("--motion_instructions_path", type=str, default="./motion_instructions/application.json")
    parser.add_argument("--motion_instruction", type=str, default="slide the window open from the center to the sides with both hands")
    parser.add_argument("--debug", action="store_true", help="Use the specified motion instruction to debug")
    parser.add_argument("--results_folder_path", type=str, default="results")
    parser.add_argument("--summarized_steps_plans_filename", type=str, default="summarized_steps_plans_%s.json")
    parser.add_argument("--log_filename", type=str, default="log_%s.json")
    parser.add_argument("--start_motion_i", default=0, type=int, help="Start from the i-th motion instruction")
    parser.add_argument("--max_attempts", default=3, type=int, help="Maximum number of attempts to get an acceptable step plan")

    # Constrained generation
    parser.add_argument("--gold", action="store_true", help="Use the golden high-level plans for constrained generation")
    parser.add_argument("--gold_motion_plans_folder_path", type=str, default="gold_motion_plans")
    parser.add_argument("--only_hp", action="store_true", help="Just generate the high-level plan")

    # Configure the API caller
    parser.add_argument("--model", type=str, default="gpt-4o-mini", choices=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "o3", "o4-mini", "claude-3-5-sonnet-20241022", "llama3.1:8b", "llama3.1:70b", "llama3.2-vision:11b", "llama3.2-vision:90b"])
    parser.add_argument("--temperature", type=float, default=1)
    parser.add_argument("--max_tokens", type=int, default=4095)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--max_retries", type=int, default=3)

    # Querying strategic options
    parser.add_argument("--high_level_planning_mode", type=str, choices=["in_one_go", "piece_by_piece"])
    parser.add_argument("--body_part_description", action="store_true", help="Whether to generate a language description for each body part before selection.")
    parser.add_argument("--body_part_reflection", action="store_true", help="Whether to reflect for each body part.")
    parser.add_argument("--next_position_planning_mode", type=str, choices=["hierarchical", "one_by_one", "all"])


    args = parser.parse_args()

    main(args)