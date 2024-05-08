## Model: gpt-4-turbo-2024-04-09

### Pure textual instructions

#### Naive instruction 
- System: `Decompose this high-level motion instruction down to atomic descriptions.`
- User: `A man raises both hands above the head.`
- Outputs:
    ```
    1. The man begins in a neutral standing position with both arms at his sides.
    2. He bends both elbows slightly to prepare for the upward movement.
    3. Simultaneously, he begins to lift both arms laterally away from his body.
    4. As his arms rise, he keeps his elbows mostly extended but not locked, palms facing each other.
    5. He continues lifting his arms upward until they are fully extended and aligned vertically with his body.
    6. His hands reach above his head, and the palms may face slightly forward or towards each other.
    7. The final position has both arms straight and hands above the head.
    ```

#### Naive recursive prompting
- System:
    ```
    Decompose this high-level motion instruction down to a structured combination of atomic descriptions.
    An atomic description specifies the movement of a certain body part in a certain time interval.
    ```
- User: `A man raises both hands above the head.`
- Assistant:
    ```
    To decompose the high-level instruction "A man raises both hands above the head" into structured, atomic descriptions, we need to specify each essential movement in terms of individual body parts (in this case, the hands and arms), along with respective time intervals. We’ll assume a simplified time interval for demonstration.

    1. **Initial Position:**
    - **Time: T0 to T1 **
    - **Description:** Man starts with both arms at his sides.

    2. **Lower Arm Movement:**
    - **Time: T1 to T2**
    - **Description:** Man bends elbows, moving forearms from a vertical position beside the body to a horizontal position in front of the chest.

    3. **Upper Arm Movement:**
    - **Time: T2 to T3**
    - **Description:** Keeping elbows bent, man lifts upper arms from hanging down at his sides to a position where they are level with his shoulders.

    4. **Full Arm Extension:**
    - **Time: T3 to T4**
    - **Description:** Man straightens elbows and extends both arms fully vertically above his head.

    These atomic descriptions cover the detailed movements involved in the action of raising both hands above the head, with each crucial step broken down into specific movements and associated time intervals.
    ```
- User: `Recursively decompose each of the descriptions above which you think is not atomic enough.`
- Assistant:
    ```
    To recursively decompose the above descriptions further into more atomic procedures, let's specify each key action involved in the smaller movements of each limb segment:

    1. **Initial Position:**
    - **Time: T0 to T1**
    - **Description:**
        - Arms straight, relaxed, and hanging by the sides of the body.
        - Palms facing the body.
        - Shoulders in a neutral, relaxed position.

    2. **Lower Arm Movement:**
    - **Time: T1 to T2**
    - **Description:**
        - **Elbow Joint Movement:**
        - **Time: T1 to T1.5**
        - **Description:** Initiate movement by flexing the elbow joints, reducing the angle between the forearms and upper arms.
        - **Forearm Positioning:**
        - **Time: T1.5 to T2**
        - **Description:** Continue flexing the elbows until the forearms are parallel to the ground, hands in front of the chest, palms facing upwards.

    3. **Upper Arm Movement:**
    - **Time: T2 to T3**
    - **Description:**
        - **Shoulder Joint Rotation:**
        - **Time: T2 to T2.5**
        - **Description:** Rotate the shoulder joints to lift the relaxed, bent arms, moving the upper arms to a position where they are horizontal and even with shoulders.
        - **Upper Arm Alignment:**
        - **Time: T2.5 to T3**
        - **Description:** Adjust the upper arms, ensuring they are aligned straight out from the shoulders, elbows bent at about 90-degrees, forearms pointing upwards.

    4. **Full Arm Extension:**
    - **Time: T3 to T4**
    - **Description:**
        - **Elbow Joint Extension:**
        - **Time: T3 to T3.5**
        - **Description:** Begin to extend the elbows, straightening the arms upward.
        - **Hand Positioning:**
        - **Time: T3.5 to T4**
        - **Description:** Fully extend the elbows until the arms are completely straight above the head, palms facing each other.

    Each of these further decomposed descriptions targets the individual joints and how they move throughout the process, avoiding the combination of multiple joints or complex actions within a single atomic instruction. This allows for a precise specification suitable for programming or detailed biomechanical analysis.
    ```
- User: `Refine the final atomic descriptions into a tabular representation. This representation should at least specify two dimensions - the time scale and body part scale`
- Assistant:
    ```
    Here's a refined tabular representation of all atomic motions breaking down the instruction "A man raises both hands above the head," specifying the time scale and body part scale for clarity and detail:
    ```
    | Time Interval | Body Part       | Movement Description                                 |
    |---------------|-----------------|------------------------------------------------------|
    | T0 to T1      | Entire Body     | Body in a relaxed standing position, arms by sides.  |
    |               | Palms           | Facing the body.                                     |
    |               | Shoulders       | In a relaxed, neutral position.                      |
    | T1 to T1.5    | Elbows          | Begin flexing at the joints.                         |
    | T1.5 to T2    | Forearms        | Continue flexing elbows until forearms are parallel to the ground, palms facing upwards. |
    | T2 to T2.5    | Shoulders       | Rotate joints to lift arms to shoulder level.        |
    | T2.5 to T3    | Upper Arms      | Align straight out from shoulders, elbows at 90-degrees, forearms vertical. |
    | T3 to T3.5    | Elbows          | Begin extending joints, moving arms upward.          |
    | T3.5 to T4    | Arms (Full Extension) | Extend elbows fully until arms are straight above the head. |
    |               | Hands           | Palms facing each other above the head.              |
    ```
    This table focuses on specific body parts (like elbows, forearms, shoulders, and hands) and details their movements over prespecified time intervals, enhancing clarity and specificity for each phase of the motion. This format is helpful for precise movement assessments, biomechanical studies, or programming humanoid robots.
    ```

#### Naive recursive prompting with programmatic input requirements
- System:
    ```
    Decompose this high-level motion instruction down to a structured combination of atomic descriptions that can potentially serve as programmatic inputs into a computer graphics engine without substantive modification.
    An atomic description specifies the movement of a certain body part in a certain time interval.
    ```
- User: `A man raises both hands above the head.`
- Assistant:
    ```
    1. **Right Arm Movement**:
    - **Initial Position**: Right arm hangs down at the side of the body.
    - **Final Position**: Right arm is raised such that the right hand is above the head.
    - **Movement Duration**: Assumes a total time from initial to final position of approximately 2 seconds.
    - **Description**:
        - Time 0s: Right arm begins movement from side.
        - Time 2s: Right hand is positioned above the head.

    2. **Left Arm Movement**:
    - **Initial Position**: Left arm hangs down at the side of the body.
    - **Final Position**: Left arm is raised such that the left hand is above the head.
    - **Movement Duration**: Assumes a total time from initial to final position of approximately 2 seconds.
    - **Description**:
        - Time 0s: Left arm begins movement from side.
        - Time 2s: Left hand is positioned above the head.

    3. **Body Posture**:
    - **Posture**: The torso remains upright throughout the movement.
    - **Movement**: Minimal to none.
        
    These atomic descriptions lay out the sequential movements for a computer graphics engine to simulate a man raising both hands above his head. Each action specifies starting and ending positions, the timeframe as well as motion direction for clarity in animation programming.
    ```
- User: `Recursively decompose each of the descriptions above which you think is not atomic enough.`
- Assistant:
    ```
    To make each description even more atomic, especially helpful for precise animation tasks in a graphics engine, let's break down the movement of each arm into sub-components, focusing specifically on the shoulder, elbow, and wrist joints, and further clarifying the orientations and rotations required at each step.

    ### Right Arm Movement
    1. **Right Shoulder Joint Movement**:
    - **Initial Position**: Right arm at the side, shoulder in a neutral position.
    - **Final Position**: Right shoulder abducted, lifting the arm laterally to about 180 degrees vertical.
    - **Movement Duration**: 1 second.
    - **Description**:
        - Time 0s: Right shoulder starts from a natural hanging position.
        - Time 1s: Right shoulder moves to a fully abducted position to raise the arm vertically upwards.
    
    2. **Right Elbow Joint Movement**:
    - **Initial Position**: Right elbow fully extended (straight).
    - **Final Position**: Right elbow remains extended.
    - **Movement Duration**: Runs concurrently with shoulder movement, 1 second.
    - **Description**:
        - Time 0s: Right elbow starts in a fully extended position.
        - Time 1s: Right elbow maintains extension throughout the arm lift.

    3. **Right Wrist Joint Movement**:
    - **Initial Position**: Wrist in a neutral, straight position aligned with the arm.
    - **Final Position**: Wrist remains neutral, aligned with the raised arm.
    - **Movement Duration**: 1 second.
    - **Description**:
        - Time 0s: Right wrist starts in a neutral position.
        - Time 1s: Right wrist maintains a neutral position as the arm is raised.

    ### Left Arm Movement
    1. **Left Shoulder Joint Movement**:
    - **Initial Position**: Left arm at the side, shoulder in a neutral position.
    - **Final Position**: Left shoulder abducted, lifting the arm laterally to about 180 degrees vertical.
    - **Movement Duration**: 1 second.
    - **Description**:
        - Time 0s: Left shoulder starts from a natural hanging position.
        - Time 1s: Left shoulder moves to a fully abducted position to raise the arm vertically upwards.
    
    2. **Left Elbow Joint Movement**:
    - **Initial Position**: Left elbow fully extended (straight).
    - **Final Position**: Left elbow remains extended.
    - **Movement Duration**: Runs concurrently with shoulder movement, 1 second.
    - **Description**:
        - Time 0s: Left elbow starts in a fully extended position.
        - Time 1s: Left elbow maintains extension throughout the arm lift.

    3. **Left Wrist Joint Movement**:
    - **Initial Position**: Wrist in a neutral, straight position aligned with the arm.
    - **Final Position**: Wrist remains neutral, aligned with the raised arm.
    - **Movement Duration**: 1 second.
    - **Description**:
        - Time 0s: Left wrist starts in a neutral position.
        - Time 1s: Left wrist maintains a neutral position as the arm is raised.

    ### Body Posture (Further Detail Not Typically Necessary)
    - **Torso and Spine Posture**:
    - **Position**: Remains constant as upright.
    - **Movement**: None, maintaining stability for the lifting of arms.

    By specifying joint-specific movements and timelines, these descriptions become extremely detailed and atomic, offering direct inputs for rigging and animating in a 3D modeling software or a computer graphics engine, ensuring that each part moves in perfect synchronization and with anatomical correctness.
    ```
- User: `Refine the final atomic descriptions into a tabular representation. This representation should at least specify two dimensions - the time scale and body part scale`
- Assistant:
    ```
    Below is a refined tabular representation of the atomic descriptions for the body parts and respective movements, specified along two axes: time scale and body part. This table helps in visualizing the synchronization and specific timeline for each joint movement required to animate a man raising both hands above his head.
    ```
    | Time (s) | Body Part         | Initial Position              | Final Position                   | Movement Description                                 |
    |----------|-------------------|-------------------------------|----------------------------------|------------------------------------------------------|
    | 0s       | Right Shoulder    | Arm at side, shoulder neutral | Shoulder abducted to 180 degrees | Shoulder moves from neutral to fully abducted upward |
    | 1s       | Right Shoulder    | -                             | -                                | Shoulder reaches full abduction                     |
    | 0s-1s    | Right Elbow       | Elbow fully extended          | Elbow remains extended           | Elbow remains extended as arm raises                |
    | 0s-1s    | Right Wrist       | Wrist neutral, straight       | Wrist remains neutral, straight  | Wrist maintains neutral alignment with raised arm   |
    | 0s       | Left Shoulder     | Arm at side, shoulder neutral | Shoulder abducted to 180 degrees | Shoulder moves from neutral to fully abducted upward |
    | 1s       | Left Shoulder     | -                             | -                                | Shoulder reaches full abduction                     |
    | 0s-1s    | Left Elbow        | Elbow fully extended          | Elbow remains extended           | Elbow remains extended as arm raises                |
    | 0s-1s    | Left Wrist        | Wrist neutral, straight       | Wrist remains neutral, straight  | Wrist maintains neutral alignment with raised arm   |
    | Throughout | Torso & Spine   | Upright, stable               | Remains upright and stable       | Maintains posture to support arm movement           |
    ```
    This table provides clear and sequential details for animators, ensuring that each component of the motion is accounted for and happens at the precise time, perfect for detailed and accurate computer graphics animations. It simplifies tracking the progression of each part of the movement within a defined time frame.
    ```

#### Step-by-step recursive prompting
##### Simple motion 1
- System:
    ```
    Decompose this high-level motion instruction down to a structured combination of atomic descriptions that can potentially serve as programmatic inputs into a computer graphics engine without substantive modification.
    An atomic description specifies the movement of a certain body part in a certain time interval.
    ```
- User: `A man raises both hands above the head.`
- Assistant:
    ```
    1. **Set Initial Position**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Man starts in a neutral position.
    - **Body Part(s)**: Whole body
    - **Motion**: None, body is static

    2. **Movement of Arms**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Both arms move from resting along the sides of the body to above the head.
    - **Body Part(s)**: Left Arm, Right Arm
    - **Motion**: Arms lift laterally (away from the body, elbows straight), continue to move until the hands are above the head, palms facing forward or toward each other.

    3. **End Position**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The arms finish moving and remain stationary above the head.
    - **Body Part(s)**: Left Arm, Right Arm
    - **Motion**: Arms are stationary, held straight above the head.

    Each of these steps details the specific body parts involved, the nature of their movement, and the timing of these movements to enact the instructions of raising both hands above
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    The description that is not atomic enough is the second point:

    **Movement of Arms**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Both arms move from resting along the sides of the body to above the head.
    - **Body Part(s)**: Left Arm, Right Arm
    - **Motion**: Arms lift laterally (away from the body, elbows straight), continue to move until the hands are above the head, palms facing forward or toward each other.

    This description covers the movement of two arms simultaneously, but for a more atomic approach, each arm's movement should be specified separately, even if they perform the same action simultaneously. This ensures that each motion can be individually adjusted or controlled if needed. Here's how you could break it down more atomically:

    **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from resting along the side of the body to above the head.
    - **Body Part**: Left Arm
    - **Motion**: Lifts laterally (away from the body, elbow straight), continuing to move until the hand is above the head, palm facing forward or toward the right hand.

    **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from resting along the side of the body to above the head.
    - **Body Part**: Right Arm
    - **Motion**: Lifts laterally (away from the body, elbow straight), continuing to move until the hand is above the head, palm facing forward or toward the left hand.

    This breakdown makes each atomic description more specific to an individual body part's movement, which is essential for granular control in animation or simulation in computer graphics.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Here are the atomic descriptions, revised to be more granular for each body part and action:

    1. **Set Initial Position for Whole Body**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Man starts in a neutral position.
    - **Body Part(s)**: Whole body
    - **Motion**: None, body is static

    2. **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from resting along the side of the body to above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues to move until the hand is above the head, palm facing forward or toward the right hand.

    3. **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from resting along the side of the body to above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues to move until the hand is above the head, palm facing forward or toward the left hand.

    4. **End Position for Left Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The left arm finishes moving and remains stationary above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm is stationary, held straight above the head.

    5. **End Position for Right Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The right arm finishes moving and remains stationary above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm is stationary, held straight above the head.

    These descriptions keep the details specific and isolated to individual body parts, enhancing precision and control for animation programming or computer graphics simulations.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    The description that is not atomic enough in the list provided is:

    1. **Set Initial Position for Whole Body**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Man starts in a neutral position.
    - **Body Part(s)**: Whole body
    - **Motion**: None, body is static

    This description lists "Whole body" as the body part, which covers multiple components (arms, legs, head, torso, etc.). For an atomic description, specific positioning or status of each major body part or section should be described separately if they could potentially require independent control or exhibit different states even when starting in a general 'neutral' pose. This is essential in more sophisticated graphic applications where fine control over each body part is necessary, such as in detailed character animations.

    Here’s how you could break it down more atomically:

    - **Initial Position of Torso**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Torso is upright in a relaxed posture.
    - **Body Part**: Torso
    - **Motion**: None, torso remains static.

    - **Initial Position of Left Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left arm is hanging relaxed at the side.
    - **Body Part**: Left Arm
    - **Motion**: None, left arm remains static.

    - **Initial Position of Right Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right arm is hanging relaxed at the side.
    - **Body Part**: Right Arm
    - **Motion**: None, right arm remains static.

    - **Initial Position of Legs**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Legs are straight with a slight gap between them, standing position.
    - **Body Part**: Legs
    - **Motion**: None, legs remain static.

    This adjustment makes each description more specific to an individual body part's initial state, providing granular control right from the start.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Here are the atomically refined descriptions for the initialization, movement, and end position of each major body part:

    1. **Initial Position of Torso**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Torso is upright in a relaxed posture.
    - **Body Part**: Torso
    - **Motion**: None, torso remains static.

    2. **Initial Position of Left Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left arm hangs relaxed at the side.
    - **Body Part**: Left Arm
    - **Motion**: None, left arm remains static.

    3. **Initial Position of Right Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right arm hangs relaxed at the side.
    - **Body Part**: Right Arm
    - **Motion**: None, right arm remains static.

    4. **Initial Position of Legs**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Legs are straight with a slight gap between them, in a standing position.
    - **Body Part**: Legs
    - **Motion**: None, legs remain static.

    5. **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from hanging by the side to above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues moving until the hand is above the head, palm facing forward or towards the right hand.

    6. **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from hanging by the side to above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues moving until the hand is above the head, palm facing forward or towards the left hand.

    7. **End Position for Left Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The left arm finishes moving and remains stationary above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm is stationary, held straight above the head.

    8. **End Position for Right Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The right arm finishes moving and remains stationary above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm is stationary, held straight above the head.

    These atomic descriptions ensure that the actions and statuses of specific body parts are completely independent and detailed, essential for accurate and nuanced animation and simulation techniques in computer graphics.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon reviewing the atomic descriptions provided, all are quite specific and focus on individual body parts; however, the descriptions of the initial positions could potentially be considered not atomic enough if precision in every aspect is crucial. For example:

    **Initial Position of Legs**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Legs are straight with a slight gap between them, in a standing position.
    - **Body Part**: Legs
    - **Motion**: None, legs remain static.

    This description involves both legs as a single unit. In cases where absolute atomic specificity is needed (for example, in detailed animation or physiotherapy simulations), it might be necessary to describe the position of each leg separately, even if they start in nearly identical conditions. This would allow for individual leg movements to be defined independently in subsequent actions, which could be essential in scenarios involving asymmetrical leg movements.

    Here is how you could break it down more atomically:

    1. **Initial Position of Left Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left leg is straight, slightly apart from the right leg, weight evenly distributed, in a standing position.
    - **Body Part**: Left Leg
    - **Motion**: None, left leg remains static.

    2. **Initial Position of Right Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right leg is straight, slightly apart from the left leg, weight evenly distributed, in a standing position.
    - **Body Part**: Right Leg
    - **Motion**: None, right leg remains static.

    These modifications make each leg's position explicitly clear and independent, offering more control for animations or simulations that might later involve only one leg.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Let's write out the fully atomic descriptions, including modifications for individual legs separated:

    1. **Initial Position of Torso**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Torso is upright in a relaxed posture.
    - **Body Part**: Torso
    - **Motion**: None, torso remains static.

    2. **Initial Position of Left Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left arm hangs relaxed at the side.
    - **Body Part**: Left Arm
    - **Motion**: None, left arm remains static.

    3. **Initial Position of Right Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right arm hangs relaxed at the side.
    - **Body Part**: Right Arm
    - **Motion**: None, right arm remains static.

    4. **Initial Position of Left Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left leg is straight, slightly apart from the right leg, weight evenly distributed, in a standing position.
    - **Body Part**: Left Leg
    - **Motion**: None, left leg remains static.

    5. **Initial Position of Right Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right leg is straight, slightly apart from the left leg, weight evenly distributed, in a standing position.
    - **Body Part**: Right Leg
    - **Motion**: None, right leg remains static.

    6. **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from hanging by the side to above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues moving until the hand is above the head, palm facing forward or towards the right hand.

    7. **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from hanging by the side to above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues moving until the hand is above the head, palm facing forward or towards the left hand.

    8. **End Position for Left Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The left arm finishes moving and remains stationary above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm is stationary, held straight above the head.

    9. **End Position for Right Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The right arm finishes moving and remains stationary above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm is stationary, held straight above the head.

    With this breakdown, every major body part's initial position, movement, and end position are defined individually, greatly enhancing precision and control for programming or animation purposes.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon further inspection, each description given in the last message is quite atomic, as each isolates individual limb movements and static positions. All body parts, including each arm and leg, are treated independently with specific actions described for their movement from the initial to the final state.

    However, if we had to suggest an improvement for even greater atomicity or specificity, it could be in the detailing of the hand orientation and exact elbow articulation during the arm movements:

    6. **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from hanging by the side to above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues moving until the hand is above the head, palm facing forward or towards the right hand.
    - **Potential Improvement**: Specify elbow angle changes if not completely straight, and more precise hand orientation.

    7. **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from hanging by the side to above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm lifts laterally (away from the body, elbow straight), continues moving until the hand is above the head, palm facing forward or towards the left hand.
    - **Potential Improvement**: Define specific angle changes in the elbow and detailed description of the hand orientation through the motion.

    These improvements could provide details that might be relevant in animation for showing muscle flexion or other detailed movements that are critical for high fidelity animations, like in character animations for films or video games where such nuances could improve realism.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Here are the refined atomic descriptions for the movement of the man, highlighting further details on the elbow and hand orientations where advisable for enhanced specificity:

    1. **Initial Position of Torso**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Torso is upright in a relaxed posture.
    - **Body Part**: Torso
    - **Motion**: None, torso remains static.

    2. **Initial Position of Left Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left arm hangs relaxed at the side.
    - **Body Part**: Left Arm
    - **Motion**: None, left arm remains static.

    3. **Initial Position of Right Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right arm hangs relaxed at the side.
    - **Body Part**: Right Arm
    - **Motion**: None, right arm remains static.

    4. **Initial Position of Left Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left leg is straight, slightly apart from the right leg, weight evenly distributed, in a standing position.
    - **Body Part**: Left Leg
    - **Motion**: None, left leg remains static.

    5. **Initial Position of Right Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right leg is straight, slightly apart from the left leg, weight evenly distributed, in a standing position.
    - **Body Part**: Right Leg
    - **Motion**: None, right leg remains static.

    6. **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from hanging by the side to above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm lifts laterally (away from the body, initially with elbow slightly bent and gradually straightening). At the end of the motion, the hand is above the head, palm facing inward towards the right hand.

    7. **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from hanging by the side to above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm lifts laterally (away from the body, initially with elbow slightly bent and gradually straightening). At the end of the motion, the hand is above the head, palm facing inward towards the left hand.

    8. **End Position for Left Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The left arm finishes moving and remains stationary above the head.
    - **Body Part**: Left Arm
    - **Motion**: Arm is stationary, held straight above the head.

    9. **End Position for Right Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The right arm finishes moving and remains stationary above the head.
    - **Body Part**: Right Arm
    - **Motion**: Arm is stationary, held straight above the head.

    These descriptions aim to capture the nuances of each body part's motion, including elbow and hand specifics, providing more detailed instruction for high-fidelity animations.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    All the descriptions provided in the revised list contain a high level of atomic detail, focusing on individual body parts and specifying their movements in a precise manner. Each body part's motion is described separately, including the nuances of limb orientation and motion dynamics, enhancing the atomicity needed for exacting animation or simulation tasks.

    However, if further precision was ever necessary, additional details could potentially be added regarding wrist movements or the specific angle measurements for elbow and knee joints during movements but from the descriptions provided:

    - **Movement of Left Arm** and **Movement of Right Arm** could potentially benefit from specifying the exact degree of elbow bending and increasing detail about wrist orientation (e.g., flexing or rotation) if required for even more detailed animation needs.

    Additionally, you might specify:
    - Head position and orientation during the movement since head pose can provide emotional cues or balance information.
    - Detailing the torso movement, if any, to account for balance adjustment as the arms raise, which often involves slight counter-movements.

    It seems these suggestions venture beyond the given scenarios, as the provided descriptions are adequately atomic for common practice in animation and motion capture applications. Continuously breaking down actions could go into subatomic levels such as muscle contractions or skin deformation, usually not necessary unless for highly specialized medical or biomechanical simulations.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    To focus on further atomic details, I will include additional specificity where possible, particularly about joint angles, and also consider the head and torso movements which might subtly accompany the arm movements. Here are the descriptions with these considerations:

    1. **Initial Position of Torso**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Torso is upright in a relaxed posture, shoulders relaxed.
    - **Body Part**: Torso
    - **Motion**: None, torso remains static.

    2. **Initial Position of Head**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Head is facing forward with eyes looking straight ahead, neck aligned with the spine.
    - **Body Part**: Head
    - **Motion**: None, head remains static.

    3. **Initial Position of Left Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left arm hangs relaxed at the side with a slight natural bend at the elbow.
    - **Body Part**: Left Arm
    - **Motion**: None, left arm remains static.

    4. **Initial Position of Right Arm**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right arm hangs relaxed at the side with a slight natural bend at the elbow.
    - **Body Part**: Right Arm
    - **Motion**: None, right arm remains static.

    5. **Initial Position of Left Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Left leg is straight, slightly apart from the right leg, weight evenly distributed, in a standing position.
    - **Body Part**: Left Leg
    - **Motion**: None, left leg remains static.

    6. **Initial Position of Right Leg**:
    - **Time Interval**: 0s to 0.1s
    - **Description**: Right leg is straight, slightly apart from the left leg, weight evenly distributed, in a standing position.
    - **Body Part**: Right Leg
    - **Motion**: None, right leg remains static.

    7. **Movement of Left Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Left arm moves from hanging by the side to above the head. Elbow straightens as the arm is raised.
    - **Body Part**: Left Arm
    - **Motion**: Arm lifts laterally with elbow starting from slight bend to fully extended, palm rotates inward as it reaches above the head.

    8. **Movement of Right Arm**:
    - **Time Interval**: 0.1s to 1.5s
    - **Description**: Right arm moves from hanging by the side to above the head. Elbow straightens as the arm is raised.
    - **Body Part**: Right Arm
    - **Motion**: Arm lifts laterally with elbow starting from slight bend to fully extended, palm rotates inward as it reaches above the head.

    9. **End Position for Left Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The left arm finishes moving and remains stationary above the head. Elbow is straight.
    - **Body Part**: Left Arm
    - **Motion**: Arm is stationary, held straight above the head with palm facing toward the right hand.

    10. **End Position for Right Arm**:
    - **Time Interval**: 1.5s to 2s
    - **Description**: The right arm finishes moving and remains stationary above the head. Elbow is straight.
    - **Body Part**: Right Arm
    - **Motion**: Arm is stationary, held straight above the head with palm facing toward the left hand.

    This detailed break-down now includes additional elements such as the initial and final orientations of the palms, specific mentions of elbow extensions, and the inclusion of head position, enhancing the atomicity for each description.
    ```
- User: `Refine the final atomic descriptions into a tabular representation. This representation should at least specify two dimensions - the time scale and body part scale`
- Assistant:
    ```
    Here's how the refined atomic descriptions can be structured into a tabular representation, organizing the information along two dimensions: the time scale and the body part scale. This format provides a clear and concise view of the actions over time for each individual body part, enhancing readability and reference.
    ```
    | Time Interval | Body Part | Description                                           | Motion Detail                                            |
    |---------------|-----------|-------------------------------------------------------|----------------------------------------------------------|
    | 0s to 0.1s    | Torso     | Torso is upright in a relaxed posture, shoulders relaxed. | None, torso remains static.                              |
    | 0s to 0.1s    | Head      | Head is facing forward with eyes looking straight ahead, neck aligned with the spine. | None, head remains static.                               |
    | 0s to 0.1s    | Left Arm  | Left arm hangs relaxed at the side with a slight natural bend at the elbow.   | None, left arm remains static.                           |
    | 0s to 0.1s    | Right Arm | Right arm hangs relaxed at the side with a slight natural bend at the elbow. | None, right arm remains static.                          |
    | 0s to 0.1s    | Left Leg  | Left leg is straight, slightly apart from the right leg, weight evenly distributed, in a standing position. | None, left leg remains static.                           |
    | 0s to 0.1s    | Right Leg | Right leg is straight, slightly apart from the left leg, weight evenly distributed, in a standing position. | None, right leg remains static.                          |
    | 0.1s to 1.5s  | Left Arm  | Left arm moves from hanging by the side to above the head. Elbow straightens as the arm is raised. | Arm lifts laterally with elbow starting from a slight bend to fully extended, palm rotates inward as it reaches above the head.  |
    | 0.1s to 1.5s  | Right Arm | Right arm moves from hanging by the side to above the head. Elbow straightens as the arm is raised. | Arm lifts laterally with elbow starting from a slight bend to fully extended, palm rotates inward as it reaches above the head.  |
    | 1.5s to 2s    | Left Arm  | The left arm finishes moving and remains stationary above the head. Elbow is straight. | Arm is stationary, held straight above the head with palm facing toward the right hand. |
    | 1.5s to 2s    | Right Arm | The right arm finishes moving and remains stationary above the head. Elbow is straight. | Arm is stationary, held straight above the head with palm facing toward the left hand.  |
    ```
    This table effectively distinguishes between the states and motions of each body part at specific time intervals. It could be used as a direct reference in various applications such as character rigging or animation programming in computer graphics software, ensuring each aspect of the motion is accounted for accurately.
    ```
##### Simple motion 2
- System:
    ```
    Decompose this high-level motion instruction down to a structured combination of atomic descriptions that can potentially serve as programmatic inputs into a computer graphics engine without substantive modification.
    An atomic description specifies the movement of a certain body part in a certain time interval.
    ```
- User: `A man slightly squats.`
- Assistant:
    ```
    Here are the atomic descriptions for the high-level motion of "A man slightly squats":

    1. **Time Interval 0-1 seconds**:
    - **Body Part: Hip** 
        - Action: Move downwards
    - **Body Part: Knees** 
        - Action: Bend slightly
    - **Body Part: Ankles** 
        - Action: Adjust to maintain balance

    2. **Time Interval 1-2 seconds**:
    - **Body Part: Hip** 
        - Action: Stabilize in a slightly lowered position
    - **Body Part: Knees** 
        - Action: Stay in a slightly bent position
    - **Body Part: Ankles** 
        - Action: Remain adjusted to maintain balance

    Each atomic description details a specific movement, which when combined, result in the action of a slight squat. These descriptions can be used in a computer graphics engine to animate the motion precisely.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    The description that is not atomic enough from the provided list is:

    - **Body Part: Ankles** 
    - Action: Adjust to maintain balance

    This description can be further broken down into more specific movements such as flexing or extending to a particular degree. To make it atomic, you would need to specify exactly how the ankle moves in each phase of the squat motion, such as:

    - **Time Interval 0-1 seconds**:
    - **Body Part: Ankles**
        - Action: Dorsiflexion (flex upwards slightly to accommodate the lowering of the body while keeping feet flat on the ground)

    This atomic modification specifies the exact type of movement required of the ankles, making it more suitable for precise animations in a graphics engine.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Certainly! Here are the revised atomic descriptions for the high-level motion of "A man slightly squats," with a more detailed breakdown for the ankle movement:

    1. **Time Interval 0-1 seconds**:
    - **Body Part: Hip**
        - Action: Move downwards by approximately 10-15 cm (depending on the height of the person)
    - **Body Part: Knees**
        - Action: Bend knees to approximately 30 degrees
    - **Body Part: Ankles**
        - Action: Dorsiflexion (flex upwards slightly to accommodate the lowering of the body while keeping the feet flat on the ground)

    2. **Time Interval 1-2 seconds**:
    - **Body Part: Hip**
        - Action: Stabilize in a slightly lowered position (maintain the 10-15 cm downward position)
    - **Body Part: Knees**
        - Action: Maintain in a slightly bent position (keep bent at approximately 30 degrees)
    - **Body Part: Ankles**
        - Action: Keep dorsiflexed (maintain slight upward flexion)

    These atomic descriptions give specific, quantifiable movements for each part of the body involved in the squat, making it suitable for direct implementation into a computer graphics simulation or animation engine.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon reviewing the descriptions provided, the one that still might not be atomic enough for direct implementation into a computer graphics engine is:

    - **Body Part: Hip**
    - Action: Move downwards by approximately 10-15 cm

    To make this description more atomic, it could further specify the exact path of movement (straight down, any lateral or forward/backward shift), speed of movement, and whether this movement is linear or if it decelerates or accelerates. Here's how to specify this in even more detail:

    - **Time Interval 0-1 seconds**:
    - **Body Part: Hip**
        - Action: Move straight downwards 12 cm, at a constant speed with no lateral shift

    This ensures that the description specifies the movement in terms that prevent ambiguity and are clear for programming precise animations in a graphics engine.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Certainly! Here's a revised and detailed breakdown of the atomic descriptions for each body part involved in the action "A man slightly squats," further detailing the hip movement to enhance precision:

    1. **Time Interval 0-1 seconds**:
    - **Body Part: Hip**
        - Action: Move straight downwards 12 cm at a constant speed, with no lateral shift.
    - **Body Part: Knees**
        - Action: Bend knees to precisely 30 degrees.
    - **Body Part: Ankles**
        - Action: Dorsiflexion - flex upwards slightly to accommodate the lowering of the body while keeping the feet flat on the ground.

    2. **Time Interval 1-2 seconds**:
    - **Body Part: Hip**
        - Action: Maintain the position 12 cm lower than the starting position without any movement.
    - **Body Part: Knees**
        - Action: Keep the knees bent at a constant 30 degrees.
    - **Body Part: Ankles**
        - Action: Maintain a slight upward flexion to keep the feet flat on the ground.

    These descriptions are designed to be straightforward inputs for a computer graphics engine, detailing specific and quantified movements over fixed time intervals. This allows for accurate and realistic animation of a slight squat motion.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    In the provided detailed descriptions, one area that might still not be fully atomic in terms of direct adaptability for programming in a computer graphics engine is:

    - **Body Part: Ankles**
    - Action: Dorsiflexion - flex upwards slightly to accommodate the lowering of the body while keeping the feet flat on the ground.

    To make this description truly atomic, you might want to specify the exact degree of upward flexion of the ankles and possibly detail the timing or change in angle. Here’s how you can detail it further:

    - **Time Interval 0-1 seconds**:
    - **Body Part: Ankles**
        - Action: Increase dorsiflexion by 5 degrees to accommodate the lowering of the body.

    This adjusted description quantifies the degree of dorsiflexion, ensuring a precise, reproducible movement in programming terms for a graphics engine.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Certainly! Here are the atomic descriptions for the motion "A man slightly squats," revised to include a specified degree of dorsiflexion for the ankles:

    1. **Time Interval 0-1 seconds**:
    - **Body Part: Hip**
        - Action: Move straight downwards 12 cm at a constant speed, with no lateral shift.
    - **Body Part: Knees**
        - Action: Bend knees to precisely 30 degrees.
    - **Body Part: Ankles**
        - Action: Increase dorsiflexion by 5 degrees to keep the feet flat on the ground while accommodating the lowering of the body.

    2. **Time Interval 1-2 seconds**:
    - **Body Part: Hip**
        - Action: Maintain the position 12 cm lower than the starting position without any movement.
    - **Body Part: Knees**
        - Action: Keep the knees bent at a constant 30 degrees.
    - **Body Part: Ankles**
        - Action: Maintain dorsiflexion increased by 5 degrees to keep the feet flat on the ground.

    These descriptions are now very specific, providing exact details on movement degrees, positional changes, and stability for each body part involved, designed for precise and realistic animation within a computer graphics engine.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon reviewing the most recent set of descriptions, they all appear to be sufficiently atomic for computer graphics animation purposes. Each body part's movement is specified with precise degrees, linear distances, or fixed positional values suitable for direct translation into programming code or animation keys in a 3D modeling software.

    All the specified descriptions cover movement detail in terms of distance (for the hip), degree (for the knees and ankles), and include instructions on maintaining those positions or states during the specified intervals. These are highly atomic, allowing for exact reproduction in a simulation or animation.

    If more exactness is needed for a certain application, additional details such as the exact speed profile (expressed in cm/sec or degrees/sec and its variation over time), or specifying ease-in and ease-out behaviors might be considered, but for most practical purposes in computer graphics, the current level of detail is adequate.

    Thus, each description currently provided is atomic enough for animation purposes:
    - The hip movement describes a precise linear distance.
    - The knee flexion specifies an exact angle.
    - The ankle dorsiflexion also quantifies the degree of movement.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon reviewing the descriptions again, each part of the squat motion (hip, knees, and ankles) is described with quantitative endpoints which should generally be sufficient for basic computer graphics animations. Each body part's movement specifies the extent and nature of the move, such as distance, angle, or degrees, which are pivotal for clear, realistic animation.

    Therefore, based on the level of detail specified:
    - Hip: precise vertical movement in cm.
    - Knees: specific angle to which they should bend.
    - Ankles: explicit increase in dorsiflexion measured in degrees.

    All these descriptions include enough atomic details for direct implementation into a computer graphics engine without the need for further breakdown. They address specific movements in clear, unambiguous terms necessary for creating believable character animations.

    Based on this, there are no further adjustments needed for atomicity within the provided scope. Each description sufficiently addresses the precision required for programming or animating a simple squat motion in typical graphics software.
    ```
- User: `Refine the final atomic descriptions into a tabular representation. This representation should at least specify two dimensions - the time scale and body part scale`
- Assistant:
    ```
    To refine the atomic descriptions of the motion "A man slightly squats" into a tabular representation, I will lay out each description across two primary dimensions: time scale and body part scale. This format helps in visualizing the specific movements mapped over the given time intervals for each body part, making it streamlined for programming or animation scripting.
    ```
    | Time Interval  | Body Part | Movement Description                           |
    |----------------|-----------|------------------------------------------------|
    | 0-1 seconds    | Hip       | Move straight downwards 12 cm at a constant speed, no lateral shift.  |
    | 0-1 seconds    | Knees     | Bend knees to exactly 30 degrees.              |
    | 0-1 seconds    | Ankles    | Increase dorsiflexion by 5 degrees to keep the feet flat on the ground. |
    | 1-2 seconds    | Hip       | Maintain position 12 cm lower than the starting position without any movement. |
    | 1-2 seconds    | Knees     | Maintain knees bent at 30 degrees.             |
    | 1-2 seconds    | Ankles    | Maintain dorsiflexion increased by 5 degrees.  |
    ```
    This table showcases each specific action taken by the different body parts in a structured timeframe. It provides an easily accessible format for developers, animators, or CGI technicians to accurately model the squat motion in various software or scripting environments. Such a structured presentation ensures precise and consistent execution of the movement in digital animations or simulations.
    ```
##### Complex motion 1
- System:
    ```
    Decompose this high-level motion instruction down to a structured combination of atomic descriptions that can potentially serve as programmatic inputs into a computer graphics engine without substantive modification.
    An atomic description specifies the movement of a certain body part in a certain time interval.
    ```
- User: `A person squats down then jumps.`
- Assistant:
    ```
    To decompose the action of a person squatting down and then jumping into atomic descriptions suitable for a computer graphics engine, we can break down the motion into a series of detailed steps focusing on key body parts: the legs (including hips, knees, and ankles), arms, and the torso. Here’s how it can be split:

    1. **Starting Position**:
    - Time Interval: t0 to t1
    - Description: The person starts standing upright. Legs are straight with feet shoulder-width apart. Arms are relaxed by the sides. Torso is erect.

    2. **Squatting Down (Preparation Phase)**:
    - Time Interval: t1 to t2
    - Legs: Begin by bending at the hips and knees to lower the body. Keep the back straight and slightly leaned forward, heels on the ground.
    - Arms: As the body lowers, extend arms forward parallel to the ground for balance.
    - Torso: Maintains an erect posture, leans slightly forward to maintain balance.

    3. **Bottom of Squat**:
    - Time Interval: t2 to t3
    - Legs: Knees are bent at approximately 90 degrees, thighs parallel to the ground, calves perpendicular to the ground. Heels remain in contact with the ground.
    - Arms: Fully extended forward, parallel with the ground.
    - Torso: Remains erect, leaned forward as needed for balance.

    4. **Launching the Jump (Initial Jump Phase)**:
    - Time Interval: t3 to t4
    - Legs: Explosively extend the knees and hips to push off the ground. Toes flex as the body prepares to leave the ground.
    - Arms: Pull arms back and then swing them upwards to gain additional momentum.
    - Torso: Straightens and aligns with legs to form a straight line at peak of jump.

    5. **Mid-Air Phase**:
    - Time Interval: t4 to t5
    - Legs: Slightly bent at knees and hips for a controlled posture mid-air.
    - Arms: Continue upward motion, reaching above the head.
    - Torso: Maintains straight alignment.

    6. **Landing Phase**:
    - Time Interval: t5 to t6
    - Legs: Begin to bend at knees and hips to absorb the impact as the feet contact the ground.
    - Arms: Swing downward to help stabilize and balance the body.
    - Torso: Keeps straight initially but may lean slightly forward upon impact to help maintain balance.

    7. **Return to Start Position**:
    - Time Interval: t6 to t7
    - Legs: Straighten to return to the original standing position.
    - Arms: Return to the relaxed position at the sides.
    - Torso: Returns to erect posture.

    Each of these atomic descriptions should be detailed with specific angles, velocities, and timings for a computer graphics engine to create a realistic and accurate depiction of a person squatting down and then jumping.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    The description in Step 4 — **Launching the Jump (Initial Jump Phase)** — is not quite atomic enough for precise input into a computer graphics engine. It covers multiple movements in a single time interval, which could be better split into more granular details, particularly focusing on the interaction of different body parts and their specific movements. Here’s how it can be refined:

    **Step 4: Launching the Jump (Initial Jump Phase)** can be divided into two distinct sub-steps to make the action more atomic:

    1. **Initial Leg Extension**:
    - Time Interval: t3 to t3.5
    - Legs: Rapid extension of the hips and knees begins, thrusting the body upward. 
    - Arms: Begin pulling back to aid in upward momentum.
    - Torso: Starts to straighten in preparation for leaving the ground.

    2. **Full Extension and Arm Swing**:
    - Time Interval: t3.5 to t4
    - Legs: Complete the extension of knees and hips; toes flex to push off the ground as the body lifts off.
    - Arms: Rapidly swing upwards, reaching above the head to maximize jump height.
    - Torso: Fully aligns with legs to form a straight vertical line at the peak of the jump.

    By detailing these sub-steps separately, we provide clearer instructions for each movement phase, allowing for more precise programming and visualization in a computer graphics context. This decomposition ensures that each body motion is captured distinctly, facilitating realistic animation where timing and coordination of movements are crucial.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Here are all the atomic descriptions rewritten and reorganized as requested, with the refinements applied to Step 4 for further detail:

    1. **Starting Position**:
    - Time Interval: t0 to t1
    - Legs: Straight, feet shoulder-width apart.
    - Arms: Relaxed by the sides.
    - Torso: Erect.

    2. **Squatting Down (Preparation Phase)**:
    - Time Interval: t1 to t2
    - Legs: Bend at the hips and knees to lower the body, heels on the ground.
    - Arms: Extend forward parallel to the ground for balance.
    - Torso: Maintains erect posture, leans slightly forward to maintain balance.

    3. **Bottom of Squat**:
    - Time Interval: t2 to t3
    - Legs: Knees bent at approximately 90 degrees, thighs parallel to the ground.
    - Arms: Fully extended forward, parallel with the ground.
    - Torso: Erect, leaned forward for balance.

    4. **Initial Leg Extension (Part of Launching the Jump)**:
    - Time Interval: t3 to t3.5
    - Legs: Begin rapid extension of knees and hips, starting to push body upward.
    - Arms: Start pulling back to aid in upward momentum.
    - Torso: Begins to straighten in preparation for liftoff.

    5. **Full Extension and Arm Swing (Part of Launching the Jump)**:
    - Time Interval: t3.5 to t4
    - Legs: Complete the extension of knees and hips; toes flex to push off the ground.
    - Arms: Rapidly swing upwards, reaching above the head.
    - Torso: Aligns with legs, forming a straight line vertically.

    6. **Mid-Air Phase**:
    - Time Interval: t4 to t5
    - Legs: Slightly bent at knees and hips.
    - Arms: Continue motion, reaching above the head.
    - Torso: Maintains straight alignment.

    7. **Landing Phase**:
    - Time Interval: t5 to t6
    - Legs: Begin to bend at knees and hips to absorb impact.
    - Arms: Swing downward to stabilize and balance.
    - Torso: Initially straight, may lean forward upon impact.

    8. **Return to Start Position**:
    - Time Interval: t6 to t7
    - Legs: Straighten to original standing position.
    - Arms: Return to relaxed position at sides.
    - Torso: Returns to erect posture.

    These detailed atomic steps specify each significant movement and transition, ideal for programming realistic animations in a computer graphics engine. Each description is focused on specific body parts and the corresponding action, ensuring clarity and allowing precise control over the animation sequence.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon reviewing the detailed steps, the description in **Step 6: Mid-Air Phase** could be considered not atomic enough compared to the others. This step generally describes a state of being ("mid-air") but does not delineate specific actions that different body parts should undertake during the several moments of being airborne. For maximal clarity and effectiveness in animation programming, it's useful to describe in more detail what each body part does during the ascent, peak, and beginning descent of the jump. Here's a more detailed breakdown:

    **6. Mid-Air Phase (Ascent):**
    - **Time Interval:** t4 to t4.5
    - **Legs:** Maintain slight bend at knees and hips to stabilize the body.
    - **Arms:** Reach maximum height above the head, then prepare to descend.
    - **Torso:** Aligns upright to stabilize posture during ascent.

    **7. Mid-Air Phase (Peak and Early Descent):**
    - **Time Interval:** t4.5 to t5
    - **Legs:** Start adjusting for landing by preparing to bend further at knees and hips.
    - **Arms:** Begin to lower from the highest point to regain balance and assist in landing.
    - **Torso:** Maintains upright posture, begins slight forward lean to prepare for landing impact.

    These additions provide specific instructions for what happens during the jump, ensuring each phase of the motion is captured and can be effectively animated.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Here are all the atomic descriptions rewritten and reorganized, with additional refinements applied to the Mid-Air Phase to provide clarity:

    1. **Starting Position**:
    - **Time Interval:** t0 to t1
    - **Legs:** Straight, feet shoulder-width apart.
    - **Arms:** Relaxed by the sides.
    - **Torso:** Erect.

    2. **Squatting Down (Preparation Phase)**:
    - **Time Interval:** t1 to t2
    - **Legs:** Bend at the hips and knees to lower the body, heels on the ground.
    - **Arms:** Extend forward parallel to the ground for balance.
    - **Torso:** Maintains erect posture, leans slightly forward to maintain balance.

    3. **Bottom of Squat**:
    - **Time Interval:** t2 to t3
    - **Legs:** Knees bent at approximately 90 degrees, thighs parallel to the ground.
    - **Arms:** Fully extended forward, parallel with the ground.
    - **Torso:** Erect, leaned forward for balance.

    4. **Initial Leg Extension (Part of Launching the Jump)**:
    - **Time Interval:** t3 to t3.5
    - **Legs:** Begin rapid extension of knees and hips, starting to push body upward.
    - **Arms:** Start pulling back to aid in upward momentum.
    - **Torso:** Begins to straighten in preparation for liftoff.

    5. **Full Extension and Arm Swing (Part of Launching the Jump)**:
    - **Time Interval:** t3.5 to t4
    - **Legs:** Complete the extension of knees and hips; toes flex to push off the ground.
    - **Arms:** Rapidly swing upwards, reaching above the head.
    - **Torso:** Aligns with legs, forming a straight line vertically.

    6. **Mid-Air Phase (Ascent):**
    - **Time Interval:** t4 to t4.5
    - **Legs:** Maintain slight bend at knees and hips to stabilize the body.
    - **Arms:** Reach maximum height above the head, then prepare to descend.
    - **Torso:** Aligns upright to stabilize posture during ascent.

    7. **Mid-Air Phase (Peak and Early Descent):**
    - **Time Interval:** t4.5 to t5
    - **Legs:** Start adjusting for landing by preparing to bend further at knees and hips.
    - **Arms:** Begin to lower from the highest point to regain balance and assist in landing.
    - **Torso:** Maintains upright posture, begins slight forward lean to prepare for landing impact.

    8. **Landing Phase**:
    - **Time Interval:** t5 to t6
    - **Legs:** Begin to bend at knees and hips to absorb impact.
    - **Arms:** Swing downward to stabilize and balance.
    - **Torso:** Initially straight, may lean forward upon impact.

    9. **Return to Start Position**:
    - **Time Interval:** t6 to t7
    - **Legs:** Straighten to original standing position.
    - **Arms:** Return to relaxed position at sides.
    - **Torso:** Returns to erect posture.

    These atomic descriptions account for specific actions of each body part across the entire sequence of squatting down, jumping, and returning to the starting position. This detailed level of granularity is crucial for realistic and programmable animation within computer graphics engines.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon further review, the descriptions provided all correspond well in terms of atomicity to the structured dance of motions involved in the action sequence. Each description focuses on specific body parts and their actions during concise time intervals. However, if any could be improved for even more preciseness, the **Landing Phase** stands out. This phase could potentially be split into two parts just like the mid-air phase to depict the initial contact and the follow-through of the landing.

    Here’s how this could be further divided for increased atomicity:

    **8. Initial Landing Contact:**
    - **Time Interval:** t5 to t5.5
    - **Legs:** Feet touch the ground with toes slightly ahead; begin bending knees to absorb impact.
    - **Arms:** Are in the downward motion to help balance the sudden deceleration.
    - **Torso:** Remains slightly forward leaning to distribute the impact.

    **9. Full Landing Stabilization:**
    - **Time Interval:** t5.5 to t6
    - **Legs:** Fully bent knees to absorb the remaining impact force, hips lower towards the heels.
    - **Arms:** Lowered and possibly move slightly backward to aid in final balancing.
    - **Torso:** Adjusts to a more upright position to stabilize the body fully.

    These additional specifics help clarify the landing process, showing the transition from impact to stabilization with distinct adjustments in body parts. Updating the overall sequence to include this added detail would ensure each portion of the motion is captured realistically for graphic animation programming.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    To enhance precision for animation in a computer graphics engine, here are the atomic descriptions for the entire sequence, now including the refined split for the **Landing Phase**:

    1. **Starting Position**:
    - **Time Interval:** t0 to t1
    - **Legs:** Straight, feet shoulder-width apart.
    - **Arms:** Relaxed by the sides.
    - **Torso:** Erect.

    2. **Squatting Down (Preparation Phase)**:
    - **Time Interval:** t1 to t2
    - **Legs:** Bend at the hips and knees to lower the body, heels on the ground.
    - **Arms:** Extend forward parallel to the ground for balance.
    - **Torso:** Maintains erect posture, leans slightly forward to maintain balance.

    3. **Bottom of Squat**:
    - **Time Interval:** t2 to t3
    - **Legs:** Knees bent at approximately 90 degrees, thighs parallel to the ground.
    - **Arms:** Fully extended forward, parallel with the ground.
    - **Torso:** Erect, leaned forward for balance.

    4. **Initial Leg Extension (Part of Launching the Jump)**:
    - **Time Interval:** t3 to t3.5
    - **Legs:** Begin rapid extension of knees and hips, starting to push body upward.
    - **Arms:** Start pulling back to aid in upward momentum.
    - **Torso:** Begins to straighten in preparation for liftoff.

    5. **Full Extension and Arm Swing (Part of Launching the Jump)**:
    - **Time Interval:** t3.5 to t4
    - **Legs:** Complete the extension of knees and hips; toes flex to push off the ground.
    - **Arms:** Rapidly swing upwards, reaching above the head.
    - **Torso:** Aligns with legs, forming a straight line vertically.

    6. **Mid-Air Phase (Ascent)**:
    - **Time Interval:** t4 to t4.5
    - **Legs:** Maintain slight bend at knees and hips to stabilize the body.
    - **Arms:** Reach maximum height above the head, then prepare to descend.
    - **Torso:** Aligns upright to stabilize posture during ascent.

    7. **Mid-Air Phase (Peak and Early Descent)**:
    - **Time Interval:** t4.5 to t5
    - **Legs:** Start adjusting for landing by preparing to bend further at knees and hips.
    - **Arms:** Begin to lower from the highest point to regain balance and assist in landing.
    - **Torso:** Maintains upright posture, begins slight forward lean to prepare for landing impact.

    8. **Initial Landing Contact**:
    - **Time Interval:** t5 to t5.5
    - **Legs:** Feet touch the ground with toes slightly ahead; begin bending knees to absorb impact.
    - **Arms:** Are in the downward motion to help balance the sudden deceleration.
    - **Torso:** Remains slightly forward leaning to distribute the impact.

    9. **Full Landing Stabilization**:
    - **Time Interval:** t5.5 to t6
    - **Legs:** Fully bent knees to absorb the remaining impact force, hips lower towards the heels.
    - **Arms:** Lowered and possibly move slightly backward to aid in final balancing.
    - **Torso:** Adjusts to a more upright position to stabilize the body fully.

    10. **Return to Start Position**:
        - **Time Interval:** t6 to t7
        - **Legs:** Straighten to original standing position.
        - **Arms:** Return to relaxed position at sides.
        - **Torso:** Returns to erect posture.

    These atomic descriptions, now broken down even further within the Landing Phase, offer exceptionally granular information for programming movements in a computer graphics engine, ensuring a highly accurate and realistic animation.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon reviewing the detailed atomic descriptions once again, each step does appear to cover specific actions for body parts within concise and well-defined time intervals, suggesting sufficient granularity for animation purposes in a computer graphics engine.

    Each step delineates actions and movements of legs, arms, and torso in tightly controlled time frames. However, if there is still room for refining atomicity or increasing granularity, one could argue that **Step 10: Return to Start Position** might be slightly less atomic compared to other steps. This description encapsulates the final positioning without explicitly detailing transitional movements for the body parts as they reset to the starting posture.

    Here are more detailed descriptions to make step 10 appropriately atomic:

    **10. Begin Return to Start Position:**
    - **Time Interval:** t6 to t6.5
    - **Legs:** Start straightening from the bent knee position.
    - **Arms:** Begin moving from a potentially lower or outward position back to resting by the sides.
    - **Torso:** Begins to shift from any forward-leaned or adjusted position back to a fully erect posture.

    **11. Complete Return to Start Position:**
    - **Time Interval:** t6.5 to t7
    - **Legs:** Fully straightened, stabilizing in the upright position.
    - **Arms:** Securely placed at the sides.
    - **Torso:** Fully erect, returning to the initial starting posture.

    Splitting the final return to start position into a beginning and completion phase ensures that each segment of this transition is explicitly noted, enhancing clarity and accuracy for the animation sequence—thereby matching the level of detail seen in the other phases.
    ```
- User: `Write down all the atomic descriptions again`
- Assistant:
    ```
    Here are the fully revised atomic descriptions for the sequence of a person squatting down and jumping, now including a more detailed breakdown of the return to the starting position to ensure uniform granularity:

    1. **Starting Position**:
    - **Time Interval:** t0 to t1
    - **Legs:** Straight, feet shoulder-width apart.
    - **Arms:** Relaxed by the sides.
    - **Torso:** Erect.

    2. **Squatting Down (Preparation Phase)**:
    - **Time Interval:** t1 to t2
    - **Legs:** Bend at the hips and knees to lower the body, heels on the ground.
    - **Arms:** Extend forward parallel to the ground for balance.
    - **Torso:** Maintains erect posture, leans slightly forward to maintain balance.

    3. **Bottom of Squat**:
    - **Time Interval:** t2 to t3
    - **Legs:** Knees bent at approximately 90 degrees, thighs parallel to the ground.
    - **Arms:** Fully extended forward, parallel with the ground.
    - **Torso:** Erect, leaned forward for balance.

    4. **Initial Leg Extension (Part of Launching the Jump)**:
    - **Time Interval:** t3 to t3.5
    - **Legs:** Begin rapid extension of knees and hips, starting to push body upward.
    - **Arms:** Start pulling back to aid in upward momentum.
    - **Torso:** Begins to straighten in preparation for liftoff.

    5. **Full Extension and Arm Swing (Part of Launching the Jump)**:
    - **Time Interval:** t3.5 to t4
    - **Legs:** Complete the extension of knees and hips; toes flex to push off the ground.
    - **Arms:** Rapidly swing upwards, reaching above the head.
    - **Torso:** Aligns with legs, forming a straight line vertically.

    6. **Mid-Air Phase (Ascent)**:
    - **Time Interval:** t4 to t4.5
    - **Legs:** Maintain slight bend at knees and hips to stabilize the body.
    - **Arms:** Reach maximum height above the head, then prepare to descend.
    - **Torso:** Aligns upright to stabilize posture during ascent.

    7. **Mid-Air Phase (Peak and Early Descent)**:
    - **Time Interval:** t4.5 to t5
    - **Legs:** Start adjusting for landing by preparing to bend further at knees and hips.
    - **Arms:** Begin to lower from the highest point to regain balance and assist in landing.
    - **Torso:** Maintains upright posture, begins slight forward lean to prepare for landing impact.

    8. **Initial Landing Contact**:
    - **Time Interval:** t5 to t5.5
    - **Legs:** Feet touch the ground with toes slightly ahead; begin bending knees to absorb impact.
    - **Arms:** Are in the downward motion to help balance the sudden deceleration.
    - **Torso:** Remains slightly forward leaning to distribute the impact.

    9. **Full Landing Stabilization**:
    - **Time Interval:** t5.5 to t6
    - **Legs:** Fully bent knees to absorb the remaining impact force, hips lower towards the heels.
    - **Arms:** Lowered and possibly move slightly backward to aid in final balancing.
    - **Torso:** Adjusts to a more upright position to stabilize the body fully.

    10. **Begin Return to Start Position**:
        - **Time Interval:** t6 to t6.5
        - **Legs:** Start straightening from the bent knee position.
        - **Arms:** Begin moving from a potentially lower or outward position back to resting by the sides.
        - **Torso:** Begins to shift from any forward-leaned or adjusted position back to a fully erect posture.

    11. **Complete Return to Start Position**:
        - **Time Interval:** t6.5 to t7
        - **Legs:** Fully straightened, stabilizing in the upright position.
        - **Arms:** Securely placed at the sides.
        - **Torso:** Fully erect, returning to the initial starting posture.

    These atomic descriptions now evenly cover every component of the movement sequence with sufficient detail for granular control in a computer graphics engine, ensuring realistic and accurate animation.
    ```
- User: `Which description above is not atomic enough?`
- Assistant:
    ```
    Upon careful review, the atomic descriptions provided for each phase of the action are precise, each detailing the movement of specific body parts within clear time intervals. Each description concentrates on the motion of the legs, arms, and torso during various, well-defined parts of the action sequence.

    Given these details, the descriptions currently align well with the concept of an "atomic" action that can be used as programmatic input into a computer graphics engine. Each stage has been split appropriately to ensure granularity that is finely tuned for realistic animations. Hence, none of the descriptions outlined in the list inherently lacks atomicity; they are all sufficiently detailed for animation purposes.

    To confirm, the information:
    - Is focused on specific parts of the body.
    - Addresses precise movements.
    - Includes clear timing intervals.
    - Separates each phase of motion uniquely and distinctly.

    If further granularity or adjustments are desired, they would likely pertain more to tuning parameters such as exact angles and speeds rather than further breaking down the descriptions. However, based on standard requirements for creating realistic animations via programmatic input, the current set of descriptions should be deemed adequately atomic.
    ```
- User: `Refine the final atomic descriptions into a tabular representation. This representation should at least specify two dimensions - the time scale and body part scale`
- Assistant:
    ```
    To efficiently document and manage the detailed atomic descriptions for the motion of squatting down and jumping, a tabular representation can be very useful. This table will categorize the movements by body part and time interval, providing a clear overview that could easily be translated into animation commands in a computer graphics engine. Below is the tabular representation dividing the descriptions along two dimensions: the time scale and the body part scale.
    ```
    | Time Interval | Body Part | Description                                                  |
    |---------------|-----------|--------------------------------------------------------------|
    | t0 to t1      | Legs      | Straight, feet shoulder-width apart.                         |
    |               | Arms      | Relaxed by the sides.                                        |
    |               | Torso     | Erect.                                                       |
    | t1 to t2      | Legs      | Bend at the hips and knees, heels on the ground.             |
    |               | Arms      | Extend forward parallel to the ground for balance.           |
    |               | Torso     | Maintains erect posture, leans slightly forward to maintain balance. |
    | t2 to t3      | Legs      | Knees bent 90 degrees, thighs parallel to the ground.        |
    |               | Arms      | Fully extended forward, parallel with the ground.            |
    |               | Torso     | Erect, leaned forward for balance.                           |
    | t3 to t3.5    | Legs      | Begin rapid extension of knees and hips, pushing body upward.|
    |               | Arms      | Start pulling back to aid in upward momentum.                |
    |               | Torso     | Begins to straighten in preparation for liftoff.             |
    | t3.5 to t4    | Legs      | Complete extension; toes flex to push off the ground.        |
    |               | Arms      | Rapidly swing upwards, reaching above the head.              |
    |               | Torso     | Aligns with legs, forming a straight line vertically.        |
    | t4 to t4.5    | Legs      | Maintain slight bend at knees and hips to stabilize the body.|
    |               | Arms      | Reach maximum height above the head, then prepare to descend.|
    |               | Torso     | Aligns upright to stabilize posture during ascent.           |
    | t4.5 to t5    | Legs      | Start adjusting for landing, preparing to bend further.      |
    |               | Arms      | Begin to lower from the highest point to assist in landing.  |
    |               | Torso     | Maintains upright posture, begins slight forward lean.       |
    | t5 to t5.5    | Legs      | Feet touch the ground, begin bending knees to absorb impact. |
    |               | Arms      | In the downward motion for balance during deceleration.      |
    |               | Torso     | Slightly forward leaning to distribute the impact.           |
    | t5.5 to t6    | Legs      | Fully bend knees absorbing force, hips lower towards heels.  |
    |               | Arms      | Lowered, move slightly backward to aid in balancing.         |
    |               | Torso     | Adjusts to a more upright position to stabilize the body fully. |
    | t6 to t6.5    | Legs      | Start straightening from the bent knee position.             |
    |               | Arms      | Begin moving back to resting by the sides.                   |
    |               | Torso     | Shifts from any forward-leaned position back to fully erect. |
    | t6.5 to t7    | Legs      | Fully straightened, stabilizing in the upright position.     |
    |               | Arms      | Securely placed at the sides.                                |
    |               | Torso     | Fully erect, returning to the initial starting posture.      |
    ```
    This tabular format offers a streamlined and structured view, simplifying the understanding of the sequence and easing the tasks of programming and animation by dividing the motion into comprehensible segments focused on specific time intervals and body parts.
    ```

- **Analysis**
    - When I ask the model to further recursively decompose the descriptions, I can get more fine-grained atomic generation.
    - Refinement into a table helps clearer representation.

##### Complex motion 1 (modified 1)

- https://platform.openai.com/playground/p/FtWvIkJKM61BZMqfvisbKcWU?model=gpt-4-turbo-2024-04-09&mode=chat
- **Comments**
    - This example shows that if we keep asking the LLM, the LLM will gradually decompose the motion down to the level of joint and body part movements with precise angles and durations. Then the LLM will specify muscle tension, breath, nervous system, etc. We need to specify the expected granularity (body parts, joints, angles, durations, etc.) and which part more worthwhile to recursively decompose.
    - We might need to specify some simple pseudo-codes with args to denote some commonly used or generated contents, e.g., `START`, `RECURSION(arg)`, `FINISH`, etc. The current pure natural language based generation is too redundant.


#### Task and pseudo-code motion planning
##### Squat and jump

- System:
    ```
    You will be given a high-level motion instruction. You will decompose this instruction down into a structured combination of atomic descriptions that can potentially serve as programmatic inputs into a computer graphics engine without substantive modification.

    There are two steps --- task planning and motion planning. In task planning, decompose the original motion instruction into several key procedures in natural language. In motion planning, decompose each key procedure into a structured series of atomic descriptions.

    An atomic description specifies the movement of a relevant body part in a certain time interval. For the movement, use **degree** as the movement unit and specify **the reference position or body part**. For the time interval, use **second** as the time unit. The format is {PERIOD}: {BODY_PART} ({REFERENCE_BODY_PART}) {START_DEGREE} -> {END_DEGREE}

    ###
    {BODY_PART}: ['head', 'torso', 'left upper arm', 'left forearm', 'left thigh', 'left calf', 'right upper arm', 'right forearm', 'right thigh', 'right calf', 'left foot', 'right foot']

    ###
    Constraints:
    # {BODY_PART} ({REFERENCE_BODY_PART}) [{DEGREE_INITIAL}, {DEGREE_LIMIT}]
    torso (vertical) [0, 90] # bend forward
    torso (vertical) [0, -90] # bend backward
    head (torso) [0, 90] # bend forward
    head (torso) [0, -90] # bend backward
    left thigh (torso) [0, 180] # from straight to totally bending
    right thigh (torso) [0, 180] # from straight to totally bending
    left calf (left thigh) [0, 180] # from straight to totally bending
    right calf (right thigh) [0, 180] # from straight to totally bending
    left foot (left calf) [0, 45] # from orthogonal to bending the left foot toward the right calf
    left foot (left calf) [0, -90] # from orthogonal to bending the left foot outward
    right foot (right calf) [0, 45] # from orthogonal to bending the right foot toward the right calf
    right foot (right calf) [0, -90] # from orthogonal to bending the left foot outward
    left forearm (left upper arm) [0, 180] # from straight to totally bending
    right forearm (right upper arm) [0, 180] # from straight to totally bending
    left upper arm (torso) [0, 180] # from sticking to the torso to raising above
    right upper arm (torso) [0, 180] # from sticking to the torso to raising above
    ```
- User: `A person squats down then jumps.`
- Assistant:
    ```
    ### Task Planning
    **Task 1: Squat Down**
    1. Bend torso forward
    2. Bend both knees
    3. Lower hips
    4. Adjust arms for balance

    **Task 2: Jump**
    1. Extend legs
    2. Push off the ground with both feet
    3. Extend arms for momentum
    4. Land back on both feet and stabilize

    ### Motion Planning

    **Task 1: Squat Down**
    - **1. Bend torso forward**
        - 0-1s: torso (vertical) 0 -> 30
    - **2. Bend both knees**
        - 0-1s: right thigh (torso) 0 -> 90
        - 0-1s: left thigh (torso) 0 -> 90
        - 0-1s: right calf (right thigh) 0 -> 90
        - 0-1s: left calf (left thigh) 0 -> 90
    - **3. Lower hips**
        - Concurrent with knee bending
    - **4. Adjust arms for balance**
        - 0-1s: right upper arm (torso) 0 -> 30
        - 0-1s: left upper arm (torso) 0 -> 30
        - 0-1s: right forearm (right upper arm) 0 -> 45
        - 0-1s: left forearm (left upper arm) 0 -> 45

    **Task 2: Jump**
    - **1. Extend legs**
        - 1-2s: right thigh (torso) 90 -> 0
        - 1-2s: left thigh (torso) 90 -> 0
        - 1-2s: right calf (right thigh) 90 -> 0
        - 1-2s: left calf (left thigh) 90 -> 0
    - **2. Push off the ground with both feet**
        - 1-2s: right foot (right calf) 0 -> -45
        - 1-2s: left foot (left calf) 0 -> -45
    - **3. Extend arms for momentum**
        - 1-2s: right forearm (right upper arm) 45 -> 0
        - 1-2s: left forearm (left upper arm) 45 -> 0
        - 1-2s: right upper arm (torso) 30 -> 90
        - 1-2s: left upper arm (torso) 30 -> 90
    - **4. Land back on both feet and stabilize**
        - 2-3s: right foot (right calf) -45 -> 0
        - 2-3s: left foot (left calf) -45 -> 0
        - 2-3s: torso (vertical) 30 -> 0
        - 2-3s: right upper arm (torso) 90 -> 0
        - 2-3s: left upper arm (torso) 90 -> 0
    ```
- Comments
    - First task planning then motion planning helps overcome the problem of non-physical motions (e.g., squating without extending arms)
    - Specifying body parts and constraints greatly increases the well-formedness of generate answers
    - Adding comments after constraints help the model more deeply understand the directions of degrees