functions_prompts = {
    "step_high_level_plan": {
        "prompt": "The human initially stands naturally with arms hanging beside the body. The textual human motion instruction is \"%s\". In the high-leve plan of Step%s, the initial states of relevant body parts are \"%s\", the final states of relevant body parts are \"%s\", and the movements of relevant body parts are \"%s\"."
    },
    "planning": {
        "language": {
            "prompt": "The last position of %s is **%s** (%s). Describe the movement of this body part during Step%s and final position at the end of the step in language."
        },
        "choice": {
            "prompt": "There are multiple possible positions for %s:\n%s\n\nThe last position of this body part is **%s**. Choose the next position from the options above.",
            "json_schema": {
                "title": "body_part_next_position_choice",
                "description": "The next position of a body part",
                "type": "object",
                "properties": {
                    "next_position": {
                        "type": "string",
                        "description": "The next position of the body part",
                        "enum": []
                    }
                },
                "required": ["next_position"]
            }
        },
        "yes_no_choice": {
            "prompt": "The last position of %s is **%s** (%s). Is the next position **%s** (%s)?",
            "json_schema": {
                "title": "body_part_next_position_choice",
                "description": "Whether the specified next position is correct",
                "type": "object",
                "properties": {
                    "judgement": {
                        "type": "string",
                        "description": "Whether the specified next position is correct",
                        "enum": ["yes", "no"]
                    }
                },
                "required": ["judgement"]
            }
        }
    },
    "reflection": {
        "analysis": {
            "prompt": "Analyze this body part with its planned next position. Is this body part necessary for this step? If so, does the planned next position of this body part achieve the goal final state in the high-level plan?"
        },
        "judgement": {
            "prompt": "Do you think there's need to replan this body part in order to achieve the goal final state in the high-level plan? Give your judgement.",
            "json_schema": {
                "title": "body_part_replanning_judgement",
                "description": "Whether the body part needs replanning",
                "type": "object",
                "properties": {
                    "judgement": {
                        "type": "string",
                        "description": "Whether the body part needs replanning",
                        "enum": ["yes", "no"]
                    }
                },
                "required": ["judgement"]
            }
        }
    },
    "correction": {
        "prompt": "You think that: %s. So the next position of %s should not be **%s**.\nBased on the thought, replan this body part in Step%s."
    }
}


body_part_positions_prompts = {
    "Head": {
        "neutral": "The head is level with the spine and faces forward relative to the torso. The chin is neither raised nor lowered, forming a right angle (90 degrees) with the neck. The back of the head is aligned with the upper back, maintaining a straight, neutral posture.",
        "tilted_up_slightly": "The chin forms a slightly obtuse angle, slightly more than 90 degrees, with the neck. The back of the head is slightly closer to the upper back, making the angle between the back of the head and the upper back slightly more than 90 degrees.",
        "tilted_up_fully": "The chin forms a significantly obtuse angle with the neck. The back of the head almost touches the upper back.",
        "tilted_down_slightly": "The chin forms a slightly acute angle, slightly less than 90 degrees, with the neck.",
        "tilted_down_fully": "The chin nearly touches the chest, forming a very acute angle, often less than 45 degrees, with the neck.",
        "turned_left_slightly": "The nose points just a bit to the left of the body's midline. The angle between the nose's direction and the body's central axis is small, resulting in a slight turn.",
        "turned_left_fully": "The nose points directly towards or over the left shoulder, forming a nearly right angle of approximately 90 degrees with the body's midline.",
        "turned_right_slightly": "The nose points just a bit to the right of the body's midline. The angle between the nose's direction and the body's central axis is small, resulting in a slight turn.",
        "turned_right_fully": "The nose points directly towards or over the right shoulder, forming a nearly right angle of approximately 90 degrees with the body's midline.",
        "tilted_left_slightly": "The left ear forms a small angle, around 45 degrees, with the left shoulder. The right ear forms a larger, obtuse angle with the right shoulder.",
        "tilted_left_fully": "The left ear nearly touches the left shoulder, forming an angle smaller than 20 degrees. The right ear forms an almost straight angle, nearing 180 degrees, with the right shoulder.",
        "tilted_right_slightly": "The right ear forms a small angle, around 45 degrees, with the right shoulder. The left ear forms a larger, obtuse angle with the left shoulder.",
        "tilted_right_fully": "The right ear nearly touches the right shoulder, forming an angle smaller than 20 degrees. The left ear forms an almost straight angle, nearing 180 degrees, with the left shoulder."
    },
    "Torso": {
        "neutral": "The waist is in an upright position, aligned with the spine. The pelvis and torso maintain a straight posture.",
        "twisted_left_slightly": "The left side of the waist moves slightly backward, and the right side moves slightly forward, forming a small angle to the left relative to the feet. The muscles on the right side extend mildly, while those on the left side contract slightly.",
        "twisted_left_fully": "The left side of the waist moves backward, and the right side moves forward, causing a rotational angle to the left relative to the feet. The muscles on the right side of the lower back and abdomen extend slightly, while the muscles on the left side contract lightly.",
        "twisted_right_slightly": "The right side of the waist moves slightly backward, and the left side moves slightly forward, forming a small angle to the right relative to the feet. The muscles on the left side extend mildly, while those on the right side contract slightly.",
        "twisted_right_fully": "The right side of the waist moves backward, and the left side moves forward, causing a rotational angle to the right relative to the feet. The muscles on the left side of the lower back and abdomen extend slightly, while the muscles on the right side contract lightly.",
        "bent_forward_slightly": "The waist forms a slight angle, around 45 degrees, with the thighs. The lower abdomen is closer to the thighs, and the muscles in the lower back lengthen slightly while those in the lower abdomen contract a little.",
        "bent_forward_fully": "The waist forms a right angle, around 90 degrees, with the thighs. The muscles in the lower back stretch significantly, while those in the abdomen contract fully.",
        "bent_backward": "The waist forms a pronounced outward curve, creating a significant arch in the lower back. The front side angle of the waist increases markedly, with the muscles in the lower back fully contracted and those in front maximally extended.",
        "tilted_left_slightly": "The left side of the waist moves slightly downward, and the right side is slightly raised, forming a small angle. The right side muscles extend a bit, while the left muscles contract slightly.",
        "tilted_left_fully": "The left side of the waist moves downward, forming a right angle with the pelvis, with the right side raised. The right body muscles stretch, while the left muscles contract.",
        "tilted_right_slightly": "The right side of the waist moves slightly downward, and the left side is slightly raised, forming a small angle. The left side muscles extend a bit, while the right muscles contract slightly.",
        "tilted_right_fully": "The right side of the waist moves downward, forming a right angle with the pelvis, with the left side raised. The left body muscles stretch, while the right muscles contract."
    },
    "LeftUpperArm": {
        "neutral": "The left upper arm is relaxed and hanging straight down by the side of the body, parallel to the torso.",
        "forward_elbowpit_inward": "The left upper arm is extended straight forward relative to the torso, parallel to the ground and perpendicular to the torso. The elbow pit faces inward to the midline of the body.",
        "forward_elbowpit_upward": "The left upper arm is extended straight forward relative to the torso, parallel to the ground and perpendicular to the torso. The elbow pit faces upward relative to the torso.",
        "upward": "The left upper arm is lifted straight upwards, close to the ear, reaching towards the sky.",
        "side_elbowpit_forward": "The left upper arm is extended straight out to the side, forming a right angle with the torso (horizontally aligned with the shoulders). The elbow pit faces forward.",
        "side_elbowpit_upward": "The left upper arm is extended straight out to the side, forming a right angle with the torso (horizontally aligned with the shoulders). The elbow pit faces upward.",
        "neutral_to_forward": "The left upper arm is raised from the neutral position towards the forward position, forming an approximate 45-degree angle in front of the body.",
        "forward_to_upward": "The left upper arm is raised from the forward position towards the upward position, forming an approximate 45-degree angle from forward towards upwards.",
        "neutral_to_back": "The left upper arm is raised from the neutral position towards the back, forming an approximate 45-degree angle behind the body.",
        "forward_to_midline": "The left upper arm is raised forward and slightly crosses the midline of the body.",
        "forward_to_side": "The left upper arm is extended from the forward position towards the side, forming an approximate 45-degree angle between forward and side.",
        "side_to_back": "The left upper arm is extended from the side position towards the back, forming an approximate 45-degree angle between side and back.",
        "neutral_to_side": "The left upper arm is in the neutral position but extends halfway outward to the side, forming a small angle from the torso.",
        "upward_to_side": "The left upper arm is extended outward from the upwards position towards the side, forming an approximate 45-degree angle between upwards and side.",
        "forward_to_upward_side": "The left upper arm is raised upwards and slightly angled towards the side from the forward position, forming a diagonal line above the shoulder.",
        "forward_to_upward_midline": "The left upper arm is raised upwards and slightly angled towards the midline from the forward position, forming a diagonal line above the shoulder.",
        "side_to_upward_back": "The left upper arm is raised from the side position towards the back and upwards, forming a diagonal reaching upwards and backward.",
        "neutral_to_forward_midline": "The left upper arm is raised upwards and slightly angled towards the midline from the neutral position, forming a diagonal line reaching up.",
        "neutral_to_forward_side": "The left upper arm is raised upwards and slightly angled towards the side from the neutral position, forming a diagonal line reaching up.",
        "neutral_to_backward_side": "The left upper arm is raised upwards and slightly angled towards the back and side from the neutral position, forming a diagonal line reaching up and behind the torso."
    },
    "RightUpperArm": {
        "neutral": "The right upper arm is relaxed and hanging straight down by the side of the body, parallel to the torso.",
        "forward_elbowpit_inward": "The right upper arm is extended straight forward relative to the torso, parallel to the ground and perpendicular to the torso. The elbow pit faces inward to the midline of the body.",
        "forward_elbowpit_upward": "The right upper arm is extended straight forward relative to the torso, parallel to the ground and perpendicular to the torso. The elbow pit faces upward relative to the torso.",
        "upward": "The right upper arm is lifted straight upwards, close to the ear, reaching towards the sky.",
        "side_elbowpit_forward": "The right upper arm is extended straight out to the side, forming a right angle with the torso (horizontally aligned with the shoulders). The elbow pit faces forward.",
        "side_elbowpit_upward": "The right upper arm is extended straight out to the side, forming a right angle with the torso (horizontally aligned with the shoulders). The elbow pit faces upward.",
        "neutral_to_forward": "The right upper arm is raised from the neutral position towards the forward position, forming an approximate 45-degree angle in front of the body.",
        "forward_to_upward": "The right upper arm is raised from the forward position towards the upward position, forming an approximate 45-degree angle from forward towards upwards.",
        "neutral_to_back": "The right upper arm is raised from the neutral position towards the back, forming an approximate 45-degree angle behind the body.",
        "forward_to_midline": "The right upper arm is raised forward and slightly crosses the midline of the body.",
        "forward_to_side": "The right upper arm is extended from the forward position towards the side, forming an approximate 45-degree angle between forward and side.",
        "side_to_back": "The right upper arm is extended from the side position towards the back, forming an approximate 45-degree angle between side and back.",
        "neutral_to_side": "The right upper arm is in the neutral position but extends halfway outward to the side, forming a small angle from the torso.",
        "upward_to_side": "The right upper arm is extended outward from the upwards position towards the side, forming an approximate 45-degree angle between upwards and side.",
        "forward_to_upward_side": "The right upper arm is raised upwards and slightly angled towards the side from the forward position, forming a diagonal line above the shoulder.",
        "forward_to_upward_midline": "The right upper arm is raised upwards and slightly angled towards the midline from the forward position, forming a diagonal line above the shoulder.",
        "side_to_upward_back": "The right upper arm is raised from the side position towards the back and upwards, forming a diagonal reaching upwards and backward.",
        "neutral_to_forward_midline": "The right upper arm is raised upwards and slightly angled towards the midline from the neutral position, forming a diagonal line reaching up.",
        "neutral_to_forward_side": "The right upper arm is raised upwards and slightly angled towards the side from the neutral position, forming a diagonal line reaching up.",
        "neutral_to_backward_side": "The right upper arm is raised upwards and slightly angled towards the back and side from the neutral position, forming a diagonal line reaching up and behind the torso."
    },
    "LeftElbow": {
        "neutral": "The left elbow is extended naturally, forming a straight line from the left shoulder to the left wrist. The left upper arm and left forearm create a nearly straight alignment of about 180 degrees.",
        "slightly_bent_in": "The left forearm forms a slightly obtuse angle with the left upper arm. The left hand moves slightly closer to the left elbow; the muscles in the left upper arm contract slightly.",
        "bent_in_90_degrees": "The left forearm forms a right angle with the left upper arm. The muscles in the left upper arm are moderately contracted.",
        "fully_bent": "The left forearm nearly touches or touches the left upper arm, forming a very acute angle close to zero degrees. The left hand is very close to or touching the left shoulder; the muscles in the left upper arm are fully contracted."
    },
    "RightElbow": {
        "neutral": "The right elbow is extended naturally, forming a straight line from the right shoulder to the right wrist. The right upper arm and right forearm create a nearly straight alignment of about 180 degrees.",
        "slightly_bent_in": "The right forearm forms a slightly obtuse angle with the right upper arm. The right hand moves slightly closer to the right elbow; the muscles in the right upper arm contract slightly.",
        "bent_in_90_degrees": "The right forearm forms a right angle with the right upper arm. The muscles in the right upper arm are moderately contracted.",
        "fully_bent": "The right forearm nearly touches or touches the right upper arm, forming a very acute angle close to zero degrees. The right hand is very close to or touching the right shoulder; the muscles in the right upper arm are fully contracted."
    },
    "LeftWrist": {
        "neutral": "The left wrist extends straight, aligned with the left forearm, forming a continuous straight line from the left elbow to the left hand. The angle between the left forearm and left wrist is close to 180 degrees.",
        "bent_upward": "The left wrist forms a right upward angle with the left forearm. The muscles on the back of the left forearm are fully contracted.",
        "bent_slightly_downward": "The left wrist forms a small downward angle, less than 45 degrees. The left palm moves slightly closer to the left forearm; the muscles on the front of the left forearm contract slightly.",
        "fully_bent_downward": "The left wrist forms a right downward angle with the left forearm. The muscles on the front of the left forearm are fully contracted.",
        "tilted_towards_thumb_side": "The left wrist tilts laterally to form a small angle, less than 20 degrees, moving the thumb side of the left hand closer to the left forearm. The muscles on the thumb side of the left forearm contract slightly.",
        "tilted_towards_pinky_side": "The left wrist tilts laterally to form a small angle, less than 20 degrees, moving the little finger side of the left hand closer to the left forearm. The muscles on the pinky side of the left forearm contract slightly."
    },
    "RightWrist": {
        "neutral": "The right wrist extends straight, aligned with the right forearm, forming a continuous straight line from the right elbow to the right hand. The angle between the right forearm and right wrist is close to 180 degrees.",
        "bent_upward": "The right wrist forms a right upward angle with the right forearm. The muscles on the back of the right forearm are fully contracted.",
        "bent_slightly_downward": "The right wrist forms a small downward angle, less than 45 degrees. The right palm moves slightly closer to the right forearm; the muscles on the front of the right forearm contract slightly.",
        "fully_bent_downward": "The right wrist forms a right downward angle with the right forearm. The muscles on the front of the right forearm are fully contracted.",
        "tilted_towards_thumb_side": "The right wrist tilts laterally to form a small angle, less than 20 degrees, moving the thumb side of the right hand closer to the right forearm. The muscles on the thumb side of the right forearm contract slightly.",
        "tilted_towards_pinky_side": "The right wrist tilts laterally to form a small angle, less than 20 degrees, moving the little finger side of the right hand closer to the right forearm. The muscles on the pinky side of the right forearm contract slightly."
    },
    "LeftUpperLeg": {
        "neutral": "The left upperleg is aligned with the body midline, standing straight with the foot pointing forward relative to the torso.",
        "forward": "The left upperleg is extended forward in front of the body, perpendicular to the torso.",
        "side": "The left upperleg is extended out to the side, perpendicular to the torso.",
        "forward_to_side": "The left upperleg is extended fully forward and slightly to the side, forming an approximate 45-degree angle between the forward direction and the side.",
        "forward_to_midline": "The left upperleg is extended fully forward and slightly towards the midline of the body.",
        "neutral_to_forward": "The left upperleg is lifted from the neutral position and extended forward in front of the body, in the middle of neutral and forward positions.",
        "neutral_to_backward": "The left upperleg is lifted from the neutral position and extended backward behind the body, in the middle of neutral and backward positions.",
        "forward_to_upward": "The left upperleg is slightly raised upwards from the forward position.",
        "neutral_to_side": "The left upperleg is lifted from the neutral position and extended to the side, in the middle of neutral and side positions.",
        "neutral_to_forward_side": "The left upperleg is lifted from the neutral position and extended partly forward and slightly to the side, forming a diagonal line.",
        "neutral_to_forward_midline": "The left upperleg is lifted from the neutral position and extended partly forward and slightly towards the midline of the body.",
        "neutral_to_backward_side": "The left upperleg is lifted from the neutral position and extended partly backward and slightly to the side, forming a diagonal line.",
        "neutral_to_backward_midline": "The left upperleg is lifted from the neutral position and extended partly backward and slightly towards the midline of the body.",
        "forward_to_upward_side": "The left upperleg is extended fully forward and raised partly upwards while slightly moving towards the side.",
        "forward_to_upward_midline": "The left upperleg is extended fully forward and raised partly upwards while slightly moving towards the midline of the body."
    },
    "RightUpperLeg": {
        "neutral": "The right upperleg is aligned with the body midline, standing straight with the foot pointing forward relative to the torso.",
        "forward": "The right upperleg is extended forward in front of the body, perpendicular to the torso.",
        "side": "The right upperleg is extended out to the side, perpendicular to the torso.",
        "forward_to_side": "The right upperleg is extended fully forward and slightly to the side, forming an approximate 45-degree angle between the forward direction and the side.",
        "forward_to_midline": "The right upperleg is extended fully forward and slightly towards the midline of the body.",
        "neutral_to_forward": "The right upperleg is lifted from the neutral position and extended forward in front of the body, in the middle of neutral and forward positions.",
        "neutral_to_backward": "The right upperleg is lifted from the neutral position and extended backward behind the body, in the middle of neutral and backward positions.",
        "forward_to_upward": "The right upperleg is slightly raised upwards from the forward position.",
        "neutral_to_side": "The right upperleg is lifted from the neutral position and extended to the side, in the middle of neutral and side positions.",
        "neutral_to_forward_side": "The right upperleg is lifted from the neutral position and extended partly forward and slightly to the side, forming a diagonal line.",
        "neutral_to_forward_midline": "The right upperleg is lifted from the neutral position and extended partly forward and slightly towards the midline of the body.",
        "neutral_to_backward_side": "The right upperleg is lifted from the neutral position and extended partly backward and slightly to the side, forming a diagonal line.",
        "neutral_to_backward_midline": "The right upperleg is lifted from the neutral position and extended partly backward and slightly towards the midline of the body.",
        "forward_to_upward_side": "The right upperleg is extended fully forward and raised partly upwards while slightly moving towards the side.",
        "forward_to_upward_midline": "The right upperleg is extended fully forward and raised partly upwards while slightly moving towards the midline of the body."
    },
    "LeftKnee": {
        "neutral": "The left leg is straight, the left knee fully extended, forming a continuous line from the the left thigh to the left ankle. The angle between the left thigh and calf is close to 180 degrees. Both the front and back thigh muscles maintain a neutral length.",
        "slightly_bent": "The left calf forms a small angle, less than 45 degrees, with the back of the left thigh. The left knee is slightly flexed; the front thigh muscles contract slightly, and the back thigh muscles lengthen slightly.",
        "bent_at_90_degrees": "The left calf forms a right angle with the left back thigh. The front thigh muscles are moderately contracted, and the back thigh muscles are moderately stretched.",
        "fully_bent": "The left calf forms a nearly zero-degree angle with the back of the left thigh, with the left heel nearly or fully touching the buttocks. The front thigh muscles are extremely contracted, and the back thigh muscles are maximally stretched."
    },
    "RightKnee": {
        "neutral": "The right leg is straight, the right knee fully extended, forming a continuous line from the the right thigh to the right ankle. The angle between the right thigh and calf is close to 180 degrees. Both the front and back thigh muscles maintain a neutral length.",
        "slightly_bent": "The right calf forms a small angle, less than 45 degrees, with the back of the right thigh. The right knee is slightly flexed; the front thigh muscles contract slightly, and the back thigh muscles lengthen slightly.",
        "bent_at_90_degrees": "The right calf forms a right angle with the right back thigh. The front thigh muscles are moderately contracted, and the back thigh muscles are moderately stretched.",
        "fully_bent": "The right calf forms a nearly zero-degree angle with the back of the right thigh, with the right heel nearly or fully touching the buttocks. The front thigh muscles are extremely contracted, and the back thigh muscles are maximally stretched."
    },
    "LeftAnkle": {
        "neutral": "The left toes point straight ahead, aligned with the left foot. The angle between the top of the left foot and the left shin is around 90 degrees. Both the front and back muscles of the left lower leg maintain a neutral length.",
        "bent_upward": "The top of the left foot forms an acute angle, less than 90 degrees, with the left shin. The left toes point closer to the left shin; the muscles on the front of the left lower leg contract to lift the left toes.",
        "bent_downward": "The top of the left foot forms a steep obtuse angle, around 180 degrees, with the left shin. The left toes point significantly downward; the calf muscles are fully contracted.",
        "tilted_inward": "The sole of the left foot moves towards the midline of the body, forming a small inward angle with the left ankle. The muscles on the inside of the left lower leg contract slightly.",
        "tilted_outward": "The sole of the left foot moves away from the midline of the body, forming a small outward angle with the left ankle. The muscles on the outside of the left lower leg contract slightly."
    },
    "RightAnkle": {
        "neutral": "The right toes point straight ahead, aligned with the right foot. The angle between the top of the right foot and the right shin is around 90 degrees. Both the front and back muscles of the right lower leg maintain a neutral length.",
        "bent_upward": "The top of the right foot forms an acute angle, less than 90 degrees, with the right shin. The right toes point closer to the right shin; the muscles on the front of the right lower leg contract to lift the right toes.",
        "bent_downward": "The top of the right foot forms a steep obtuse angle, around 180 degrees, with the right shin. The right toes point significantly downward; the calf muscles are fully contracted.",
        "tilted_inward": "The sole of the right foot moves towards the midline of the body, forming a small inward angle with the right ankle. The muscles on the inside of the right lower leg contract slightly.",
        "tilted_outward": "The sole of the right foot moves away from the midline of the body, forming a small outward angle with the right ankle. The muscles on the outside of the right lower leg contract slightly."
    },
    "LeftToes": {
        "neutral": "The left toes point straight ahead, aligned with the left foot. The left toes and the left foot form a straight line from the base to the tips, making a right angle.",
        "curled_up": "The left toes lift upwards, forming small upward angles between the left toe tips and the left foot. The muscles on the top of the left foot and left toes contract to lift the left toes.",
        "curled_down": "The left toes curl downward, forming small downward angles with the sole of the left foot. The muscles on the bottom of the left foot and left toes contract to curl the left toes."
    },
    "RightToes": {
        "neutral": "The right toes point straight ahead, aligned with the right foot. The right toes and the right foot form a straight line from the base to the tips, making a right angle.",
        "curled_up": "The right toes lift upwards, forming small upward angles between the right toe tips and the right foot. The muscles on the top of the right foot and right toes contract to lift the right toes.",
        "curled_down": "The right toes curl downward, forming small downward angles with the sole of the right foot. The muscles on the bottom of the right foot and right toes contract to curl the right toes."
    }
}


body_part_hierarchical_questions_prompts = {
    "json_schema": {
        "title": "next_position_clarification",
        "description": "Clarifying the next position of the body part",
        "type": "object",
        "properties": {
            "next_position": {
                "type": "string",
                "description": "Clarifying the next position of the body part",
                "enum": []
            }
        },
        "required": ["next_position"]
    },
    "Head": {
        "question": "At the end of this step, is the head upright in the neutral position, tilted left, tilted right, tilted down, tilted up, turned left or turned right? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "tilted_left": {
                "question": "Is the head tilted left slightly or fully? Choose one from %s",
                "options": {
                    "tilted_left_slightly": "tilted_left_slightly",
                    "tilted_left_fully": "tilted_left_fully"
                }
            },
            "tilted_right": {
                "question": "Is the head tilted right slightly or fully? Choose one from %s",
                "options": {
                    "tilted_right_slightly": "tilted_right_slightly",
                    "tilted_right_fully": "tilted_right_fully"
                }
            },
            "tilted_down": {
                "question": "Is the head tilted down slightly or fully? Choose one from %s",
                "options": {
                    "tilted_down_slightly": "tilted_down_slightly",
                    "tilted_down_fully": "tilted_down_fully"
                }
            },
            "tilted_up": {
                "question": "Is the head tilted up slightly or fully? Choose one from %s",
                "options": {
                    "tilted_up_slightly": "tilted_up_slightly",
                    "tilted_up_fully": "tilted_up_fully"
                }
            },
            "turned_left": {
                "question": "Is the head turned left slightly or fully? Choose one from %s",
                "options": {
                    "turned_left_slightly": "turned_left_slightly",
                    "turned_left_fully": "turned_left_fully"
                }
            },
            "turned_right": {
                "question": "Is the head turned right slightly or fully? Choose one from %s",
                "options": {
                    "turned_right_slightly": "turned_right_slightly",
                    "turned_right_fully": "turned_right_fully"
                }
            }
        }
    },
    "Torso": {
        "question": "At the end of this step, is the torso upright in the neutral position, bent forward, bent backward, tilted left, tilted right, twisted left or twisted right? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "bent_backward": "bent_backward",
            "bent_forward": {
                "question": "Is the torso bent forward slightly or fully? Choose one from %s",
                "options": {
                    "bent_forward_slightly": "bent_forward_slightly",
                    "bent_forward_fully": "bent_forward_fully"
                }
            },
            "tilted_left": {
                "question": "Is the torso tilted left slightly or fully? Choose one from %s",
                "options": {
                    "tilted_left_slightly": "tilted_left_slightly",
                    "tilted_left_fully": "tilted_left_fully"
                }
            },
            "tilted_right": {
                "question": "Is the torso tilted right slightly or fully? Choose one from %s",
                "options": {
                    "tilted_right_slightly": "tilted_right_slightly",
                    "tilted_right_fully": "tilted_right_fully"
                }
            },
            "twisted_left": {
                "question": "Is the torso twisted left slightly or fully? Choose one from %s",
                "options": {
                    "twisted_left_slightly": "twisted_left_slightly",
                    "twisted_left_fully": "twisted_left_fully"
                }
            },
            "twisted_right": {
                "question": "Is the torso twisted right slightly or fully? Choose one from %s",
                "options": {
                    "twisted_right_slightly": "twisted_right_slightly",
                    "twisted_right_fully": "twisted_right_fully"
                }
            }
        }
    },
    "LeftUpperArm": {
        "question": "At the end of this step, relative to the torso, is the left upper arm neutrally resting by the side of the body, straight upward, straight forward, straight out to the side forming a right angle with the torso, or in other in-between positions? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "upward": "upward",
            "forward": {
                "question": "Is the left elbow pit facing inward to the midline of the body or upward relative to the torso? Choose one from %s",
                "options": {
                    "forward_elbowpit_inward": "forward_elbowpit_inward",
                    "forward_elbowpit_upward": "forward_elbowpit_upward"
                }
            },
            "side": {
                "question": "Is the left elbow pit facing forward or upward relative to the torso? Choose one from %s",
                "options": {
                    "side_elbowpit_forward": "side_elbowpit_forward",
                    "side_elbowpit_upward": "side_elbowpit_upward"
                }
            },
            "in_between_positions": {
                "question": "Relative to the torso, is the left upper arm out to the side, towards the midline of the body, or neither? Choose one from %s",
                "options": {
                    "out_to_side": {
                        "question": "Relative to the torso, is the left upper arm in front of the body, behind the body, or neither? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the left upper arm above the left shoulder, below the left shoulder, or neither? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward_side",
                                    "below": "neutral_to_forward_side",
                                    "neither": "forward_to_side"
                                }
                            },
                            "behind": {
                                "question": "Relative to the torso, is the left upper arm above the left shoulder, below the left shoulder, or neither? Choose one from %s",
                                "options": {
                                    "above": "side_to_upward_back",
                                    "below": "neutral_to_backward_side",
                                    "neither": "side_to_back"
                                }
                            },
                            "neither": {
                                "question": "Relative to the torso, is the left upper arm above the left shoulder or below the left shoulder? Choose one from %s",
                                "options": {
                                    "above": "upward_to_side",
                                    "below": "neutral_to_side"
                                }
                            }
                        }
                    },
                    "towards_midline": {
                        "question": "Relative to the torso, is the left upper arm above the left shoulder, below the left shoulder, or neither? Choose one from %s",
                        "options": {
                            "above": "forward_to_upward_midline",
                            "below": "neutral_to_forward_midline",
                            "neither": "forward_to_midline"
                        }
                    },
                    "neither": {
                        "question": "Relative to the torso, is the left upper arm in front of the body or behind the body? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the left upper arm above the left shoulder or below the left shoulder? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward",
                                    "below": "neutral_to_forward"
                                }
                            },
                            "behind": "neutral_to_back"
                        }
                    }
                }
            }
        }
    },
    "RightUpperArm": {
        "question": "At the end of this step, relative to the torso, is the right upper arm neutrally resting by the side of the body, straight upward, straight forward, straight out to the side forming a right angle with the torso, or in other in-between positions? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "upward": "upward",
            "forward": {
                "question": "Is the right elbow pit facing inward to the midline of the body or upward relative to the torso? Choose one from %s",
                "options": {
                    "forward_elbowpit_inward": "forward_elbowpit_inward",
                    "forward_elbowpit_upward": "forward_elbowpit_upward"
                }
            },
            "side": {
                "question": "Is the right elbow pit facing forward or upward relative to the torso? Choose one from %s",
                "options": {
                    "side_elbowpit_forward": "side_elbowpit_forward",
                    "side_elbowpit_upward": "side_elbowpit_upward"
                }
            },
            "in_between_positions": {
                "question": "Relative to the torso, is the right upper arm out to the side, towards the midline of the body, or neither? Choose one from %s",
                "options": {
                    "out_to_side": {
                        "question": "Relative to the torso, is the right upper arm in front of the body, behind the body, or neither? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the right upper arm above the right shoulder, below the right shoulder, or neither? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward_side",
                                    "below": "neutral_to_forward_side",
                                    "neither": "forward_to_side"
                                }
                            },
                            "behind": {
                                "question": "Relative to the torso, is the right upper arm above the right shoulder, below the right shoulder, or neither? Choose one from %s",
                                "options": {
                                    "above": "side_to_upward_back",
                                    "below": "neutral_to_backward_side",
                                    "neither": "side_to_back"
                                }
                            },
                            "neither": {
                                "question": "Relative to the torso, is the right upper arm above the right shoulder or below the right shoulder? Choose one from %s",
                                "options": {
                                    "above": "upward_to_side",
                                    "below": "neutral_to_side"
                                }
                            }
                        }
                    },
                    "towards_midline": {
                        "question": "Relative to the torso, is the right upper arm above the right shoulder, below the right shoulder, or neither? Choose one from %s",
                        "options": {
                            "above": "forward_to_upward_midline",
                            "below": "neutral_to_forward_midline",
                            "neither": "forward_to_midline"
                        }
                    },
                    "neither": {
                        "question": "Relative to the torso, is the right upper arm in front of the body or behind the body? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the right upper arm above the right shoulder or below the right shoulder? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward",
                                    "below": "neutral_to_forward"
                                }
                            },
                            "behind": "neutral_to_back"
                        }
                    }
                }
            }
        }
    },
    "LeftElbow": {
        "question": "At the end of this step, is the left elbow stright or bent? Choose one from %s",
        "options": {
            "straight": "neutral",
            "bent": {
                "question": "Is the left elbow slightly bent in, bent in 90 degrees or fully bent? Choose one from %s",
                "options": {
                    "slightly_bent_in": "slightly_bent_in",
                    "bent_in_90_degrees": "bent_in_90_degrees",
                    "fully_bent": "fully_bent"
                }
            }
        }
    },
    "RightElbow": {
        "question": "At the end of this step, is the right elbow stright or bent? Choose one from %s",
        "options": {
            "straight": "neutral",
            "bent": {
                "question": "Is the right elbow slightly bent in, bent in 90 degrees or fully bent? Choose one from %s",
                "options": {
                    "slightly_bent_in": "slightly_bent_in",
                    "bent_in_90_degrees": "bent_in_90_degrees",
                    "fully_bent": "fully_bent"
                }
            }
        }
    },
    "LeftWrist": {
        "question": "At the end of this step, is the left wrist straight in the neutral position, bent vertically, or tilted sideways? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "bent_vertically": {
                "question": "Is the left wrist bent upward so that the back of the left hand is closer to the back of the left forearm, with the muscles of the back of the left forearm contracted? Or is the left wrist bent downward so that the left palm moves towards the left forearm? Choose one from %s",
                "options": {
                    "bent_upward": "bent_upward",
                    "bent_downward": {
                        "question": "Is the left wrist slightly bent downward or fully? Choose one from %s",
                        "options": {
                            "bent_slightly_downward": "bent_slightly_downward",
                            "fully_bent_downward": "fully_bent_downward"
                        }
                    }
                }
            },
            "tilted_sideways": {
                "question": "Is the left wrist tilted laterally towards the left thumb, or the left little finger? Choose one from %s",
                "options": {
                    "tilted_towards_thumb_side": "tilted_towards_thumb_side",
                    "tilted_towards_pinky_side": "tilted_towards_pinky_side"
                }
            }
        }
    },
    "RightWrist": {
        "question": "At the end of this step, is the right wrist straight in the neutral position, bent vertically, or tilted sideways? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "bent_vertically": {
                "question": "Is the right wrist bent upward so that the back of the right hand is closer to the back of the right forearm, with the muscles of the back of the right forearm contracted? Or is the right wrist bent downward so that the right palm moves towards the right forearm? Choose one from %s",
                "options": {
                    "bent_upward": "bent_upward",
                    "bent_downward": {
                        "question": "Is the right wrist slightly bent downward or fully? Choose one from %s",
                        "options": {
                            "bent_slightly_downward": "bent_slightly_downward",
                            "fully_bent_downward": "fully_bent_downward"
                        }
                    }
                }
            },
            "tilted_sideways": {
                "question": "Is the right wrist tilted laterally towards the right thumb, or the right little finger? Choose one from %s",
                "options": {
                    "tilted_towards_thumb_side": "tilted_towards_thumb_side",
                    "tilted_towards_pinky_side": "tilted_towards_pinky_side"
                }
            }
        }
    },
    "LeftUpperLeg": {
        "question": "At the end of this step, is the left upper leg neutrally aligned with the body midline, straight forward, straight out to the side forming a right angle with the torso, or in other in-between positions? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "forward": "forward",
            "side": "side",
            "in_between_positions": {
                "question": "Relative to the torso, is the left upper leg out to the side, towards the midline of the body, or neither? Choose one from %s",
                "options": {
                    "out_to_side" : {
                        "question": "Relative to the torso, is the left upper leg in front of the body, behind the body, or neither? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the left upper leg above the left pelvis, below the left pelvis, or neither? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward_side",
                                    "below": "neutral_to_forward_side",
                                    "neither": "forward_to_side"
                                }
                            },
                            "behind": "neutral_to_backward_side",
                            "neither": "neutral_to_side"
                        }
                    },
                    "towards_midline": {
                        "question": "Relative to the torso, is the left upper leg in front of the body or behind the body? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the left upper leg above the left pelvis, below the left pelvis, or neither? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward_midline",
                                    "below": "neutral_to_forward_midline",
                                    "neither": "forward_to_midline"
                                }
                            },
                            "behind": "neutral_to_backward_midline"
                        }
                    },
                    "neither": {
                        "question": "Relative to the torso, is the left upper leg in front of the body or behind the body? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the left upper leg above the left pelvis or below the left pelvis? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward",
                                    "below": "neutral_to_forward"
                                }
                            },
                            "behind": "neutral_to_backward"
                        }
                    }
                }
            }
        }
    },
    "RightUpperLeg": {
        "question": "At the end of this step, is the right upper leg neutrally aligned with the body midline, straight forward, straight out to the side forming a right angle with the torso, or in other in-between positions? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "forward": "forward",
            "side": "side",
            "in_between_positions": {
                "question": "Relative to the torso, is the right upper leg out to the side, towards the midline of the body, or neither? Choose one from %s",
                "options": {
                    "out_to_side" : {
                        "question": "Relative to the torso, is the right upper leg in front of the body, behind the body, or neither? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the right upper leg above the right pelvis, below the right pelvis, or neither? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward_side",
                                    "below": "neutral_to_forward_side",
                                    "neither": "forward_to_side"
                                }
                            },
                            "behind": "neutral_to_backward_side",
                            "neither": "neutral_to_side"
                        }
                    },
                    "towards_midline": {
                        "question": "Relative to the torso, is the right upper leg in front of the body or behind the body? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the right upper leg above the right pelvis, below the right pelvis, or neither? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward_midline",
                                    "below": "neutral_to_forward_midline",
                                    "neither": "forward_to_midline"
                                }
                            },
                            "behind": "neutral_to_backward_midline"
                        }
                    },
                    "neither": {
                        "question": "Relative to the torso, is the right upper leg in front of the body or behind the body? Choose one from %s",
                        "options": {
                            "front": {
                                "question": "Relative to the torso, is the right upper leg above the right pelvis or below the right pelvis? Choose one from %s",
                                "options": {
                                    "above": "forward_to_upward",
                                    "below": "neutral_to_forward"
                                }
                            },
                            "behind": "neutral_to_backward"
                        }
                    }
                }
            }
        }
    },
    "LeftKnee": {
        "question": "At the end of this step, is the left knee stright or bent? Choose one from %s",
        "options": {
            "straight": "neutral",
            "bent": {
                "question": "Is the left knee slightly bent, bent at 90 degrees or fully bent? Choose one from %s",
                "options": {
                    "slightly_bent": "slightly_bent",
                    "bent_at_90_degrees": "bent_at_90_degrees",
                    "fully_bent": "fully_bent"
                }
            }
        }
    },
    "RightKnee": {
        "question": "At the end of this step, is the right knee stright or bent? Choose one from %s",
        "options": {
            "straight": "neutral",
            "bent": {
                "question": "Is the right knee slightly bent, bent at 90 degrees or fully bent? Choose one from %s",
                "options": {
                    "slightly_bent": "slightly_bent",
                    "bent_at_90_degrees": "bent_at_90_degrees",
                    "fully_bent": "fully_bent"
                }
            }
        }
    },
    "LeftAnkle": {
        "question": "At the end of this step, is the left ankle in a neutral position like when standing? Or is the left ankle bent vertically? Or is the left ankle tilted so that the sole moves towards the side or midline? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "bent_vertically": {
                "question": "Is the left ankle bent upward so that the top of the left foot forms an acute angle with the left shin? Or is the left ankle bent downward so that the top of the left foot forms an obtuse angle with the left shin? Choose one from %s",
                "options": {
                    "bent_upward": "bent_upward",
                    "bent_downward": "bent_downward"
                }
            },
            "tilted_inward_or_outward": {
                "question": "Is the left ankle tilted inwards so that the left sole moves towards the midline of the body? Or is the left ankle tilted outwards so that the left sole moves away from the midline of the body? Choose one from %s",
                "options": {
                    "tilted_inward": "tilted_inward",
                    "tilted_outward": "tilted_outward"
                }
            }
        }
    },
    "RightAnkle": {
        "question": "At the end of this step, is the right ankle in a neutral position like when standing? Or is the right ankle bent vertically? Or is the right ankle tilted so that the sole moves towards the side or midline? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "bent_vertically": {
                "question": "Is the right ankle bent upward so that the top of the right foot forms an acute angle with the right shin? Or is the right ankle bent downward so that the top of the right foot forms an obtuse angle with the right shin? Choose one from %s",
                "options": {
                    "bent_upward": "bent_upward",
                    "bent_downward": "bent_downward"
                }
            },
            "tilted_inward_or_outward": {
                "question": "Is the right ankle tilted inwards so that the right sole moves towards the midline of the body? Or is the right ankle tilted outwards so that the right sole moves away from the midline of the body? Choose one from %s",
                "options": {
                    "tilted_inward": "tilted_inward",
                    "tilted_outward": "tilted_outward"
                }
            }
        }
    },
    "LeftToes": {
        "question": "At the end of this step, are the left toes in the neutral position or curled? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "curled": {
                "question": "Are the left toes curled up or down? Choose one from %s",
                "options": {
                    "curled_up": "curled_up",
                    "curled_down": "curled_down"
                }
            }
        }
    },
    "RightToes": {
        "question": "At the end of this step, are the right toes in the neutral position or curled? Choose one from %s",
        "options": {
            "neutral": "neutral",
            "curled": {
                "question": "Are the right toes curled up or down? Choose one from %s",
                "options": {
                    "curled_up": "curled_up",
                    "curled_down": "curled_down"
                }
            }
        }
    }
}