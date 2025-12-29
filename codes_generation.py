import json
import argparse
from os.path import join as pjoin
from typing import *
from config import positions_map



codes_template = "\
using System.Collections.Generic;\n\
using UnityEngine;\n\
\n\
public class MyAnimation_%s : MonoBehaviour\n\
{\n\
    // Declare the Transform variables for the joints to move\n\
    private Transform m_avg_root;\n\
    private Transform m_avg_L_Hip, m_avg_R_Hip, m_avg_L_Knee, m_avg_R_Knee, m_avg_L_Ankle, m_avg_R_Ankle, m_avg_L_Foot, m_avg_R_Foot;\n\
    private Transform m_avg_Spine1, m_avg_Spine2, m_avg_Spine3;\n\
    private Transform m_avg_Neck, m_avg_Head;\n\
    private Transform m_avg_L_Collar, m_avg_R_Collar, m_avg_L_Shoulder, m_avg_R_Shoulder, m_avg_L_Elbow, m_avg_R_Elbow, m_avg_L_Wrist, m_avg_R_Wrist;\n\
\n\
    // The dictionary to store the Transform variables for the joints\n\
    private Dictionary<string, Transform> jointsTransform;\n\
    private Dictionary<string, Quaternion> accumulatedRotations;\n\
\n\
    private int lastCompletedStep = -1; // Variable to track the last completed step\n\
\n\
    // Declare the general control variables for the animation\n\
    public float animationTime = %sf;\n\
    private float localTime = 0f;\n\
\n\
    void Start()\n\
    {\n\
        InitializeJoints();\n\
        InitializeAccumulatedRotations();\n\
    }\n\
\n\
    void Update()\n\
    {\n\
        localTime += Time.deltaTime;\n\
        if (localTime <= animationTime)\n\
        {\n\
            Animation(localTime);\n\
        }\n\
    }\n\
\n\
    private void InitializeJoints()\n\
    {\n\
        // Automatically assign the joint variables to the objects in the SMPL human model\n\
        m_avg_root = transform.Find(\"m_avg_root\");\n\
        m_avg_L_Hip = m_avg_root.Find(\"m_avg_Pelvis/m_avg_L_Hip\");\n\
        m_avg_R_Hip = m_avg_root.Find(\"m_avg_Pelvis/m_avg_R_Hip\");\n\
        m_avg_L_Knee = m_avg_L_Hip.Find(\"m_avg_L_Knee\");\n\
        m_avg_R_Knee = m_avg_R_Hip.Find(\"m_avg_R_Knee\");\n\
        m_avg_L_Ankle = m_avg_L_Knee.Find(\"m_avg_L_Ankle\");\n\
        m_avg_R_Ankle = m_avg_R_Knee.Find(\"m_avg_R_Ankle\");\n\
        m_avg_L_Foot = m_avg_L_Ankle.Find(\"m_avg_L_Foot\");\n\
        m_avg_R_Foot = m_avg_R_Ankle.Find(\"m_avg_R_Foot\");\n\
        m_avg_Spine1 = m_avg_root.Find(\"m_avg_Pelvis/m_avg_Spine1\");\n\
        m_avg_Spine2 = m_avg_Spine1.Find(\"m_avg_Spine2\");\n\
        m_avg_Spine3 = m_avg_Spine2.Find(\"m_avg_Spine3\");\n\
        m_avg_Neck = m_avg_Spine3.Find(\"m_avg_Neck\");\n\
        m_avg_Head = m_avg_Neck.Find(\"m_avg_Head\");\n\
        m_avg_L_Collar = m_avg_Spine3.Find(\"m_avg_L_Collar\");\n\
        m_avg_R_Collar = m_avg_Spine3.Find(\"m_avg_R_Collar\");\n\
        m_avg_L_Shoulder = m_avg_L_Collar.Find(\"m_avg_L_Shoulder\");\n\
        m_avg_R_Shoulder = m_avg_R_Collar.Find(\"m_avg_R_Shoulder\");\n\
        m_avg_L_Elbow = m_avg_L_Shoulder.Find(\"m_avg_L_Elbow\");\n\
        m_avg_R_Elbow = m_avg_R_Shoulder.Find(\"m_avg_R_Elbow\");\n\
        m_avg_L_Wrist = m_avg_L_Elbow.Find(\"m_avg_L_Wrist\");\n\
        m_avg_R_Wrist = m_avg_R_Elbow.Find(\"m_avg_R_Wrist\");\n\
\n\
        jointsTransform = new Dictionary<string, Transform>\n\
        {\n\
            { \"m_avg_L_Hip\", m_avg_L_Hip },\n\
            { \"m_avg_R_Hip\", m_avg_R_Hip },\n\
            { \"m_avg_L_Knee\", m_avg_L_Knee },\n\
            { \"m_avg_R_Knee\", m_avg_R_Knee },\n\
            { \"m_avg_L_Ankle\", m_avg_L_Ankle },\n\
            { \"m_avg_R_Ankle\", m_avg_R_Ankle },\n\
            { \"m_avg_L_Foot\", m_avg_L_Foot },\n\
            { \"m_avg_R_Foot\", m_avg_R_Foot },\n\
            { \"m_avg_Spine1\", m_avg_Spine1 },\n\
            { \"m_avg_Spine2\", m_avg_Spine2 },\n\
            { \"m_avg_Spine3\", m_avg_Spine3 },\n\
            { \"m_avg_Neck\", m_avg_Neck },\n\
            { \"m_avg_Head\", m_avg_Head },\n\
            { \"m_avg_L_Collar\", m_avg_L_Collar },\n\
            { \"m_avg_R_Collar\", m_avg_R_Collar },\n\
            { \"m_avg_L_Shoulder\", m_avg_L_Shoulder },\n\
            { \"m_avg_R_Shoulder\", m_avg_R_Shoulder },\n\
            { \"m_avg_L_Elbow\", m_avg_L_Elbow },\n\
            { \"m_avg_R_Elbow\", m_avg_R_Elbow },\n\
            { \"m_avg_L_Wrist\", m_avg_L_Wrist },\n\
            { \"m_avg_R_Wrist\", m_avg_R_Wrist }\n\
        };\n\
    }\n\
\n\
    private void InitializeAccumulatedRotations()\n\
    {\n\
        accumulatedRotations = new Dictionary<string, Quaternion>\n\
        {\n\
            { \"m_avg_L_Hip\", Quaternion.identity },\n\
            { \"m_avg_R_Hip\", Quaternion.identity },\n\
            { \"m_avg_L_Knee\", Quaternion.identity },\n\
            { \"m_avg_R_Knee\", Quaternion.identity },\n\
            { \"m_avg_L_Ankle\", Quaternion.identity },\n\
            { \"m_avg_R_Ankle\", Quaternion.identity },\n\
            { \"m_avg_L_Foot\", Quaternion.identity },\n\
            { \"m_avg_R_Foot\", Quaternion.identity },\n\
            { \"m_avg_Spine1\", Quaternion.identity },\n\
            { \"m_avg_Spine2\", Quaternion.identity },\n\
            { \"m_avg_Spine3\", Quaternion.identity },\n\
            { \"m_avg_Neck\", Quaternion.identity },\n\
            { \"m_avg_Head\", Quaternion.identity },\n\
            { \"m_avg_L_Collar\", Quaternion.Euler(0.0f, 0.0f, 20.0f) }, // From T-pose to natural pose\n\
            { \"m_avg_R_Collar\", Quaternion.Euler(0.0f, 0.0f, -20.0f) }, // From T-pose to natural pose\n\
            { \"m_avg_L_Shoulder\", Quaternion.Euler(0.0f, 0.0f, 70.0f) }, // From T-pose to natural pose\n\
            { \"m_avg_R_Shoulder\", Quaternion.Euler(0.0f, 0.0f, -70.0f) }, // From T-pose to natural pose\n\
            { \"m_avg_L_Elbow\", Quaternion.identity },\n\
            { \"m_avg_R_Elbow\", Quaternion.identity },\n\
            { \"m_avg_L_Wrist\", Quaternion.identity },\n\
            { \"m_avg_R_Wrist\", Quaternion.identity }\n\
        };\n\
\n\
        jointsTransform[\"m_avg_L_Collar\"].localRotation = accumulatedRotations[\"m_avg_L_Collar\"];\n\
        jointsTransform[\"m_avg_R_Collar\"].localRotation = accumulatedRotations[\"m_avg_R_Collar\"];\n\
        jointsTransform[\"m_avg_L_Shoulder\"].localRotation = accumulatedRotations[\"m_avg_L_Shoulder\"];\n\
        jointsTransform[\"m_avg_R_Shoulder\"].localRotation = accumulatedRotations[\"m_avg_R_Shoulder\"];\n\
    }\n\
\n\
    void Animation(float time)\n\
    {\n\
        int currentStep = -1;\n\
        Dictionary<string, List<(Quaternion rotation, (float startTime, float endTime) timeRange)>> targetRotations = null;\n\
\n\
%s\n\
\n\
        if (targetRotations != null)\n\
        {\n\
            // Update accumulated rotations only if transitioning to a new step\n\
            if (currentStep != lastCompletedStep)\n\
            {\n\
                foreach (var jointName in targetRotations.Keys)\n\
                {\n\
                    accumulatedRotations[jointName] = jointsTransform[jointName].localRotation;\n\
                }\n\
                lastCompletedStep = currentStep;\n\
            }\n\
            AnimateJoints(time, targetRotations);\n\
        }\n\
    }\n\
\n\
    void AnimateJoints(float time, Dictionary<string, List<(Quaternion rotation, (float startTime, float endTime) timeRange)>> targetRotations)\n\
    {\n\
        foreach (string jointName in jointsTransform.Keys)\n\
        {\n\
            if (targetRotations != null && targetRotations.ContainsKey(jointName))\n\
            {\n\
                foreach (var (targetRotation, (jointStartTime, jointEndTime)) in targetRotations[jointName])\n\
                {\n\
                    if (time >= jointStartTime && time < jointEndTime)\n\
                    {\n\
                        float t = (time - jointStartTime) / (jointEndTime - jointStartTime);\n\
                        Quaternion innerRotation = Quaternion.Slerp(accumulatedRotations[jointName], targetRotation, t);\n\
                        jointsTransform[jointName].localRotation = innerRotation;\n\
                    }\n\
                }\n\
            }\n\
        }\n\
    }\n\
}"

step_codes_template = "\
        if (time >= %s && time < %s) // %s\n\
        {\n\
            currentStep = %s;\n\
            targetRotations = new Dictionary<string, List<(Quaternion, (float, float))>>\n\
            {\n\
            // Rotations\n\
%s\n\
            };\n\
        }"

joint_transform_template = "\
                { \"%s\", new List<(Quaternion, (float, float))> { (Quaternion.Euler(%sf, %sf, %sf), (%sf, %sf)) } }"


def build_step_codes(step):
    joints_transform_codes = ""
    step_time_range = step["time_range"]
    step_number = step["step_number"]

    for body_part in step["changed_body_parts_states"]:
        initial_pos, final_pos = step["changed_body_parts_states"][body_part]
        for joint in positions_map[body_part][initial_pos].keys():
            target_quantity = positions_map[body_part][final_pos][joint]
            joint_quaternion = joint_transform_template % (joint, target_quantity[0], target_quantity[1], target_quantity[2], step_time_range[0], step_time_range[1])
            joints_transform_codes += (joint_quaternion + ",\n")

    step_codes = step_codes_template % (
        step_time_range[0], step_time_range[1], f"Step {step_number}",
        step_number,
        joints_transform_codes
    )
    return step_codes


def generate_codes(args):

    with open(args.motion_instructions_path, "r", encoding="utf8") as rf:
        motion_instructions = json.load(rf)

    for motion_i, motion_instruction in enumerate(motion_instructions):
        if motion_i >= args.start_motion_i:
            with open(pjoin(args.results_folder_path, args.summarized_steps_plans_filename % motion_i), "r", encoding="utf8") as rf:
                summarized_steps_plans = json.load(rf)
            finish_time = summarized_steps_plans[-1]["time_range"][-1] # The finish time of the animation
            
            steps_codes = ""
            for step in summarized_steps_plans:
                steps_codes += (build_step_codes(step) + "\n")
            
            codes = codes_template % (motion_i, finish_time, steps_codes)
            with open(pjoin(args.results_folder_path, args.output_codes_filename % motion_i), "w", encoding="utf8") as wf:
                wf.write(codes)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--motion_instructions_path", type=str, default="./motion_instructions/application.json")
    parser.add_argument("--summarized_steps_plans_filename", type=str, default="summarized_steps_plans_%s.json")
    parser.add_argument("--results_folder_path", type=str, default="results")
    parser.add_argument("--output_codes_filename", type=str, default="MyAnimation_%s.cs")
    parser.add_argument("--start_motion_i", type=int, default=0, help="specify which motion to generate")
    args = parser.parse_args()

    generate_codes(args)