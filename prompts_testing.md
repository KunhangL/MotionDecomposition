## Model: gpt-4-turbo-2024-04-09

### Pure textual instructions
1. 
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

2. 
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

3. 
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
#### Analysis
1. Currently I only ask the model to further recursively decompose in the second run, which indeed helps more fine-grained and atomic generation.
2. Refinement into a table helps clearer representation.

#### TODO
1. Try the methods with more complex motions
2. Design a looping mechanism to really enable recursively decomposition.