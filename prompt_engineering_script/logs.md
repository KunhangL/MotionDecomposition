# Important Information in Prompts
- Human Model Hierarchy JSON
```
{"m_avg_root": {"joint_name": "m_avg_root", "position": [0, 0, 0], "children": {"m_avg_Pelvis": {"joint_name": "m_avg_Pelvis", "position": [0.00217367915589215, 0.972723857779389, 0.0285837934769579], "children": {"m_avg_L_Hip": {"joint_name": "m_avg_L_Hip", "position": [-0.0585813504507656, -0.0822800412730611, -0.0176640839745186], "children": {"m_avg_L_Knee": {"joint_name": "m_avg_L_Knee", "position": [-0.0434514314503899, -0.386469457538986, 0.00803700217630674], "children": {"m_avg_L_Ankle": {"joint_name": "m_avg_L_Ankle", "position": [0.01479033494873, -0.426874391452085, -0.0374279940964569], "children": {"m_avg_L_Foot": {"joint_name": "m_avg_L_Foot", "position": [-0.0410543674633154, -0.0602859492311727, 0.12204242350686]}}}}}}}, "m_avg_R_Hip": {"joint_name": "m_avg_R_Hip", "position": [0.0603097291884147, -0.0905132843011647, -0.01354252931849], "children": {"m_avg_R_Knee": {"joint_name": "m_avg_R_Knee", "position": [0.0432566254253949, -0.383687877466446, -0.00484304494182445], "children": {"m_avg_R_Ankle": {"joint_name": "m_avg_R_Ankle", "position": [-0.019055544286818, -0.420045587890346, -0.0345616702037777], "children": {"m_avg_R_Foot": {"joint_name": "m_avg_R_Foot", "position": [0.0348398706827247, -0.062105561171744, 0.130323289537847]}}}}}}}, "m_avg_Spine1": {"joint_name": "m_avg_Spine1", "position": [-0.00443944898221867, 0.124403551233992, -0.0383852227732937], "children": {"m_avg_Spine2": {"joint_name": "m_avg_Spine2", "position": [-0.0044884401766645, 0.137956399353686, 0.0268203279187967], "children": {"m_avg_Spine3": {"joint_name": "m_avg_Spine3", "position": [0.00226458745836407, 0.0560324043117619, 0.00285504453980784], "children": {"m_avg_Neck": {"joint_name": "m_avg_Neck", "position": [0.0133901850163491, 0.211635514692671, -0.0334675763976523], "children": {"m_avg_Head": {"joint_name": "m_avg_Head", "position": [-0.0101132115910344, 0.088937353899629, 0.0504098606300206]}}}, "m_avg_L_Collar": {"joint_name": "m_avg_L_Collar", "position": [-0.0717024751888973, 0.113999713923281, -0.0188981710845057], "children": {"m_avg_L_Shoulder": {"joint_name": "m_avg_L_Shoulder", "position": [-0.122921382186775, 0.045205076329708, -0.019045999826937], "children": {"m_avg_L_Elbow": {"joint_name": "m_avg_L_Elbow", "position": [-0.255331898315701, -0.0156490327473171, -0.0229464854803309], "children": {"m_avg_L_Wrist": {"joint_name": "m_avg_L_Wrist", "position": [-0.265709255263499, 0.0126981037070203, -0.00737473431115989], "children": {"m_avg_L_Hand": {"joint_name": "m_avg_L_Hand", "position": [-0.0866905441238188, -0.0106360603299893, -0.0155942904792877]}}}}}}}}}, "m_avg_R_Collar": {"joint_name": "m_avg_R_Collar", "position": [0.0829536517743771, 0.112472303849185, -0.0237073845553838], "children": {"m_avg_R_Shoulder": {"joint_name": "m_avg_R_Shoulder", "position": [0.113228312318425, 0.0468532786471522, -0.00847206923501845], "children": {"m_avg_R_Elbow": {"joint_name": "m_avg_R_Elbow", "position": [0.260127500631845, -0.0143692952953938, -0.0312687296438665], "children": {"m_avg_R_Wrist": {"joint_name": "m_avg_R_Wrist", "position": [0.269108382383609, 0.00679372784357952, -0.00602676583284452], "children": {"m_avg_R_Hand": {"joint_name": "m_avg_R_Hand", "position": [0.0887537661914463, -0.00865157243230385, -0.0101070787784667]}}}}}}}}}}}}}}}}}}}}
```
- C# Generation
```
Based on the hierarchy of this human model, generate a C# animation script for the following textual description
[TEXT]
 ## Checklist
 1. The trigger key should be "SPACE".
 2. Don't use the animation controller.
 3. Please **automatically** assign the root joint in the script, using `root = transform.Find("m_avg_root")`
 4. For the root body part 'm_avg_root', you can perform both translation and rotation.
 5. For all the other body parts except for the root body part, you can only perform rotation.
 6. You should generate the process of the animation instead of just the final pose.
 7. The body parts should move in reasonable speed.
 8. The class name should be "MyAnimation"
 9.  Please respectively apply transforms to left and right parts of the body, as they might not follow the same direction specifications. For example, the local Y-rotations of Left Shoulder and Right Shoulder are opposite.
... (TBA)
```
- Hierarchical Rotation Specifications from the Initial T-pose
```
1. Root (m_avg_root):
- Typically, the root joint handles global positioning and rotation of the entire model.
2. Pelvis (m_avg_Pelvis):
    - Local X Rotation (pitch): (+) Tilts the pelvis forward / (-) Tilts the pelvis backward.
    - Local Y Rotation (yaw): (+) Rotates the pelvis right / (-) Rotates the pelvis left.
    - Local Z Rotation (roll): (+) Tilts the pelvis to the left side / (-) Tilts the pelvis to the right side.
    // Example: Slight tilt forward for pelvis
    // m_avg_Pelvis.localRotation = Quaternion.Euler(10, 0, 0);
3. Left Hip (m_avg_L_Hip):
    - Local X Rotation (pitch): (+) Moves the left leg backward / (-) Moves the left leg forward.
    - Local Y Rotation (yaw): (+) Swivels the left leg inward / (-) Swivels the left leg outward.
    - Local Z Rotation (roll):  (+) Twists the left leg counterclockwise / (-) Twists the left leg clockwise.
    // Example: Raise the left leg forward by 30 degrees
    // m_avg_L_Hip.localRotation = Quaternion.Euler(-30, 0, 0);
4. Left Knee (m_avg_L_Knee):
    - Local X Rotation (pitch): (+) Bends the knee backward / (-) Bends the knee forward.
    - Local Y Rotation (yaw): (+) Twists the knee inward / (-) Twists the knee outward.
    - Local Z Rotation (roll): Null (DO NOT CHANGE IT)
    // Example: Bend the left knee 45 degrees
    // m_avg_L_Knee.localRotation = Quaternion.Euler(45, 0, 0);
5. Left Ankle (m_avg_L_Ankle):
    - Local X Rotation (pitch): (+) Points the left foot down / (-) Points the left foot up.
    - Local Y Rotation (yaw): (+) Twists the left foot inward / (-) Twists the left foot outward.
    - Local Z Rotation (roll): (+) Tilts the left foot so that the left sole is more towards the midline of the body / (-) Tilts the left foot so that the left sole is less towards the midline of the body.
    // Example: Point the left foot down 30 degrees
    // m_avg_L_Ankle.localRotation = Quaternion.Euler(30, 0, 0);
6. Left Foot (m_avg_L_Foot): Null (DO NOT MOVE IT)
7. Right Hip (m_avg_R_Hip):
    - Local X Rotation (pitch): (+) Moves the right leg backward / (-) Moves the right leg forward.
    - Local Y Rotation (yaw): (+) Swivels the right leg outward / (-) Swivels the right leg inward.
    - Local Z Rotation (roll):  (+) Twists the right leg counterclockwise / (-) Twists the right leg clockwise.
    // Example: Raise the right leg forward by 30 degrees
    // m_avg_R_Hip.localRotation = Quaternion.Euler(-30, 0, 0);
8. Right Knee (m_avg_R_Knee):
    - Local X Rotation (pitch): (+) Bends the knee backward / (-) Bends the knee forward.
    - Local Y Rotation (yaw): (+) Twists the knee outward / (-) Twists the knee inward.
    - Local Z Rotation (roll): Null (DO NOT CHANGE IT)
    // Example: Bend the right knee 45 degrees
    // m_avg_R_Knee.localRotation = Quaternion.Euler(45, 0, 0);
9. Right Ankle (m_avg_R_Ankle):
    - Local X Rotation (pitch): (+) Points the right foot down / (-) Points the right foot up.
    - Local Y Rotation (yaw): (+) Twists the right foot outward / (-) Twists the right foot inward.
    - Local Z Rotation (roll): (+) Tilts the right foot so that the right sole is less towards the midline of the body / (-) Tilts the right foot so that the right sole is more towards the midline of the body.
    // Example: Point the right foot down 30 degrees
    // m_avg_R_Ankle.localRotation = Quaternion.Euler(30, 0, 0);
10. Right Foot (m_avg_R_Foot): Null (DO NOT MOVE IT)
11. Spine1, Spine2, Spine3:
    - Local X Rotation (pitch): (+) Bends the spine forward / (-) Bends the spine backward.
    - Local Y Rotation (yaw): (+) Twists the torso right / (-) Twists the torso left.
    - Local Z Rotation (roll): (+) Tilts the torso to the left side / (-) Tilts the torso to the right side.
    // Example: Slight forward bend
    // m_avg_Spine1.localRotation = Quaternion.Euler(10, 0, 0);
    // m_avg_Spine2.localRotation = Quaternion.Euler(5, 0, 0);
    // m_avg_Spine3.localRotation = Quaternion.Euler(2, 0, 0);
12. Neck (m_avg_Neck):
    - Local X Rotation (pitch): (+) Tilts the head down / (-) Tilts the head up.
    - Local Y Rotation (yaw): (+) Turns the head right / (-) Turns the head left.
    - Local Z Rotation (roll): (+) Tilts the head to the left side / (-) Tilts the head to the right side.
    // Example: Look at the sky
    // m_avg_Neck.localRotation = Quaternion.Euler(-20, 0, 0);
13. Head (m_avg_Head):
    - Fine adjustments to head rotation, similar to Neck (m_avg_Neck).
    // Example: Look slightly to the left
    //m_avg_Head.localRotation = Quaternion.Euler(0, -10, 0);
14. Left Collar (m_avg_L_Collar): Null (DO NOT MOVE IT)
15. Left Shoulder (m_avg_L_Shoulder):
    - Local X Rotation (pitch): (+) Twists the left arm so that the left palm faces backward / (-) Twists the left arm so that the left palm faces backward.
    - Local Y Rotation (yaw): (+) Moves the arm forward / (-) Moves the arm backward.
    - Local Z Rotation (roll): (+) Lowers the arm / (-) Raises the arm.
    // Example: Raise the left arm by 45 degrees
    // m_avg_L_Shoulder.localRotation = Quaternion.Euler(0, 0, -45);
16. Left Elbow (m_avg_L_Elbow):
    - Local X Rotation (pitch): (+) Twists the left forearm so that the left palm faces backward / (-) Twists the left forearm so that the left palm faces backward.
    - Local Y Rotation (yaw): (+) Moves the left forearm forward / (-) Null.
    - Local Z Rotation (roll): Null
    // Example: Twist the left forearm so that the left palm faces backward
    // m_avg_L_Elbow.localRotation = Quaternion.Euler(30, 0, 0);
17. Left Wrist (m_avg_L_Wrist):
    - Local X Rotation (pitch): (+) Twist the left wrist so that the left palm faces backward / (-) Twist the left wrist so that the left palm faces forward.
    - Local Y Rotation (yaw): (+) Tilts the left hand forward / (-) Tilts the left hand backward.
    - Local Z Rotation (roll): (+) Tilts the left hand down / (-) Tilts the left hand up.
    // Example: Tilt the left hand upward
    // m_avg_L_Wrist.localRotation = Quaternion.Euler(0, 0, -30);
18. Left Hand (m_avg_L_Hand): Null (DO NOT MOVE IT)
19. Right Collar (m_avg_R_Collar): Null (DO NOT MOVE IT)
20. Right Shoulder (m_avg_R_Shoulder):
    - Local X Rotation (pitch): (+) Twists the right arm so that the right palm faces backward / (-) Twists the left arm so that the left palm faces backward.
    - Local Y Rotation (yaw): (+) Moves the arm backward / (-) Moves the arm forward.
    - Local Z Rotation (roll): (+) Raises the arm / (-) Lowers the arm.
    // Example: Raise the right arm by 45 degrees
    // m_avg_R_Shoulder.localRotation = Quaternion.Euler(0, 0, 45);
21. Right Elbow (m_avg_R_Elbow):
    - Local X Rotation (pitch): (+) Twists the right forearm so that the right palm faces backward / (-) Twists the right forearm so that the right palm faces backward.
    - Local Y Rotation (yaw): (+) Null / (-) Moves the right forearm forward.
    - Local Z Rotation (roll): Null
    // Example: Twist the right forearm so that the right palm faces backward
    // m_avg_R_Elbow.localRotation = Quaternion.Euler(30, 0, 0);
22. Right Wrist (m_avg_R_Wrist):
    - Local X Rotation (pitch): (+) Twist the right wrist so that the right palm faces backward / (-) Twist the right wrist so that the right palm faces forward.
    - Local Y Rotation (yaw): (+) Tilts the right hand backward / (-) Tilts the right hand forward.
    - Local Z Rotation (roll): (+) Tilts the right hand up / (-) Tilts the right hand down.
    // Example: Tilt the right hand upward
    // m_avg_L_Wrist.localRotation = Quaternion.Euler(0, 0, 30);
23. Right Hand (m_avg_R_Hand): Null (DO NOT MOVE IT)
```


# Prompts

## Notes
- Human Model Hierarchy JSON
- +Rotation specifications (examples / detailed specifications / detailed examples) and ground specifications

## Showcases

### Version 1: Human Model Hierarchy JSON
- System
```
You are an animator to be provided the joints on a rigged 3D human model in Unity, and you need to rotate them to produce the requested animation from a textual motion description. The joints of the human model are shown below, stored as a JSON string that outlines the object hierarchy.

**Human Model JSON**
{"m_avg_root": {"joint_name": "m_avg_root", "position": [0, 0, 0], "children": {"m_avg_Pelvis": {"joint_name": "m_avg_Pelvis", "position": [0.00217367915589215, 0.972723857779389, 0.0285837934769579], "children": {"m_avg_L_Hip": {"joint_name": "m_avg_L_Hip", "position": [-0.0585813504507656, -0.0822800412730611, -0.0176640839745186], "children": {"m_avg_L_Knee": {"joint_name": "m_avg_L_Knee", "position": [-0.0434514314503899, -0.386469457538986, 0.00803700217630674], "children": {"m_avg_L_Ankle": {"joint_name": "m_avg_L_Ankle", "position": [0.01479033494873, -0.426874391452085, -0.0374279940964569], "children": {"m_avg_L_Foot": {"joint_name": "m_avg_L_Foot", "position": [-0.0410543674633154, -0.0602859492311727, 0.12204242350686]}}}}}}}, "m_avg_R_Hip": {"joint_name": "m_avg_R_Hip", "position": [0.0603097291884147, -0.0905132843011647, -0.01354252931849], "children": {"m_avg_R_Knee": {"joint_name": "m_avg_R_Knee", "position": [0.0432566254253949, -0.383687877466446, -0.00484304494182445], "children": {"m_avg_R_Ankle": {"joint_name": "m_avg_R_Ankle", "position": [-0.019055544286818, -0.420045587890346, -0.0345616702037777], "children": {"m_avg_R_Foot": {"joint_name": "m_avg_R_Foot", "position": [0.0348398706827247, -0.062105561171744, 0.130323289537847]}}}}}}}, "m_avg_Spine1": {"joint_name": "m_avg_Spine1", "position": [-0.00443944898221867, 0.124403551233992, -0.0383852227732937], "children": {"m_avg_Spine2": {"joint_name": "m_avg_Spine2", "position": [-0.0044884401766645, 0.137956399353686, 0.0268203279187967], "children": {"m_avg_Spine3": {"joint_name": "m_avg_Spine3", "position": [0.00226458745836407, 0.0560324043117619, 0.00285504453980784], "children": {"m_avg_Neck": {"joint_name": "m_avg_Neck", "position": [0.0133901850163491, 0.211635514692671, -0.0334675763976523], "children": {"m_avg_Head": {"joint_name": "m_avg_Head", "position": [-0.0101132115910344, 0.088937353899629, 0.0504098606300206]}}}, "m_avg_L_Collar": {"joint_name": "m_avg_L_Collar", "position": [-0.0717024751888973, 0.113999713923281, -0.0188981710845057], "children": {"m_avg_L_Shoulder": {"joint_name": "m_avg_L_Shoulder", "position": [-0.122921382186775, 0.045205076329708, -0.019045999826937], "children": {"m_avg_L_Elbow": {"joint_name": "m_avg_L_Elbow", "position": [-0.255331898315701, -0.0156490327473171, -0.0229464854803309], "children": {"m_avg_L_Wrist": {"joint_name": "m_avg_L_Wrist", "position": [-0.265709255263499, 0.0126981037070203, -0.00737473431115989], "children": {"m_avg_L_Hand": {"joint_name": "m_avg_L_Hand", "position": [-0.0866905441238188, -0.0106360603299893, -0.0155942904792877]}}}}}}}}}, "m_avg_R_Collar": {"joint_name": "m_avg_R_Collar", "position": [0.0829536517743771, 0.112472303849185, -0.0237073845553838], "children": {"m_avg_R_Shoulder": {"joint_name": "m_avg_R_Shoulder", "position": [0.113228312318425, 0.0468532786471522, -0.00847206923501845], "children": {"m_avg_R_Elbow": {"joint_name": "m_avg_R_Elbow", "position": [0.260127500631845, -0.0143692952953938, -0.0312687296438665], "children": {"m_avg_R_Wrist": {"joint_name": "m_avg_R_Wrist", "position": [0.269108382383609, 0.00679372784357952, -0.00602676583284452], "children": {"m_avg_R_Hand": {"joint_name": "m_avg_R_Hand", "position": [0.0887537661914463, -0.00865157243230385, -0.0101070787784667]}}}}}}}}}}}}}}}}}}}}
```
- User
```
Based on the hierarchy of this human model, generate a C# animation script for the following textual description
[TEXT]
 ## Checklist
 1. The trigger key should be "SPACE".
 2. Don't use the animation controller.
 3. Please **automatically** assign the root joint in the script.
 3. Any body parts cannot sink into the ground, which means the Y position should always be greater than 0.
 4. For the root body part 'm_avg_root', you can perform both translation and rotation.
 5. For all the other body parts except for the root body part, you can only perform rotation.
 6. You should generate the process of the animation instead of just the final pose.
 7. The body parts should move in reasonable speed.
```
- Cases
1. "From the original T-pose, a person continually walks."

```
Sure! Below is a C# script for Unity that will animate a character model based on the given hierarchy and textual description:

using UnityEngine;

public class SquatWithArmForward : MonoBehaviour
{
    private Transform rootJoint;
    private Transform leftHip, leftKnee, leftAnkle, leftFoot;
    private Transform rightHip, rightKnee, rightAnkle, rightFoot;
    private Transform spine1, spine2, spine3, neck, head;
    private Transform leftShoulder, leftElbow, leftWrist, leftHand;
    private Transform rightShoulder, rightElbow, rightWrist, rightHand;
    private Vector3 initialRootPosition;
    private Quaternion initialRootRotation;

    private float animationSpeed = 1.0f;
    private bool isAnimating = false;
    private float currentTime = 0.0f;
    private float animationDuration = 2.0f;

    void Start()
    {
        rootJoint = transform.Find("m_avg_root");
        leftHip = rootJoint.Find("m_avg_Pelvis/m_avg_L_Hip");
        leftKnee = leftHip.Find("m_avg_L_Knee");
        leftAnkle = leftKnee.Find("m_avg_L_Ankle");
        leftFoot = leftAnkle.Find("m_avg_L_Foot");
        
        rightHip = rootJoint.Find("m_avg_Pelvis/m_avg_R_Hip");
        rightKnee = rightHip.Find("m_avg_R_Knee");
        rightAnkle = rightKnee.Find("m_avg_R_Ankle");
        rightFoot = rightAnkle.Find("m_avg_R_Foot");
        
        spine1 = rootJoint.Find("m_avg_Pelvis/m_avg_Spine1");
        spine2 = spine1.Find("m_avg_Spine2");
        spine3 = spine2.Find("m_avg_Spine3");
        neck = spine3.Find("m_avg_Neck");
        head = neck.Find("m_avg_Head");

        leftShoulder = spine3.Find("m_avg_L_Collar/m_avg_L_Shoulder");
        leftElbow = leftShoulder.Find("m_avg_L_Elbow");
        leftWrist = leftElbow.Find("m_avg_L_Wrist");
        leftHand = leftWrist.Find("m_avg_L_Hand");

        rightShoulder = spine3.Find("m_avg_R_Collar/m_avg_R_Shoulder");
        rightElbow = rightShoulder.Find("m_avg_R_Elbow");
        rightWrist = rightElbow.Find("m_avg_R_Wrist");
        rightHand = rightWrist.Find("m_avg_R_Hand");

        initialRootPosition = rootJoint.position;
        initialRootRotation = rootJoint.rotation;
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            isAnimating = true;
            currentTime = 0.0f;
        }

        if (isAnimating)
        {
            currentTime += Time.deltaTime * animationSpeed;
            float progress = currentTime / animationDuration;

            if (progress >= 1.0f)
            {
                progress = 1.0f;
                isAnimating = false;
            }

            AnimateSquatWithArmForward(progress);
        }
    }

    void AnimateSquatWithArmForward(float progress)
    {
        // Translation and rotation for the root joint
        rootJoint.position = Vector3.Lerp(initialRootPosition, initialRootPosition + new Vector3(0, -0.5f, 0), progress);

        // Rotation for hips, knees, and ankles for squatting
        RotateJoint(leftHip, new Vector3(-60, 0, 0), progress);
        RotateJoint(leftKnee, new Vector3(60, 0, 0), progress);
        RotateJoint(leftAnkle, new Vector3(-30, 0, 0), progress);

        RotateJoint(rightHip, new Vector3(-60, 0, 0), progress);
        RotateJoint(rightKnee, new Vector3(60, 0, 0), progress);
        RotateJoint(rightAnkle, new Vector3(-30, 0, 0), progress);

        // Rotation for arms moving forward
        RotateJoint(leftShoulder, new Vector3(90, 0, 0), progress);
        RotateJoint(leftElbow, new Vector3(-30, 0, 0), progress);
        RotateJoint(leftWrist, new Vector3(0, 0, 0), progress);

        RotateJoint(rightShoulder, new Vector3(90, 0, 0), progress);
        RotateJoint(rightElbow, new Vector3(-30, 0, 0), progress);
        RotateJoint(rightWrist, new Vector3(0, 0, 0), progress);
    }

    void RotateJoint(Transform joint, Vector3 rotation, float progress)
    {
        joint.localRotation = Quaternion.Lerp(Quaternion.identity, Quaternion.Euler(rotation), progress);
    }
}

### Explanation
1. **Initialization:**
   - At the start of the script, the joints are retrieved using `Transform.Find` based on the provided hierarchy.
  
2. **Input Handling:**
   - The script listens for the `SPACE` key press to trigger the animation.

3. **Animation Logic:**
   - The `AnimateSquatWithArmForward` method smoothly interpolates the joint rotations and root position over the `animationDuration`.

4. **Joint Rotation:**
   - The `RotateJoint` helper method handles the interpolation of joint rotations from the initial identity quaternion to the target rotation quaternion.

5. **Root Joint Movement:**
   - The root joint is both translated and rotated to simulate squatting.

6. **Avoid Ground Penetration:**
   - The root joint maintains a downward translation without sinking into the ground (keeping track of `Y` position).

7. **Duration and Speed:**
   - The animation progresses over a specified duration, ensuring a reasonable movement speed.
```

<video src="squat_arms_1.mov" controls="controls" width="500" height="300"></video>

2. "From the original T-pose, a person jumps and then lands."
<video src="jump_1.mov" controls="controls" width="500" height="300"></video>

3. "From the original T-pose, a person squats while moving the arms forward."
<video src="walk_1.mov" controls="controls" width="500" height="300"></video>


### Version 2: Human Model Hierarchy JSON + Rotation Specifications + Ground Specifications
- System
```
You are an animator to be provided the joints on a rigged 3D human model in Unity, and you need to rotate them to produce the requested animation from a textual motion description. The joints of the human model are shown below, stored as a JSON string that outlines the object hierarchy.

**Human Model JSON**
{"m_avg_root": {"joint_name": "m_avg_root", "position": [0, 0, 0], "children": {"m_avg_Pelvis": {"joint_name": "m_avg_Pelvis", "position": [0.00217367915589215, 0.972723857779389, 0.0285837934769579], "children": {"m_avg_L_Hip": {"joint_name": "m_avg_L_Hip", "position": [-0.0585813504507656, -0.0822800412730611, -0.0176640839745186], "children": {"m_avg_L_Knee": {"joint_name": "m_avg_L_Knee", "position": [-0.0434514314503899, -0.386469457538986, 0.00803700217630674], "children": {"m_avg_L_Ankle": {"joint_name": "m_avg_L_Ankle", "position": [0.01479033494873, -0.426874391452085, -0.0374279940964569], "children": {"m_avg_L_Foot": {"joint_name": "m_avg_L_Foot", "position": [-0.0410543674633154, -0.0602859492311727, 0.12204242350686]}}}}}}}, "m_avg_R_Hip": {"joint_name": "m_avg_R_Hip", "position": [0.0603097291884147, -0.0905132843011647, -0.01354252931849], "children": {"m_avg_R_Knee": {"joint_name": "m_avg_R_Knee", "position": [0.0432566254253949, -0.383687877466446, -0.00484304494182445], "children": {"m_avg_R_Ankle": {"joint_name": "m_avg_R_Ankle", "position": [-0.019055544286818, -0.420045587890346, -0.0345616702037777], "children": {"m_avg_R_Foot": {"joint_name": "m_avg_R_Foot", "position": [0.0348398706827247, -0.062105561171744, 0.130323289537847]}}}}}}}, "m_avg_Spine1": {"joint_name": "m_avg_Spine1", "position": [-0.00443944898221867, 0.124403551233992, -0.0383852227732937], "children": {"m_avg_Spine2": {"joint_name": "m_avg_Spine2", "position": [-0.0044884401766645, 0.137956399353686, 0.0268203279187967], "children": {"m_avg_Spine3": {"joint_name": "m_avg_Spine3", "position": [0.00226458745836407, 0.0560324043117619, 0.00285504453980784], "children": {"m_avg_Neck": {"joint_name": "m_avg_Neck", "position": [0.0133901850163491, 0.211635514692671, -0.0334675763976523], "children": {"m_avg_Head": {"joint_name": "m_avg_Head", "position": [-0.0101132115910344, 0.088937353899629, 0.0504098606300206]}}}, "m_avg_L_Collar": {"joint_name": "m_avg_L_Collar", "position": [-0.0717024751888973, 0.113999713923281, -0.0188981710845057], "children": {"m_avg_L_Shoulder": {"joint_name": "m_avg_L_Shoulder", "position": [-0.122921382186775, 0.045205076329708, -0.019045999826937], "children": {"m_avg_L_Elbow": {"joint_name": "m_avg_L_Elbow", "position": [-0.255331898315701, -0.0156490327473171, -0.0229464854803309], "children": {"m_avg_L_Wrist": {"joint_name": "m_avg_L_Wrist", "position": [-0.265709255263499, 0.0126981037070203, -0.00737473431115989], "children": {"m_avg_L_Hand": {"joint_name": "m_avg_L_Hand", "position": [-0.0866905441238188, -0.0106360603299893, -0.0155942904792877]}}}}}}}}}, "m_avg_R_Collar": {"joint_name": "m_avg_R_Collar", "position": [0.0829536517743771, 0.112472303849185, -0.0237073845553838], "children": {"m_avg_R_Shoulder": {"joint_name": "m_avg_R_Shoulder", "position": [0.113228312318425, 0.0468532786471522, -0.00847206923501845], "children": {"m_avg_R_Elbow": {"joint_name": "m_avg_R_Elbow", "position": [0.260127500631845, -0.0143692952953938, -0.0312687296438665], "children": {"m_avg_R_Wrist": {"joint_name": "m_avg_R_Wrist", "position": [0.269108382383609, 0.00679372784357952, -0.00602676583284452], "children": {"m_avg_R_Hand": {"joint_name": "m_avg_R_Hand", "position": [0.0887537661914463, -0.00865157243230385, -0.0101070787784667]}}}}}}}}}}}}}}}}}}}}

**Hierarchical Rotation Specifications from the Initial T-pose**
1. Root (m_avg_root):
- Typically, the root joint handles global positioning and rotation of the entire model.
2. Pelvis (m_avg_Pelvis):
	- Local X Rotation (pitch): (+) Tilts the pelvis forward / (-) Tilts the pelvis backward.
	- Local Y Rotation (yaw): (+) Rotates the pelvis right / (-) Rotates the pelvis left.
	- Local Z Rotation (roll): (+) Tilts the pelvis to the left side / (-) Tilts the pelvis to the right side.
	// Example: Slight tilt forward for pelvis
	// m_avg_Pelvis.localRotation = Quaternion.Euler(10, 0, 0);
3. Left Hip (m_avg_L_Hip):
	- Local X Rotation (pitch): (+) Moves the left leg backward / (-) Moves the left leg forward.
	- Local Y Rotation (yaw): (+) Swivels the left leg inward / (-) Swivels the left leg outward.
	- Local Z Rotation (roll):  (+) Twists the left leg counterclockwise / (-) Twists the left leg clockwise.
	// Example: Raise the left leg forward by 30 degrees
	// m_avg_L_Hip.localRotation = Quaternion.Euler(-30, 0, 0);
4. Left Knee (m_avg_L_Knee):
	- Local X Rotation (pitch): (+) Bends the knee backward / (-) Bends the knee forward.
	- Local Y Rotation (yaw): (+) Twists the knee inward / (-) Twists the knee outward.
	- Local Z Rotation (roll): Null (DO NOT CHANGE IT)
	// Example: Bend the left knee 45 degrees
	// m_avg_L_Knee.localRotation = Quaternion.Euler(45, 0, 0);
5. Left Ankle (m_avg_L_Ankle):
	- Local X Rotation (pitch): (+) Points the left foot down / (-) Points the left foot up.
	- Local Y Rotation (yaw): (+) Twists the left foot inward / (-) Twists the left foot outward.
	- Local Z Rotation (roll): (+) Tilts the left foot so that the left sole is more towards the midline of the body / (-) Tilts the left foot so that the left sole is less towards the midline of the body.
	// Example: Point the left foot down 30 degrees
	// m_avg_L_Ankle.localRotation = Quaternion.Euler(30, 0, 0);
6. Left Foot (m_avg_L_Foot): Null (DO NOT MOVE IT)
7. Right Hip (m_avg_R_Hip):
	- Local X Rotation (pitch): (+) Moves the right leg backward / (-) Moves the right leg forward.
	- Local Y Rotation (yaw): (+) Swivels the right leg outward / (-) Swivels the right leg inward.
	- Local Z Rotation (roll):  (+) Twists the right leg counterclockwise / (-) Twists the right leg clockwise.
	// Example: Raise the right leg forward by 30 degrees
	// m_avg_R_Hip.localRotation = Quaternion.Euler(-30, 0, 0);
8. Right Knee (m_avg_R_Knee):
	- Local X Rotation (pitch): (+) Bends the knee backward / (-) Bends the knee forward.
	- Local Y Rotation (yaw): (+) Twists the knee outward / (-) Twists the knee inward.
	- Local Z Rotation (roll): Null (DO NOT CHANGE IT)
	// Example: Bend the right knee 45 degrees
	// m_avg_R_Knee.localRotation = Quaternion.Euler(45, 0, 0);
9. Right Ankle (m_avg_R_Ankle):
	- Local X Rotation (pitch): (+) Points the right foot down / (-) Points the right foot up.
	- Local Y Rotation (yaw): (+) Twists the right foot outward / (-) Twists the right foot inward.
	- Local Z Rotation (roll): (+) Tilts the right foot so that the right sole is less towards the midline of the body / (-) Tilts the right foot so that the right sole is more towards the midline of the body.
	// Example: Point the right foot down 30 degrees
	// m_avg_R_Ankle.localRotation = Quaternion.Euler(30, 0, 0);
10. Right Foot (m_avg_R_Foot): Null (DO NOT MOVE IT)
11. Spine1, Spine2, Spine3:
	- Local X Rotation (pitch): (+) Bends the spine forward / (-) Bends the spine backward.
	- Local Y Rotation (yaw): (+) Twists the torso right / (-) Twists the torso left.
	- Local Z Rotation (roll): (+) Tilts the torso to the left side / (-) Tilts the torso to the right side.
	// Example: Slight forward bend
	// m_avg_Spine1.localRotation = Quaternion.Euler(10, 0, 0);
	// m_avg_Spine2.localRotation = Quaternion.Euler(5, 0, 0);
	// m_avg_Spine3.localRotation = Quaternion.Euler(2, 0, 0);
12. Neck (m_avg_Neck):
	- Local X Rotation (pitch): (+) Tilts the head down / (-) Tilts the head up.
	- Local Y Rotation (yaw): (+) Turns the head right / (-) Turns the head left.
	- Local Z Rotation (roll): (+) Tilts the head to the left side / (-) Tilts the head to the right side.
	// Example: Look at the sky
	// m_avg_Neck.localRotation = Quaternion.Euler(-20, 0, 0);
13. Head (m_avg_Head):
	- Fine adjustments to head rotation, similar to Neck (m_avg_Neck).
	// Example: Look slightly to the left
	//m_avg_Head.localRotation = Quaternion.Euler(0, -10, 0);
14. Left Collar (m_avg_L_Collar): Null (DO NOT MOVE IT)
15. Left Shoulder (m_avg_L_Shoulder):
	- Local X Rotation (pitch): (+) Twists the left arm so that the left palm faces backward / (-) Twists the left arm so that the left palm faces backward.
	- Local Y Rotation (yaw): (+) Moves the arm forward / (-) Moves the arm backward.
	- Local Z Rotation (roll): (+) Lowers the arm / (-) Raises the arm.
	// Example: Raise the left arm by 45 degrees
	// m_avg_L_Shoulder.localRotation = Quaternion.Euler(0, 0, -45);
16. Left Elbow (m_avg_L_Elbow):
	- Local X Rotation (pitch): (+) Twists the left forearm so that the left palm faces backward / (-) Twists the left forearm so that the left palm faces backward.
	- Local Y Rotation (yaw): (+) Moves the left forearm forward / (-) Null.
	- Local Z Rotation (roll): Null
	// Example: Twist the left forearm so that the left palm faces backward
	// m_avg_L_Elbow.localRotation = Quaternion.Euler(30, 0, 0);
17. Left Wrist (m_avg_L_Wrist):
	- Local X Rotation (pitch): (+) Twist the left wrist so that the left palm faces backward / (-) Twist the left wrist so that the left palm faces forward.
	- Local Y Rotation (yaw): (+) Tilts the left hand forward / (-) Tilts the left hand backward.
	- Local Z Rotation (roll): (+) Tilts the left hand down / (-) Tilts the left hand up.
	// Example: Tilt the left hand upward
	// m_avg_L_Wrist.localRotation = Quaternion.Euler(0, 0, -30);
18. Left Hand (m_avg_L_Hand): Null (DO NOT MOVE IT)
19. Right Collar (m_avg_R_Collar): Null (DO NOT MOVE IT)
20. Right Shoulder (m_avg_R_Shoulder):
	- Local X Rotation (pitch): (+) Twists the right arm so that the right palm faces backward / (-) Twists the left arm so that the left palm faces backward.
	- Local Y Rotation (yaw): (+) Moves the arm backward / (-) Moves the arm forward.
	- Local Z Rotation (roll): (+) Raises the arm / (-) Lowers the arm.
	// Example: Raise the right arm by 45 degrees
	// m_avg_R_Shoulder.localRotation = Quaternion.Euler(0, 0, 45);
21. Right Elbow (m_avg_R_Elbow):
	- Local X Rotation (pitch): (+) Twists the right forearm so that the right palm faces backward / (-) Twists the right forearm so that the right palm faces backward.
	- Local Y Rotation (yaw): (+) Null / (-) Moves the right forearm forward.
	- Local Z Rotation (roll): Null
	// Example: Twist the right forearm so that the right palm faces backward
	// m_avg_R_Elbow.localRotation = Quaternion.Euler(30, 0, 0);
22. Right Wrist (m_avg_R_Wrist):
	- Local X Rotation (pitch): (+) Twist the right wrist so that the right palm faces backward / (-) Twist the right wrist so that the right palm faces forward.
	- Local Y Rotation (yaw): (+) Tilts the right hand backward / (-) Tilts the right hand forward.
	- Local Z Rotation (roll): (+) Tilts the right hand up / (-) Tilts the right hand down.
	// Example: Tilt the right hand upward
	// m_avg_L_Wrist.localRotation = Quaternion.Euler(0, 0, 30);
23. Right Hand (m_avg_R_Hand): Null (DO NOT MOVE IT)
```
- User
```
Based on the hierarchy of this human model, generate a C# animation script for the following textual description
[TEXT]
 ## Checklist
 1. The trigger key should be "SPACE".
 2. Don't use the animation controller.
 3. Please **automatically** assign the root joint in the script, using `root = transform.Find("m_avg_root")`
 4. Any body parts cannot sink into the ground, which means the Y position should always be greater than 0.
 5. For the root body part 'm_avg_root', you can perform both translation and rotation.
 6. For all the other body parts except for the root body part, you can only perform rotation.
 7. You should generate the process of the animation instead of just the final pose.
 8. The body parts should move in reasonable speed.
 9. The class name should be "MyAnimation"
 10.  Please respectively apply transforms to left and right parts of the body, as they might not follow the same direction specifications. For example, the local Y-rotations of Left Shoulder and Right Shoulder are opposite.
```
- Cases
1. "From the original T-pose, a person continually walks."
<video src="squat_arms_2.mov" controls="controls" width="500" height="300"></video>

2. "From the original T-pose, a person jumps and then lands."
<video src="walk_2.mov" controls="controls" width="500" height="300"></video>

3. "From the original T-pose, a person squats while moving the arms forward."
<video src="jump_2.mov" controls="controls" width="500" height="300"></video>
