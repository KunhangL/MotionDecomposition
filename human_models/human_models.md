# Skeleton-based

## SMPL
```
SMPL_KEYPOINTS = [
    'pelvis',
    'left_hip',
    'right_hip',
    'spine_1',
    'left_knee',
    'right_knee',
    'spine_2',
    'left_ankle',
    'right_ankle',
    'spine_3',
    'left_foot',
    'right_foot',
    'neck',
    'left_collar',
    'right_collar',
    'head',
    'left_shoulder',
    'right_shoulder',
    'left_elbow',
    'right_elbow',
    'left_wrist',
    'right_wrist',
    'left_hand',
    'right_hand',
]
```
<center><img src="./SMPL_keypoints.png" alt="drawing"/ width=300></center>

- Notes
    - The collection of skeleton-based human models (https://github.com/open-mmlab/mmhuman3d/tree/main/mmhuman3d/core/conventions/keypoints_mapping)<br>
    - The SMPL paper (https://files.is.tue.mpg.de/black/papers/SMPL2015.pdf)<br>
    - `SMPL_blender_addon` (Video: https://www.youtube.com/watch?v=DY2k29Jef94; Code: https://github.com/Meshcapade/SMPL_blender_addon/tree/main)<br>

- Comments
    - Might need to merge some joints, or assign the same motion to several joints?
    - How to animate a simple human model (mixamo / SMPL) in Unity with the LLM? $\rightarrow$ Related work: [Real-time Animation Generation and Control on Rigged Models via Large Language Models](https://github.com/Whalefishin/LLM_animation)
        - Method 1 (data-driven): Generate animation raw data with the LLM, and convert into animation clips in Unity.
            - Pros: Expressive in motions;
            - Cons: Too long to generate; $\rightarrow$ Possible solutions: Specify a compact output format to be converted into an FBX file. / Only generate key frames and interpolate. / Develop a recursive generation method.
        - Method 2 (script-driven): Generate C# animation scripts which utilize mathematical functions to describe the animation curves with the LLM.
            - Pros
                - Meaningful in terms of the combination of spatial semantics and the codes;
                - Relatively straightforward;
            - Cons
                - Lack of motion expressivity compared with the data-driven method;
                - The LLM seems not to be very good at the combination of spatial semantics and the codes (**INITIAL** attempts failed); $\rightarrow$ Might need to explore more, e.g., putting more necessary spatial information into the prompt. / We ask the LLM to generate scripts to drive the motions, but it's very hard to immediately generate a good motion script. So we use a video2text/image2text model (even GPT4o itself) to evaluate the generated motion, and then automatically modify the script correspondingly.
        - Method 3 (pipeline): Utilize existing text2motion datasets/models to generate motions for simple texts as assets + Utilize existing video2text/image2text captioning models to generate fine-grained descriptions for the existing motions + Utilize the LLM and the graphics engine to select, modify and stitch the existing motions
            - Pros
                - The graphics engine provides a sophisticated platform with semantically meaningful codes for the motion system;
                - Utilize specialized text2motion models to generate motions for simple texts as assets, instead of leaving this heavy task to the LLM;
				- Utilize existing captioning models to generate fine-grained descriptions for the existing motions, to prepare for selection, modification and stitching;
                - Utilize the LLM to plan the target motion, and adapt the primitive motions to the graphics engine;
            - Cons: Complicated; $\rightarrow$ Ready to try this!

- Prompts
	- Hierarchy
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
	3. Please **automatically** assign the root joint in the script.
	3. Any body parts cannot sink into the ground, which means the Y position should always be greater than 0.
	4. For the root body part 'm_avg_root', you can perform both translation and rotation.
	5. For all the other body parts except for the root body part, you can only perform rotation.
	```
	- Rotation Specifications
	```
	**Hierarchical Rotation Specifications from the Initial T-pose**
	1. Root (m_avg_root):
	- Typically, the root joint handles global positioning and rotation of the entire model.
	2. Pelvis (m_avg_Pelvis):
		- Local X Rotation: (+) Tilts the pelvis forward / (-) Tilts the pelvis backward
		- Local Y Rotation: (-) Rotates the pelvis left / (+) Rotates the pelvis right
		- Local Z Rotation: (+) Tilts the pelvis to the left / (-) Tilts the pelvis to the right
		// Example: Slight tilt forward for pelvis
		// m_avg_Pelvis.localRotation = Quaternion.Euler(10, 0, 0);
	3. Left Hip (m_avg_L_Hip):
		- Local X Rotation: (+) Moves the leg backward / (-) Moves the leg forward
		- Local Y Rotation: (+) Swivels the leg inward / (-) Swivels the leg outward
		- Local Z Rotation: (+) Twists the leg counterclockwise / (-) Twists the leg clockwise
		// Example: Raise the left leg by 30 degrees
		// m_avg_L_Hip.localRotation = Quaternion.Euler(-30, 0, 0);
	4. Left Knee (m_avg_L_Knee):
		- Local X Rotation: Bends the knee forward/backward.
		- Local Y Rotation: Twists the knee inward/outward.
		- Local Z Rotation: Rarely used.
		// Example: Bend the left knee 45 degrees
		m_avg_L_Knee.localRotation = Quaternion.Euler(45, 0, 0);
	5. Left Ankle (m_avg_L_Ankle):
		- Local X Rotation: Points the foot up/down.
		- Local Y Rotation: Twists the foot inward/outward.
		- Local Z Rotation: Tilts the foot side to side.
		// Example: Point the left foot down 30 degrees
		m_avg_L_Ankle.localRotation = Quaternion.Euler(-30, 0, 0);
	6. Left Foot (m_avg_L_Foot):
		- Local rotations for minor adjustments or toe movements.
		// No specific example; depends on required animation.
	7. Right Hip (m_avg_R_Hip):
		- Similar to Left Hip but for the right leg.
		// Example: Raise the right leg by 30 degrees
		m_avg_R_Hip.localRotation = Quaternion.Euler(-30, 0, 0);
	8. Right Knee (m_avg_R_Knee):
		- Similar to Left Knee.
		// Example: Bend the right knee 45 degrees
		m_avg_R_Knee.localRotation = Quaternion.Euler(45, 0, 0);
	9. Right Ankle (m_avg_R_Ankle):
		- Similar to Left Ankle.
		// Example: Point the right foot down 30 degrees
		m_avg_R_Ankle.localRotation = Quaternion.Euler(-30, 0, 0);
	10. Right Foot (m_avg_R_Foot):
		- Local rotations for minor adjustments or toe movements.
		// No specific example; depends on required animation.
	11. Spine1, Spine2, Spine3:
		- Local X Rotation: Bends the spine forward/backward.
		- Local Y Rotation: Twists the torso left/right.
		- Local Z Rotation: Tilts the torso sideways.
		// Example: Slight forward bend
		m_avg_Spine1.localRotation = Quaternion.Euler(10, 0, 0);
		m_avg_Spine2.localRotation = Quaternion.Euler(5, 0, 0);
		m_avg_Spine3.localRotation = Quaternion.Euler(2, 0, 0);
	12. Neck (m_avg_Neck):
		- Local X Rotation: Tilts the head up/down.
		- Local Y Rotation: Turns the head left/right.
		- Local Z Rotation: Tilts the head side to side.
		// Example: Tilt the head backward
		m_avg_Neck.localRotation = Quaternion.Euler(-20, 0, 0);
	13. Head (m_avg_Head):
		- Fine adjustments to head rotation.
		// Example: Look slightly to the left
		m_avg_Head.localRotation = Quaternion.Euler(0, -10, 0);
	14. Left Collar (m_avg_L_Collar):
		- Local rotations to adjust shoulder orientation.
	15. Left Shoulder (m_avg_L_Shoulder):
		- Local X Rotation: Raises/lowers the arm.
		- Local Y Rotation: Moves the arm forward/backward.
		- Local Z Rotation: Twists the arm.
		// Example: Raise the left arm by 45 degrees
		m_avg_L_Shoulder.localRotation = Quaternion.Euler(0, 0, 45);
	16. Left Elbow (m_avg_L_Elbow):
		- Previously specified.
	17. Left Wrist (m_avg_L_Wrist):
		- Local X Rotation: Tilts the hand up/down.
		- Local Y Rotation: Twist the wrist.
		- Local Z Rotation: Tilts the hand side to side.
		// Example: Tilt the left hand upward
		m_avg_L_Wrist.localRotation = Quaternion.Euler(30, 0, 0);
	18. Left Hand (m_avg_L_Hand):
		- Fine adjustments for hand and finger movements.
		// Example: Slight finger curl (if detailed finger joints are present)
	19. Right Collar (m_avg_R_Collar):
		- Local rotations to adjust shoulder orientation.
		// Example: Pose adjustment (depends on desired animation)
	20. Right Shoulder (m_avg_R_Shoulder):
		- Similar to Left Shoulder.
		// Example: Lower the right arm by 45 degrees
		m_avg_R_Shoulder.localRotation = Quaternion.Euler(0, 0, -45);
	21. Right Elbow (m_avg_R_Elbow):
		- Similar to Left Elbow.
		// Example: Bend the right elbow inward
		m_avg_R_Elbow.localRotation = Quaternion.Euler(0, 0, -45);
	22. Right Wrist (m_avg_R_Wrist):
		- Similar to Left Wrist.
		// Example: Tilt the right hand downward
		m_avg_R_Wrist.localRotation = Quaternion.Euler(-30, 0, 0);
	23. Right Hand (m_avg_R_Hand):
		- Fine adjustments for hand and finger movements.
		// Example: Fine finger movements (if detailed finger joints are present)
	```
	- Notes
		- Version 1: Hierarchy
		- Version 2: + Rotation specifications (examples / detailed specifications)
		- Versioin 2: + body constraints or specification
		- Version 3: + ground







# Appendix
- Information regarding the body parts extracted from the character FBX file
```
; Object definitions
;------------------------------------------------------------------

Definitions:  {

	ObjectType: "Model" {
		Count: 26
		PropertyTemplate: "FbxNode" {
			Properties70:  {
				P: "QuaternionInterpolate", "enum", "", "",0
				P: "RotationOffset", "Vector3D", "Vector", "",0,0,0
				P: "RotationPivot", "Vector3D", "Vector", "",0,0,0
				P: "ScalingOffset", "Vector3D", "Vector", "",0,0,0
				P: "ScalingPivot", "Vector3D", "Vector", "",0,0,0
				P: "TranslationActive", "bool", "", "",0
				P: "TranslationMin", "Vector3D", "Vector", "",0,0,0
				P: "TranslationMax", "Vector3D", "Vector", "",0,0,0
				P: "TranslationMinX", "bool", "", "",0
				P: "TranslationMinY", "bool", "", "",0
				P: "TranslationMinZ", "bool", "", "",0
				P: "TranslationMaxX", "bool", "", "",0
				P: "TranslationMaxY", "bool", "", "",0
				P: "TranslationMaxZ", "bool", "", "",0
				P: "RotationOrder", "enum", "", "",0
				P: "RotationSpaceForLimitOnly", "bool", "", "",0
				P: "RotationStiffnessX", "double", "Number", "",0
				P: "RotationStiffnessY", "double", "Number", "",0
				P: "RotationStiffnessZ", "double", "Number", "",0
				P: "AxisLen", "double", "Number", "",10
				P: "PreRotation", "Vector3D", "Vector", "",0,0,0
				P: "PostRotation", "Vector3D", "Vector", "",0,0,0
				P: "RotationActive", "bool", "", "",0
				P: "RotationMin", "Vector3D", "Vector", "",0,0,0
				P: "RotationMax", "Vector3D", "Vector", "",0,0,0
				P: "RotationMinX", "bool", "", "",0
				P: "RotationMinY", "bool", "", "",0
				P: "RotationMinZ", "bool", "", "",0
				P: "RotationMaxX", "bool", "", "",0
				P: "RotationMaxY", "bool", "", "",0
				P: "RotationMaxZ", "bool", "", "",0
				P: "InheritType", "enum", "", "",0
				P: "ScalingActive", "bool", "", "",0
				P: "ScalingMin", "Vector3D", "Vector", "",0,0,0
				P: "ScalingMax", "Vector3D", "Vector", "",1,1,1
				P: "ScalingMinX", "bool", "", "",0
				P: "ScalingMinY", "bool", "", "",0
				P: "ScalingMinZ", "bool", "", "",0
				P: "ScalingMaxX", "bool", "", "",0
				P: "ScalingMaxY", "bool", "", "",0
				P: "ScalingMaxZ", "bool", "", "",0
				P: "GeometricTranslation", "Vector3D", "Vector", "",0,0,0
				P: "GeometricRotation", "Vector3D", "Vector", "",0,0,0
				P: "GeometricScaling", "Vector3D", "Vector", "",1,1,1
				P: "MinDampRangeX", "double", "Number", "",0
				P: "MinDampRangeY", "double", "Number", "",0
				P: "MinDampRangeZ", "double", "Number", "",0
				P: "MaxDampRangeX", "double", "Number", "",0
				P: "MaxDampRangeY", "double", "Number", "",0
				P: "MaxDampRangeZ", "double", "Number", "",0
				P: "MinDampStrengthX", "double", "Number", "",0
				P: "MinDampStrengthY", "double", "Number", "",0
				P: "MinDampStrengthZ", "double", "Number", "",0
				P: "MaxDampStrengthX", "double", "Number", "",0
				P: "MaxDampStrengthY", "double", "Number", "",0
				P: "MaxDampStrengthZ", "double", "Number", "",0
				P: "PreferedAngleX", "double", "Number", "",0
				P: "PreferedAngleY", "double", "Number", "",0
				P: "PreferedAngleZ", "double", "Number", "",0
				P: "LookAtProperty", "object", "", ""
				P: "UpVectorProperty", "object", "", ""
				P: "Show", "bool", "", "",1
				P: "NegativePercentShapeSupport", "bool", "", "",1
				P: "DefaultAttributeIndex", "int", "Integer", "",-1
				P: "Freeze", "bool", "", "",0
				P: "LODBox", "bool", "", "",0
				P: "Lcl Translation", "Lcl Translation", "", "A",0,0,0
				P: "Lcl Rotation", "Lcl Rotation", "", "A",0,0,0
				P: "Lcl Scaling", "Lcl Scaling", "", "A",1,1,1
				P: "Visibility", "Visibility", "", "A",1
				P: "Visibility Inheritance", "Visibility Inheritance", "", "",1
			}
		}
	}

}

; Object properties
;------------------------------------------------------------------

Objects:  {

	Model: 140378808671232, "Model::m_avg", "Mesh" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",1
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "AL7",0,0,0
			P: "Lcl Rotation", "Lcl Rotation", "", "AL7",0,0,0
			P: "Lcl Scaling", "Lcl Scaling", "", "AL7",1,1,1
		}
		Shading: T
		Culling: "CullingOff"
	}
	Model: 140378808674816, "Model::m_avg_root", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",1
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808678400, "Model::m_avg_Pelvis", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-0.217367915589215,97.2723857779389,2.85837934769579
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808681984, "Model::m_avg_L_Hip", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",5.85813504507656,-8.22800412730611,-1.76640839745186
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808685568, "Model::m_avg_L_Knee", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",4.34514314503899,-38.6469457538986,0.803700217630674
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808689152, "Model::m_avg_L_Ankle", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-1.479033494873,-42.6874391452085,-3.74279940964569
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808692736, "Model::m_avg_L_Foot", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",4.10543674633154,-6.02859492311727,12.204242350686
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808696320, "Model::m_avg_R_Hip", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-6.03097291884147,-9.05132843011647,-1.354252931849
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808699904, "Model::m_avg_R_Knee", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-4.32566254253949,-38.3687877466446,-0.484304494182445
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808703488, "Model::m_avg_R_Ankle", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",1.9055544286818,-42.0045587890346,-3.45616702037777
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808707072, "Model::m_avg_R_Foot", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-3.48398706827247,-6.2105561171744,13.0323289537847
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808710656, "Model::m_avg_Spine1", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",0.443944898221867,12.4403551233992,-3.83852227732937
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808714240, "Model::m_avg_Spine2", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",0.44884401766645,13.7956399353686,2.68203279187967
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808717824, "Model::m_avg_Spine3", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-0.226458745836407,5.60324043117619,0.285504453980784
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808721408, "Model::m_avg_Neck", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-1.33901850163491,21.1635514692671,-3.34675763976523
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808724992, "Model::m_avg_Head", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",1.01132115910344,8.8937353899629,5.04098606300206
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808728576, "Model::m_avg_L_Collar", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",7.17024751888973,11.3999713923281,-1.88981710845057
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808732160, "Model::m_avg_L_Shoulder", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",12.2921382186775,4.5205076329708,-1.9045999826937
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808735744, "Model::m_avg_L_Elbow", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",25.5331898315701,-1.56490327473171,-2.29464854803309
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808739328, "Model::m_avg_L_Wrist", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",26.5709255263499,1.26981037070203,-0.737473431115989
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808742912, "Model::m_avg_L_Hand", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",8.66905441238188,-1.06360603299893,-1.55942904792877
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808746496, "Model::m_avg_R_Collar", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-8.29536517743771,11.2472303849185,-2.37073845553838
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808750080, "Model::m_avg_R_Shoulder", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-11.3228312318425,4.68532786471522,-0.847206923501845
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808753664, "Model::m_avg_R_Elbow", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-26.0127500631845,-1.43692952953938,-3.12687296438665
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808757248, "Model::m_avg_R_Wrist", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-26.9108382383609,0.679372784357952,-0.602676583284452
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}
	Model: 140378808760832, "Model::m_avg_R_Hand", "LimbNode" {
		Version: 232
		Properties70:  {
			P: "RotationActive", "bool", "", "",1
			P: "InheritType", "enum", "", "",2
			P: "ScalingMax", "Vector3D", "Vector", "",0,0,0
			P: "DefaultAttributeIndex", "int", "Integer", "",0
			P: "Lcl Translation", "Lcl Translation", "", "A",-8.87537661914463,-0.865157243230385,-1.01070787784667
			P: "lockInfluenceWeights", "Bool", "", "A+U",0
		}
		Shading: Y
		Culling: "CullingOff"
	}

}

; Object connections
;------------------------------------------------------------------

Connections:  {
	
	;Model::m_avg, Model::RootNode
	C: "OO",140378808671232,0
	
	;Model::m_avg_root, Model::RootNode
	C: "OO",140378808674816,0
	
	;Model::m_avg_Pelvis, Model::m_avg_root
	C: "OO",140378808678400,140378808674816
	
	;Model::m_avg_L_Hip, Model::m_avg_Pelvis
	C: "OO",140378808681984,140378808678400
	
	;Model::m_avg_R_Hip, Model::m_avg_Pelvis
	C: "OO",140378808696320,140378808678400
	
	;Model::m_avg_Spine1, Model::m_avg_Pelvis
	C: "OO",140378808710656,140378808678400
	
	;Model::m_avg_L_Knee, Model::m_avg_L_Hip
	C: "OO",140378808685568,140378808681984
	
	;Model::m_avg_L_Ankle, Model::m_avg_L_Knee
	C: "OO",140378808689152,140378808685568
	
	;Model::m_avg_L_Foot, Model::m_avg_L_Ankle
	C: "OO",140378808692736,140378808689152
	
	;Model::m_avg_R_Knee, Model::m_avg_R_Hip
	C: "OO",140378808699904,140378808696320
	
	;Model::m_avg_R_Ankle, Model::m_avg_R_Knee
	C: "OO",140378808703488,140378808699904
	
	;Model::m_avg_R_Foot, Model::m_avg_R_Ankle
	C: "OO",140378808707072,140378808703488
	
	;Model::m_avg_Spine2, Model::m_avg_Spine1
	C: "OO",140378808714240,140378808710656
	
	;Model::m_avg_Spine3, Model::m_avg_Spine2
	C: "OO",140378808717824,140378808714240
	
	;Model::m_avg_Neck, Model::m_avg_Spine3
	C: "OO",140378808721408,140378808717824
	
	;Model::m_avg_L_Collar, Model::m_avg_Spine3
	C: "OO",140378808728576,140378808717824
	
	;Model::m_avg_R_Collar, Model::m_avg_Spine3
	C: "OO",140378808746496,140378808717824
	
	;Model::m_avg_Head, Model::m_avg_Neck
	C: "OO",140378808724992,140378808721408
	
	;Model::m_avg_L_Shoulder, Model::m_avg_L_Collar
	C: "OO",140378808732160,140378808728576
	
	;Model::m_avg_L_Elbow, Model::m_avg_L_Shoulder
	C: "OO",140378808735744,140378808732160
	
	;Model::m_avg_L_Wrist, Model::m_avg_L_Elbow
	C: "OO",140378808739328,140378808735744
	
	;Model::m_avg_L_Hand, Model::m_avg_L_Wrist
	C: "OO",140378808742912,140378808739328
	
	;Model::m_avg_R_Shoulder, Model::m_avg_R_Collar
	C: "OO",140378808750080,140378808746496
	
	;Model::m_avg_R_Elbow, Model::m_avg_R_Shoulder
	C: "OO",140378808753664,140378808750080
	
	;Model::m_avg_R_Wrist, Model::m_avg_R_Elbow
	C: "OO",140378808757248,140378808753664
	
	;Model::m_avg_R_Hand, Model::m_avg_R_Wrist
	C: "OO",140378808760832,140378808757248

}
```