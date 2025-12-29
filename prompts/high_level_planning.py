high_level_planning_prompts = {
    "in_one_go": {
        "prompt": "The human initially stands naturally with arms hanging beside the body. The textual human motion instruction is \"%s\". Decompose it step-by-step with three language descriptions for each step (one for the initial state of moved body parts, one for the final state of moved body parts and one for the movement). Each step should be simple enough to include only **single-direction** motions for all moved body parts. Estimate a time range in the second unit for each step (the end time of the last step should exactly be the start time of the next step).",
        "json_schema": {
            "title": "high_level_planning",
            "description": "Decompose the motion instruction step-by-step",
            "type": "object",
            "properties": {
                "number_of_steps": {
                    "type": "integer",
                    "description": "The number of steps involved in the motion instruction"
                },
                "steps": {
                    "type": "array",
                    "description": "The steps involved in the motion instruction",
                    "items": {
                        "type": "object",
                        "description": "The details of a step",
                        "properties": {
                            "step_number": {
                                "type": "integer",
                                "description": "The number of this step"
                            },
                            "time_range": {
                                "type": "array",
                                "description": "The time range of the step in the second unit",
                                "items": {
                                    "type": "number"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "initial_state": {
                                "type": "string",
                                "description": "The initial states of moved body parts in language"
                            },
                            "final_state": {
                                "type": "string",
                                "description": "The final states of moved body parts in language"
                            },
                            "step_text": {
                                "type": "string",
                                "description": "The movements of moved body parts in language"
                            }
                        },
                        "required": ["step_number", "time_range", "initial_state", "final_state", "step_text"]
                    }
                }
            },
            "required": ["number_of_steps", "steps"]
        }
    },
    "piece_by_piece": {
        "setup": {
            "prompt": "The human initially stands naturally with arms hanging beside the body. The textual human motion instruction is \"%s\"."
        },
        "movement": {
            "prompt": "What are the movements of relevant body parts in Step%s? The movements should be simple enough to be only **single-directional**."
        },
        "initial_state": {
            "prompt": "What are the initial states of relevant body parts in Step%s?"
        },
        "final_state": {
            "prompt": "What are the final states of relevant body parts in Step%s?"
        },
        "timing": {
            "prompt": "How long does Step%s last in the second unit?",
            "json_schema": {
                "title": "timing",
                "description": "The duration of a step",
                "type": "object",
                "properties": {
                    "timing": {
                        "type": "number",
                        "description": "The duration of the step in the second unit"
                    }
                },
                "required": ["timing"]
            }
        },
        "is_end": {
            "prompt": "Is it the end of this motion?",
            "json_schema": {
                "title": "is_end",
                "description": "Whether the motion is finished",
                "type": "object",
                "properties": {
                    "is_end": {
                        "type": "string",
                        "description": "Whether the motion is finished",
                        "enum": ["yes", "no"]
                    }
                },
                "required": ["is_end"]
            }
        }
    }
}