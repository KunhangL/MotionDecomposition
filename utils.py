import os
import json
import fastjsonschema

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama



def load_dict_from_message(message):
    return json.loads(message.content)


def load_text_from_message(message):
    return message.content


class APICaller:

    def __init__(
        self,
        model,
        reasoning_effort=None, # Only used for OpenAI reasoning models
        temperature=1,
        max_tokens=4095,
        timeout=60,
        max_retries=3, # max_retries for the model
        max_retries_schema=20 # max_retries for the schema
    ):
        self.model = model
        self.reasoning_effort = reasoning_effort
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_retries_schema = max_retries_schema
        self._initialize_model() # initialize self.llm

    def __call__(self, messages, json_schema=None) -> str:
        if json_schema:
            schema_matched = False
            cnt = 0
            while not schema_matched:
                cnt += 1
                structured_llm = self.llm.with_structured_output(json_schema)
                response_dict = structured_llm.invoke(messages)
                response_validator = fastjsonschema.compile(json_schema)
                try:
                    response_validator(response_dict)
                    schema_matched = True
                except fastjsonschema.JsonSchemaException as e:
                    print(response_dict)
                    # if set(response_dict.keys()) == {"timing"} and float(response_dict["timing"]): # Handle timing in string format
                    #     response_dict["timing"] = float(response_dict["timing"])
                    #     return json.dumps(response_dict)
                    if cnt == self.max_retries_schema:
                        raise ValueError(f"Schema validation failed after {self.max_retries_schema} retries")
                    print(e, "--->Retrying...")
            return json.dumps(response_dict)
        else:
            return self.llm.invoke(messages).content

    def _initialize_model(self):
        if self.model in ["gpt-4.1", "gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "o3", "o4-mini"]:
            self.llm = ChatOpenAI(
                model=self.model,
                reasoning_effort=self.reasoning_effort,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                timeout=self.timeout,
                max_retries=self.max_retries
            )
        elif self.model in ["gemini-2.5-flash", "gemini-2.5-pro"]:
            self.llm = ChatGoogleGenerativeAI(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                timeout=self.timeout,
                max_retries=self.max_retries
            )
        elif self.model in ["claude-3-5-sonnet-20241022", "claude-sonnet-4-20250514"]:
            self.llm = ChatAnthropic(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                timeout=self.timeout,
                max_retries=self.max_retries
            )
        elif self.model in ["llama3.1:8b", "llama3.1:70b", "llama3.2-vision:11b", "llama3.2-vision:90b"]:
            self.llm = ChatOllama(
                model=self.model,
                temperature=self.temperature,
                num_predict=self.max_tokens
            )
        else:
            raise ValueError(f"Model {self.model} not supported")


if __name__ == "__main__":
    from prompts.system import system_prompt
    from prompts.high_level_planning import high_level_planning_prompts
    motion_instruction = "A person jumps onto a 1-meter-high table right in front of him."
    api_caller = APICaller(model="gpt-4.1")
    template = "```TEMPLATE\n\
{\n\
    \"number_of_steps\": N,\n\
    \"steps\": [\n\
        {\n\
            \"step_number\": 1,\n\
            \"time_range\": [t_0, t_1],\n\
            \"initial_state\": INTIAL_STATE_1_LANGUAGE,\n\
            \"final_state\": FINAL_STATE_1_LANGUAGE,\n\
            \"step_text\": \"STEP_TEXT_1_LANGUAGE\"\n\
        },\n\
        ...,\n\
        {\n\
            \"step_number\": N,\n\
            \"time_range\": [t_{N-1}, t_N],\n\
            \"initial_state\": INTIAL_STATE_N_LANGUAGE,\n\
            \"final_state\": FINAL_STATE_N_LANGUAGE,\n\
            \"step_text\": \"STEP_TEXT_N_LANGUAGE\"\n\
        }\n\
    ]\n\
}\n\
```"
    messages = [
        ("system", system_prompt),
        ("user", high_level_planning_prompts["in_one_go"]["prompt"] % motion_instruction + "\nTEMPLATE" + template),
        # ("user", high_level_planning_prompts["in_one_go"]["prompt"] % motion_instruction + "\nTEMPLATE" + json.dumps(high_level_planning_prompts["in_one_go"]["json_schema"])),
        # ("user", high_level_planning_prompts["in_one_go"]["prompt"] % motion_instruction),
    ]

    # response = api_caller(messages, json_schema=high_level_planning_prompts["in_one_go"]["json_schema"])
    response = api_caller(messages)
    print(response)