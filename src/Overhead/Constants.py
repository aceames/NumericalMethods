'''
Created on Jul 27, 2015

@author: aeames
'''
'''
These coefficients are presumed constant and are used 
to describe the quantities below as functions of temperature
in the form:

    Y    = A + B*(T^-1) + C*(T^-2)  + D*(T^-3)  + E*(T^-4)
    
Parameters are provided in lists as:

    P    = [A, B, C ,
            D, E    ]
'''

#
#    PARAMS FOR EQUILIBRIUM COEFFICIENT #4 FIT, SEE ABU-ARABI REFERENCE
#
k_4_coefficients    = [float(39.5554),      float(-9.8790e4),   float(0.5688e8) , 
                       float(-0.1465e11),   float(0.1361e13)                    ]
#
#    PARAMS FOR EQUILIBRIUM COEFFICIENT #6 FIT, SEE ABU-ARABI REFERENCE
#
k_6_coefficients    = [float(-304.6890),    float(38.7211e4),   float(-1.9476e8), 
                       float(0.4381e11),    float(-0.3732e13)                   ]
#
#    PARAMS FOR EQUILIBRIUM COEFFICIENT #7 FIT, SEE ABU-ARABI REFERENCE
#
k_7_coefficients    = [float(-657.9650),    float(91.6311e4),   float(-4.9063e8),
                       float(1.1531e11),    float(-1.0102e13)                   ]
#
#    PARAMS FOR EQUILIBRIUM Henry's Law Constant, SEE ABU-ARABI REFERENCE
#
H_H2S_coefficients  = [float(104.5180),     float(-13.6808e4),  float(0.7377e8) , 
                       float(-0.1747e11),   float(0.1522e13)                    ]
