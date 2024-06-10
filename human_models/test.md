name:metarig,position:(0.00,0.00,0.00),rotation:(-0.7,0.0,0.0,0.7),
children:[
    name:spine,position:(0.00,0.00,0.00),rotation :(0.7,0.0,0.0,0.7),
    children:[
        name:pelvis.L,position :(0.00,0.00,0.00),rotation:(-0.2,0.6,0.7,0.4),
        name:pelvis.R, position:(0.00,0.00,0.00),rotation:(0.2,0.6,0.7,-0.4),
        name:spine .001,position:(0.00,0.00,0.00),rotation:(0.0,0.0,0.0,1.0),
        children :[
            name:spine.002,position:(0.00,0.00,0.00),rotation :(0.0,0.0,0.0,1.0),
            children:[name:spine.003,position :(0.00,0.00,0.00),rotation:(-0.1,0.0,0.0,1.0),children:[
            name: breast.L,position:(0.00,0.00,0.00),rotation:(0.0,0.8,0.6,0.0),
            name :breast.R,position:(0.00,0.00,0.00),rotation:(0.0,0.8,0.6,0.0),
            name:shoulder.L,position:(0.00,0.00,0.00),rotation :(-0.7,0.2,0.4,0.6),
            children:[name:upper_arm.L,position :(0.00,0.00,0.00),rotation:(0.2,-0.7,0.4,0.5),children:[name: forearm.L,position:(0.00,0.00,0.00),rotation:(0.5,0.0,0.0,0.8), children:[name:hand.L,position:(0.00,0.00,0.00),rotation :(0.1,0.0,-0.1,1.0)]]],
            name:shoulder.R,position:(0.00,0.00,0.00), rotation:(-0.7,-0.2,-0.4,0.6),
            children:[name:upper_arm.R,position :(0.00,0.00,0.00),rotation:(-0.1,0.9,-0.3,0.4),children:[name: forearm.R,position:(0.00,0.00,0.00),rotation:(-0.1,0.2,-0.6,0.8), children:[name:hand.R,position:(0.00,0.00,0.00),rotation :(0.1,0.1,-0.2,1.0),children:[name:hand.R.001,position :(0.00,0.00,0.00),rotation:(0.3,0.0,0.7,0.6),children:[name: Spork_low,position:(0.00,0.00,0.00),rotation:(0.0,0.7,-0.7,0.1) ]]]]],
            name:spine.006,position:(0.00,0.00,0.00),rotation :(-0.1,0.0,0.0,1.0),
            children:[name:ear.L,position:(0.00,0.01,0.00) ,rotation:(-0.1,-0.1,0.2,1.0),name:ear.R,position:(0.00,0.01,0.00) ,rotation:(-0.1,0.1,-0.5,0.9)]
            ]
        ]],
        name:tail,position :(0.00,0.00,0.00),rotation:(0.8,0.4,-0.1,-0.3),
        children:[
            name:tail .001,position:(0.00,0.00,0.00),rotation:(-0.2,0.1,-0.2,1.0), children:[name:tail.002,position:(0.00,0.00,0.00),rotation :(0.0,0.5,-0.5,0.7),children:[name:tail.003,position :(0.00,0.00,0.00),rotation:(-0.5,0.0,0.0,0.8)]]
        ],
        name:thigh.L, position:(0.00,0.00,0.00),rotation:(1.0,0.1,-0.3,0.0),
        children:[ name:shin.L,position:(0.00,0.00,0.00),rotation:(0.2,0.3,-0.1,0.9), children:[name:foot.L,position:(0.00,0.00,0.00),rotation :(-0.5,0.1,0.2,0.8),children:[name:heel.02.L,position :(0.00,0.00,0.00),rotation:(-0.6,0.6,-0.2,-0.5),name:toe.L, position:(0.00,0.00,0.00),rotation:(-0.3,0.8,-0.4,-0.3)]]],name: thigh.R,position:(0.00,0.00,0.00),rotation:(1.0,-0.1,0.3,0.0),children:[name:shin.R,position:(0.00,0.00,0.00),rotation :(0.2,-0.3,0.1,0.9),
            children:[
                name:foot.R,position :(0.00,0.00,0.00),rotation:(-0.5,-0.1,-0.2,0.8),
                children:[
                    name: heel.02.R,position:(0.00,0.00,0.00),rotation:(0.6,0.6,-0.2,0.5),
                    name:toe.R,position:(0.00,0.00,0.00),rotation:(0.3,0.8,-0.4,0.3)
                ]
            ]
        ]
    ]
]