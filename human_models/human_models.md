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