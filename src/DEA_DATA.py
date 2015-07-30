'''
Created on Jul 29, 2015

@author: aeames
'''
T_F_0_5     = [77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77.,
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284., 284., 284., 284.]
#
P_0_5       = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.]
#
A_w_0_5     = [5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257]
#
Loading_0_5 = [0.188, 0.247, 0.294, 0.333, 0.432, 0.502, 0.559, 0.685, 0.78, 0.861,
               1.094, 1.446, 1.921, 3.04, 0.083, 0.121, 0.159, 0.193, 0.285, 0.355,
               0.414, 0.557, 0.658, 0.74, 0.966, 1.2, 1.5, 2.255, 0.01, 0.042, 0.07, 
               0.091, 0.17, 0.231, 0.286, 0.423, 0.522, 0.613, 0.85, 1.066, 1.278,
               1.765, 2.25, 0.032, 0.088, 0.137, 0.18, 0.295, 0.394, 0.48, 0.722, 0.95,
               1.175, 1.6, 1.97, 0.042, 0.083, 0.122, 0.221, 0.31, 0.391, 0.616, 0.815,
               1.02, 1.509, 1.853, 0.02, 0.048, 0.071, 0.16, 0.238, 0.317, 0.52, 0.705,
               0.9, 1.39, 1.78]
#
T_F_2       = [77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77.,
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167.,
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284., 284., 284.]
#
P_2         = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.]
#
A_w_2       = [21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028]
#
Loading_2   = [0.068, 0.111, 0.168, 0.229, 0.396, 0.508, 0.587, 0.738, 0.812, 0.865, 0.95, 1.03, 1.19,
               1.473, 1.76, 0.028, 0.066, 0.1, 0.136, 0.222, 0.31, 0.382, 0.552, 0.66, 0.73, 0.87, 0.936,
               1.002, 1.215, 1.4, 0.005, 0.02, 0.036, 0.055, 0.119, 0.178, 0.23, 0.37, 0.469, 0.546, 0.733,
               0.85, 0.945, 1.107, 1.28, 0.023, 0.054, 0.09, 0.12, 0.202, 0.28, 0.348, 0.533, 0.683, 0.808, 1.03, 
               1.178, 0.02, 0.048, 0.079, 0.14, 0.199, 0.248, 0.413, 0.56, 0.68, 0.927, 1.102, 0.028, 0.046, 0.1,
               0.15, 0.19, 0.326, 0.441, 0.555, 0.808, 1.012]

T_F_3_5     = [77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167.,
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284., 284.]
#
P_3_5       = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300., 
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300., 
               0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               1., 3., 6., 10., 30., 60., 100., 200., 300.]
#
A_w_3_5     = [36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799,
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799,
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799]
#
Loading_3_5 = [0.04, 0.081, 0.13, 0.194, 0.279, 0.361, 0.452, 0.63, 0.707, 0.755, 0.849, 0.94, 
               1.02, 1.155, 1.278, 0.012, 0.038, 0.07, 0.087, 0.154, 0.226, 0.278, 0.417, 0.522, 
               0.62, 0.773, 0.851, 0.92, 1.04, 1.138, 0.02, 0.04, 0.07, 0.109, 0.146, 0.252, 0.338,
               0.423, 0.652, 0.765, 0.83, 0.945, 1.04, 0.02, 0.036, 0.057, 0.078, 0.148, 0.22, 0.282,
               0.465, 0.615, 0.712, 0.84, 0.926, 0.014, 0.031, 0.05, 0.092, 0.134, 0.175, 0.332, 0.479, 
               0.6, 0.747, 0.846, 0.029, 0.055, 0.086, 0.122, 0.246, 0.365, 0.482, 0.653, 0.762]
#
T_F_5       = [77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77.,
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167.,
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284.]
#
P_5         = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300., 
               0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               3., 6., 10., 30., 60., 100., 200., 300.]
#
A_w_5       = [52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57]
#
Loading_5   = [0.02, 0.062, 0.108, 0.152, 0.281, 0.373, 0.444, 0.609, 0.716, 0.779,
               0.87, 0.918, 0.988, 1.14, 1.3, 0.027, 0.05, 0.072, 0.143, 0.203, 0.251,
               0.381, 0.49, 0.58, 0.78, 0.848, 0.89, 1.002, 1.11, 0.017, 0.028, 0.061,
               0.087, 0.114, 0.211, 0.298, 0.379, 0.595, 0.738, 0.805, 0.94, 1.01, 0.01,
               0.024, 0.04, 0.055, 0.112, 0.171, 0.227, 0.415, 0.6, 0.702, 0.811, 0.891,
               0.017, 0.027, 0.061, 0.099, 0.138, 0.283, 0.453, 0.56, 0.692, 0.771, 0.031,
               0.054, 0.08, 0.18, 0.287, 0.431, 0.606, 0.694]
#
#
T_F         = [77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77.,
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284., 284., 284., 284., 
               77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77.,
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167.,
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284., 284., 284.,
               77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167.,
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284., 284., 
               77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77.,
               122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122., 122.,
               167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167., 167.,
               212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
               248., 248., 248., 248., 248., 248., 248., 248., 248., 248.,
               284., 284., 284., 284., 284., 284., 284., 284.]
#
P           = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300., 
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300., 
               0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300., 
               0.03, 0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.06, 0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.1, 0.3, 0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               0.6, 1., 3., 6., 10., 30., 60., 100., 200., 300.,
               3., 6., 10., 30., 60., 100., 200., 300.]
#
A_w         = [5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               5.257, 5.257, 5.257, 5.257, 5.257, 5.257, 5.257,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028, 21.028,
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799,
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799,
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 36.799, 
               36.799, 36.799, 36.799, 36.799, 36.799,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57, 52.57,
               52.57, 52.57]
#
Loading     = [0.188, 0.247, 0.294, 0.333, 0.432, 0.502, 0.559, 0.685, 0.78, 0.861,
               1.094, 1.446, 1.921, 3.04, 0.083, 0.121, 0.159, 0.193, 0.285, 0.355,
               0.414, 0.557, 0.658, 0.74, 0.966, 1.2, 1.5, 2.255, 0.01, 0.042, 0.07, 
               0.091, 0.17, 0.231, 0.286, 0.423, 0.522, 0.613, 0.85, 1.066, 1.278,
               1.765, 2.25, 0.032, 0.088, 0.137, 0.18, 0.295, 0.394, 0.48, 0.722, 0.95,
               1.175, 1.6, 1.97, 0.042, 0.083, 0.122, 0.221, 0.31, 0.391, 0.616, 0.815,
               1.02, 1.509, 1.853, 0.02, 0.048, 0.071, 0.16, 0.238, 0.317, 0.52, 0.705,
               0.9, 1.39, 1.78, 0.068, 0.111, 0.168, 0.229, 0.396, 0.508, 0.587, 0.738, 
               0.812, 0.865, 0.95, 1.03, 1.19,
               1.473, 1.76, 0.028, 0.066, 0.1, 0.136, 0.222, 0.31, 0.382, 0.552, 0.66, 0.73, 0.87, 0.936,
               1.002, 1.215, 1.4, 0.005, 0.02, 0.036, 0.055, 0.119, 0.178, 0.23, 0.37, 0.469, 0.546, 0.733,
               0.85, 0.945, 1.107, 1.28, 0.023, 0.054, 0.09, 0.12, 0.202, 0.28, 0.348, 0.533, 0.683, 0.808, 1.03, 
               1.178, 0.02, 0.048, 0.079, 0.14, 0.199, 0.248, 0.413, 0.56, 0.68, 0.927, 1.102, 0.028, 0.046, 0.1,
               0.15, 0.19, 0.326, 0.441, 0.555, 0.808, 1.012,
               0.04, 0.081, 0.13, 0.194, 0.279, 0.361, 0.452, 0.63, 0.707, 0.755, 0.849, 0.94, 
               1.02, 1.155, 1.278, 0.012, 0.038, 0.07, 0.087, 0.154, 0.226, 0.278, 0.417, 0.522, 
               0.62, 0.773, 0.851, 0.92, 1.04, 1.138, 0.02, 0.04, 0.07, 0.109, 0.146, 0.252, 0.338,
               0.423, 0.652, 0.765, 0.83, 0.945, 1.04, 0.02, 0.036, 0.057, 0.078, 0.148, 0.22, 0.282,
               0.465, 0.615, 0.712, 0.84, 0.926, 0.014, 0.031, 0.05, 0.092, 0.134, 0.175, 0.332, 0.479, 
               0.6, 0.747, 0.846, 0.029, 0.055, 0.086, 0.122, 0.246, 0.365, 0.482, 0.653, 0.762,
               0.02, 0.062, 0.108, 0.152, 0.281, 0.373, 0.444, 0.609, 0.716, 0.779,
               0.87, 0.918, 0.988, 1.14, 1.3, 0.027, 0.05, 0.072, 0.143, 0.203, 0.251,
               0.381, 0.49, 0.58, 0.78, 0.848, 0.89, 1.002, 1.11, 0.017, 0.028, 0.061,
               0.087, 0.114, 0.211, 0.298, 0.379, 0.595, 0.738, 0.805, 0.94, 1.01, 0.01,
               0.024, 0.04, 0.055, 0.112, 0.171, 0.227, 0.415, 0.6, 0.702, 0.811, 0.891,
               0.017, 0.027, 0.061, 0.099, 0.138, 0.283, 0.453, 0.56, 0.692, 0.771, 0.031,
               0.054, 0.08, 0.18, 0.287, 0.431, 0.606, 0.694]