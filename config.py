body_part_group = [
    ["Head"],
    ["Torso"],
    ["LeftUpperArm", "RightUpperArm", "LeftElbow", "RightElbow", "LeftWrist", "RightWrist"],
    ["LeftUpperLeg", "RightUpperLeg", "LeftKnee", "RightKnee", "LeftAnkle", "RightAnkle", "LeftToes", "RightToes"]
]

positions_map = {
    "Head": {
        "neutral": {"m_avg_Head": [0.0, 0.0, 0.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "tilted_up_slightly": {"m_avg_Head": [-30.0, 0.0, 0.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "tilted_up_fully": {"m_avg_Head": [-45.0, 0.0, 0.0], "m_avg_Neck": [-10.0, 0.0, 0.0]},
        "tilted_down_slightly": {"m_avg_Head": [30.0, 0.0, 0.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "tilted_down_fully": {"m_avg_Head": [45.0, 0.0, 0.0], "m_avg_Neck": [30.0, 0.0, 0.0]},
        "turned_left_slightly": {"m_avg_Head": [0.0, -45.0, 0.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "turned_left_fully": {"m_avg_Head": [0.0, -60.0, 0.0], "m_avg_Neck": [0.0, -30.0, 0.0]},
        "turned_right_slightly": {"m_avg_Head": [0.0, 45.0, 0.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "turned_right_fully": {"m_avg_Head": [0.0, 60.0, 0.0], "m_avg_Neck": [0.0, 30.0, 0.0]},
        "tilted_left_slightly": {"m_avg_Head": [0.0, 0.0, 20.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "tilted_left_fully": {"m_avg_Head": [0.0, 0.0, 45.0], "m_avg_Neck": [0.0, 0.0, 20.0]},
        "tilted_right_slightly": {"m_avg_Head": [0.0, 0.0, -20.0], "m_avg_Neck": [0.0, 0.0, 0.0]},
        "tilted_right_fully": {"m_avg_Head": [0.0, 0.0, -45.0], "m_avg_Neck": [0.0, 0.0, -20.0]}
    },
    "Torso": {
        "neutral": {"m_avg_Spine1": [0.0, 0.0, 0.0], "m_avg_Spine2": [0.0, 0.0, 0.0], "m_avg_Spine3": [0.0, 0.0, 0.0]},
        "twisted_left_slightly": {"m_avg_Spine1": [0.0, -20.0, 0.0], "m_avg_Spine2": [0.0, -10.0, 0.0], "m_avg_Spine3": [0.0, -5.0, 0.0]},
        "twisted_left_fully": {"m_avg_Spine1": [0.0, -30.0, 0.0], "m_avg_Spine2": [0.0, -20.0, 0.0], "m_avg_Spine3": [0.0, -10.0, 0.0]},
        "twisted_right_slightly": {"m_avg_Spine1": [0.0, 20.0, 0.0], "m_avg_Spine2": [0.0, 10.0, 0.0], "m_avg_Spine3": [0.0, 5.0, 0.0]},
        "twisted_right_fully": {"m_avg_Spine1": [0.0, 30.0, 0.0], "m_avg_Spine2": [0.0, 20.0, 0.0], "m_avg_Spine3": [0.0, 0.0, 10.0]},
        "bent_forward_slightly": {"m_avg_Spine1": [30.0, 0.0, 0.0], "m_avg_Spine2": [5.0, 0.0, 0.0], "m_avg_Spine3": [5.0, 0.0, 0.0]},
        "bent_forward_fully": {"m_avg_Spine1": [60.0, 0.0, 0.0], "m_avg_Spine2": [10.0, 0.0, 0.0], "m_avg_Spine3": [10.0, 0.0, 0.0]},
        "bent_backward": {"m_avg_Spine1": [-20.0, 0.0, 0.0], "m_avg_Spine2": [0.0, 0.0, 0.0], "m_avg_Spine3": [0.0, 0.0, 0.0]},
        "tilted_left_slightly": {"m_avg_Spine1": [0.0, 0.0, 10.0], "m_avg_Spine2": [0.0, 0.0, 5.0], "m_avg_Spine3": [0.0, 0.0, 5.0]},
        "tilted_left_fully": {"m_avg_Spine1": [0.0, 0.0, 20.0], "m_avg_Spine2": [0.0, 0.0, 10.0], "m_avg_Spine3": [0.0, 0.0, 10.0]},
        "tilted_right_slightly": {"m_avg_Spine1": [0.0, 0.0, -10.0], "m_avg_Spine2": [0.0, 0.0, -5.0], "m_avg_Spine3": [0.0, 0.0, -5.0]},
        "tilted_right_fully": {"m_avg_Spine1": [0.0, 0.0, -20.0], "m_avg_Spine2": [0.0, 0.0, -10.0], "m_avg_Spine3": [0.0, 0.0, -10.0]}
    },
    "LeftUpperArm": {
        "neutral": {"m_avg_L_Collar": [0.0, 0.0, 20.0], "m_avg_L_Shoulder": [0.0, 0.0, 70.0]},
        "forward_elbowpit_inward": {"m_avg_L_Collar": [0.0, 0.0, 0.0], "m_avg_L_Shoulder": [0.0, 90.0, 0.0]},
        "forward_elbowpit_upward": {"m_avg_L_Collar": [0.0, 0.0, 20.0], "m_avg_L_Shoulder": [-70.0, 90.0, 0.0]},
        "upward": {"m_avg_L_Collar": [0.0, 0.0, -45.0], "m_avg_L_Shoulder": [0.0, 0.0, -40.0]},
        "side_elbowpit_forward": {"m_avg_L_Collar": [0.0, 0.0, 0.0], "m_avg_L_Shoulder": [0.0, 0.0, 0.0]},
        "side_elbowpit_upward": {"m_avg_L_Collar": [-45.0, 0.0, 0.0], "m_avg_L_Shoulder": [-45.0, 0.0, 0.0]},
        "neutral_to_forward": {"m_avg_L_Collar": [0.0, 0.0, 10.0], "m_avg_L_Shoulder": [-60.0, 20.0, 70.0]},
        "forward_to_upward": {"m_avg_L_Collar": [0.0, 0.0, -10.0], "m_avg_L_Shoulder": [0.0, 90.0, -35.0]},
        "neutral_to_back": {"m_avg_L_Collar": [0.0, 0.0, 10.0], "m_avg_L_Shoulder": [10.0, 90.0, 120.0]},
        "forward_to_midline": {"m_avg_L_Collar": [0.0, 10.0, 0.0], "m_avg_L_Shoulder": [0.0, 120.0, 0.0]},
        "forward_to_side": {"m_avg_L_Collar": [0.0, 10.0, 0.0], "m_avg_L_Shoulder": [0.0, 30.0, 0.0]},
        "side_to_back": {"m_avg_L_Collar": [0.0, -10.0, 0.0], "m_avg_L_Shoulder": [0.0, -30.0, 0.0]},
        "neutral_to_side": {"m_avg_L_Collar": [0.0, 0.0, 10.0], "m_avg_L_Shoulder": [0.0, 0.0, 45.0]},
        "upward_to_side": {"m_avg_L_Collar": [0.0, 0.0, -10.0], "m_avg_L_Shoulder": [0.0, 0.0, -45.0]},
        "forward_to_upward_side": {"m_avg_L_Collar": [0.0, 0.0, -10.0], "m_avg_L_Shoulder": [0.0, 45.0, -30.0]},
        "forward_to_upward_midline": {"m_avg_L_Collar": [0.0, 15.0, -10.0], "m_avg_L_Shoulder": [0.0, 110.0, -30.0]},
        "side_to_upward_back": {"m_avg_L_Collar": [0.0, -15.0, -10.0], "m_avg_L_Shoulder": [0.0, -30.0, -30.0]},
        "neutral_to_forward_midline": {"m_avg_L_Collar": [0.0, 0.0, 10.0], "m_avg_L_Shoulder": [-45.0, 0.0, 100.0]},
        "neutral_to_forward_side": {"m_avg_L_Collar": [0.0, 0.0, 10.0], "m_avg_L_Shoulder": [45.0, 90.0, 45.0]},
        "neutral_to_backward_side": {"m_avg_L_Collar": [20.0, 0.0, 10.0], "m_avg_L_Shoulder": [45.0, 90.0, 100.0]}
    },
    "RightUpperArm": {
        "neutral": {"m_avg_R_Collar": [0.0, 0.0, -20.0], "m_avg_R_Shoulder": [0.0, 0.0, -70.0]},
        "forward_elbowpit_inward": {"m_avg_R_Collar": [0.0, 0.0, 0.0], "m_avg_R_Shoulder": [0.0, -90.0, 0.0]},
        "forward_elbowpit_upward": {"m_avg_R_Collar": [0.0, 0.0, -20.0], "m_avg_R_Shoulder": [-70.0, -90.0, 0.0]},
        "upward": {"m_avg_R_Collar": [0.0, 0.0, 45.0], "m_avg_R_Shoulder": [0.0, 0.0, 40.0]},
        "side_elbowpit_forward": {"m_avg_R_Collar": [0.0, 0.0, 0.0], "m_avg_R_Shoulder": [0.0, 0.0, 0.0]},
        "side_elbowpit_upward": {"m_avg_R_Collar": [-45.0, 0.0, 0.0], "m_avg_R_Shoulder": [-45.0, 0.0, 0.0]},
        "neutral_to_forward": {"m_avg_R_Collar": [0.0, 0.0, -10.0], "m_avg_R_Shoulder": [-60.0, -20.0, -70.0]},
        "forward_to_upward": {"m_avg_R_Collar": [0.0, 0.0, 10.0], "m_avg_R_Shoulder": [0.0, -90.0, 35.0]},
        "neutral_to_back": {"m_avg_R_Collar": [0.0, 0.0, -10.0], "m_avg_R_Shoulder": [10.0, -90.0, -120.0]},
        "forward_to_midline": {"m_avg_R_Collar": [0.0, -10.0, 0.0], "m_avg_R_Shoulder": [0.0, -120.0, 0.0]},
        "forward_to_side": {"m_avg_R_Collar": [0.0, -10.0, 0.0], "m_avg_R_Shoulder": [0.0, -30.0, 0.0]},
        "side_to_back": {"m_avg_R_Collar": [0.0, 10.0, 0.0], "m_avg_R_Shoulder": [0.0, 30.0, 0.0]},
        "neutral_to_side": {"m_avg_R_Collar": [0.0, 0.0, -10.0], "m_avg_R_Shoulder": [0.0, 0.0, -45.0]},
        "upward_to_side": {"m_avg_R_Collar": [0.0, 0.0, 10.0], "m_avg_R_Shoulder": [0.0, 0.0, 45.0]},
        "forward_to_upward_side": {"m_avg_R_Collar": [0.0, 0.0, 10.0], "m_avg_R_Shoulder": [0.0, -45.0, 30.0]},
        "forward_to_upward_midline": {"m_avg_R_Collar": [0.0, -15.0, 10.0], "m_avg_R_Shoulder": [0.0, -110.0, 30.0]},
        "side_to_upward_back": {"m_avg_R_Collar": [0.0, 15.0, 10.0], "m_avg_R_Shoulder": [0.0, 30.0, 30.0]},
        "neutral_to_forward_midline": {"m_avg_R_Collar": [0.0, 0.0, -10.0], "m_avg_R_Shoulder": [-45.0, 0.0, -100.0]},
        "neutral_to_forward_side": {"m_avg_R_Collar": [0.0, 0.0, -10.0], "m_avg_R_Shoulder": [45.0, -90.0, -45.0]},
        "neutral_to_backward_side": {"m_avg_R_Collar": [20.0, 0.0, -10.0], "m_avg_R_Shoulder": [45.0, -90.0, -100.0]}
    },
    "LeftElbow": {
        "neutral": {"m_avg_L_Elbow": [0.0, 0.0, 0.0]},
        "slightly_bent_in": {"m_avg_L_Elbow": [0.0, 45.0, 0.0]},
        "bent_in_90_degrees": {"m_avg_L_Elbow": [0.0, 90.0, 0.0]},
        "fully_bent": {"m_avg_L_Elbow": [0.0, 135.0, 0.0]},
    },
    "RightElbow": {
        "neutral": {"m_avg_R_Elbow": [0.0, 0.0, 0.0]},
        "slightly_bent_in": {"m_avg_R_Elbow": [0.0, -45.0, 0.0]},
        "bent_in_90_degrees": {"m_avg_R_Elbow": [0.0, -90.0, 0.0]},
        "fully_bent": {"m_avg_R_Elbow": [0.0, -135.0, 0.0]},
    },
    "LeftWrist": {
        "neutral": {"m_avg_L_Wrist": [0.0, 0.0, 0.0]},
        "bent_upward": {"m_avg_L_Wrist": [0.0, 0.0, -45.0]},
        "bent_slightly_downward": {"m_avg_L_Wrist": [0.0, 0.0, 45.0]},
        "fully_bent_downward": {"m_avg_L_Wrist": [0.0, 0.0, 80.0]},
        "tilted_towards_thumb_side": {"m_avg_L_Wrist": [0.0, 30.0, 0.0]},
        "tilted_towards_pinky_side": {"m_avg_L_Wrist": [0.0, -30.0, 0.0]}
    },
    "RightWrist": {
        "neutral": {"m_avg_R_Wrist": [0.0, 0.0, 0.0]},
        "bent_upward": {"m_avg_R_Wrist": [0.0, 0.0, 45.0]},
        "bent_slightly_downward": {"m_avg_R_Wrist": [0.0, 0.0, -45.0]},
        "fully_bent_downward": {"m_avg_R_Wrist": [0.0, 0.0, -80.0]},
        "tilted_towards_thumb_side": {"m_avg_R_Wrist": [0.0, -30.0, 0.0]},
        "tilted_towards_pinky_side": {"m_avg_R_Wrist": [0.0, 30.0, 0.0]}
    },
    "LeftUpperLeg": {
        "neutral": {"m_avg_L_Hip": [0.0, 0.0, 0.0]},
        "forward": {"m_avg_L_Hip": [-90.0, 0.0, 0.0]},
        "side": {"m_avg_L_Hip": [0.0, 0.0, -80.0]},
        "forward_to_side": {"m_avg_L_Hip": [-90.0, 0.0, -45.0]},
        "forward_to_midline": {"m_avg_L_Hip": [-90.0, 0.0, 45.0]},
        "neutral_to_forward": {"m_avg_L_Hip": [-45.0, 0.0, 0.0]},
        "neutral_to_backward": {"m_avg_L_Hip": [45.0, 0.0, 0.0]},
        "forward_to_upward": {"m_avg_L_Hip": [-120.0, 0.0, 0.0]},
        "neutral_to_side": {"m_avg_L_Hip": [0.0, 0.0, -45.0]},
        "neutral_to_forward_side": {"m_avg_L_Hip": [-45.0, 0.0, -45.0]},
        "neutral_to_forward_midline": {"m_avg_L_Hip": [-45.0, 0.0, 45.0]},
        "neutral_to_backward_side": {"m_avg_L_Hip": [45.0, 0.0, -45.0]},
        "neutral_to_backward_midline": {"m_avg_L_Hip": [45.0, 0.0, 45.0]},
        "forward_to_upward_side": {"m_avg_L_Hip": [-120.0, 0.0, -45.0]},
        "forward_to_upward_midline": {"m_avg_L_Hip": [-120.0, 0.0, 45.0]}
    },
    "RightUpperLeg": {
        "neutral": {"m_avg_R_Hip": [0.0, 0.0, 0.0]},
        "forward": {"m_avg_R_Hip": [-90.0, 0.0, 0.0]},
        "side": {"m_avg_R_Hip": [0.0, 0.0, 80.0]},
        "forward_to_side": {"m_avg_R_Hip": [-90.0, 0.0, 45.0]},
        "forward_to_midline": {"m_avg_R_Hip": [-90.0, 0.0, -45.0]},
        "neutral_to_forward": {"m_avg_R_Hip": [-45.0, 0.0, 0.0]},
        "neutral_to_backward": {"m_avg_R_Hip": [45.0, 0.0, 0.0]},
        "forward_to_upward": {"m_avg_R_Hip": [-120.0, 0.0, 0.0]},
        "neutral_to_side": {"m_avg_R_Hip": [0.0, 0.0, 45.0]},
        "neutral_to_forward_side": {"m_avg_R_Hip": [-45.0, 0.0, 45.0]},
        "neutral_to_forward_midline": {"m_avg_R_Hip": [-45.0, 0.0, -45.0]},
        "neutral_to_backward_side": {"m_avg_R_Hip": [45.0, 0.0, 45.0]},
        "neutral_to_backward_midline": {"m_avg_R_Hip": [45.0, 0.0, -45.0]},
        "forward_to_upward_side": {"m_avg_R_Hip": [-120.0, 0.0, 45.0]},
        "forward_to_upward_midline": {"m_avg_R_Hip": [-120.0, 0.0, -45.0]}
    },
    "LeftKnee": {
        "neutral": {"m_avg_L_Knee": [0.0, 0.0, 0.0]},
        "slightly_bent": {"m_avg_L_Knee": [45.0, 0.0, 0.0]},
        "bent_at_90_degrees": {"m_avg_L_Knee": [90.0, 0.0, 0.0]},
        "fully_bent": {"m_avg_L_Knee": [135.0, 0.0, 0.0]}
    },
    "RightKnee": {
        "neutral": {"m_avg_R_Knee": [0.0, 0.0, 0.0]},
        "slightly_bent": {"m_avg_R_Knee": [45.0, 0.0, 0.0]},
        "bent_at_90_degrees": {"m_avg_R_Knee": [90.0, 0.0, 0.0]},
        "fully_bent": {"m_avg_R_Knee": [135.0, 0.0, 0.0]}
    },
    "LeftAnkle": {
        "neutral": {"m_avg_L_Ankle": [0.0, 0.0, 0.0]},
        "bent_upward": {"m_avg_L_Ankle": [-20.0, 0.0, 0.0]},
        "bent_downward": {"m_avg_L_Ankle": [45.0, 0.0, 0.0]},
        "tilted_inward": {"m_avg_L_Ankle": [0.0, 0.0, 30.0]},
        "tilted_outward": {"m_avg_L_Ankle": [0.0, 0.0, -10.0]}
    },
    "RightAnkle": {
        "neutral": {"m_avg_R_Ankle": [0.0, 0.0, 0.0]},
        "bent_upward": {"m_avg_R_Ankle": [-20.0, 0.0, 0.0]},
        "bent_downward": {"m_avg_R_Ankle": [45.0, 0.0, 0.0]},
        "tilted_inward": {"m_avg_R_Ankle": [0.0, 0.0, -30.0]},
        "tilted_outward": {"m_avg_R_Ankle": [0.0, 0.0, 10.0]}
    },
    "LeftToes": {
        "neutral": {"m_avg_L_Foot": [0.0, 0.0, 0.0]},
        "curled_up": {"m_avg_L_Foot": [-30.0, 0.0, 0.0]},
        "curled_down": {"m_avg_L_Foot": [30.0, 0.0, 0.0]}
    },
    "RightToes": {
        "neutral": {"m_avg_R_Foot": [0.0, 0.0, 0.0]},
        "curled_up": {"m_avg_R_Foot": [-30.0, 0.0, 0.0]},
        "curled_down": {"m_avg_R_Foot": [30.0, 0.0, 0.0]}
    }
}