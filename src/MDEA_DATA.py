'''
Created on Jul 30, 2015

@author: aeames
'''
T_F     = [103.874, 103.892, 103.928, 103.964, 103.964, 103.946, 103.982, 103.946,
           103.928, 104.216, 104.18, 104.072, 104.18, 77., 77.018, 77.018, 77., 77.036,
           76.964, 76.64, 77.018, 77.018, 79.142, 77.018, 77.036, 76.964, 77.018, 77.036,
           77., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104.,
           104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 212.,
           212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 212., 104., 104.,
           104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104.,  77., 
           77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 77., 104., 104., 104., 104.,
           104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 104., 158., 158.,
           158., 158., 158., 158., 158., 158., 158., 158., 158., 158., 158., 158., 158.,
           158., 158., 158., 158., 212., 212., 212., 212., 212., 212., 212., 212., 212.,
           212., 212., 212., 212., 212., 212., 248., 248., 248., 248., 248., 248., 248., 
           248., 248., 248., 248., 248., 100., 100., 100., 100., 100., 100., 100., 100., 
           100., 100., 150.08, 150.08, 150.08, 150.08, 150.08, 150.08, 150.08, 150.08, 
           150.08, 150.08, 150.08, 150.08, 150.08, 150.08, 150.08, 240.08, 240.08, 240.08,
           240.08, 240.08, 240.08, 240.08, 240.08, 240.08, 240.08, 240.08, 240.08, 240.08,
           240.08, 240.08]

P       = [0.00580151, 0.016389264, 0.032488453, 0.051488397, 0.073824209, 0.128648474,
           0.196091022, 0.233655796, 0.026541906, 0.042205982, 0.060335699, 0.106602737,
           0.163602568, 0.00449617, 0.009572491, 0.025526642, 0.047717416, 0.061350963,
           0.095869945, 0.137060662, 0.185358229, 0.212915399, 0.003335868, 0.007106849,
           0.010297679, 0.018709868, 0.031618227, 0.06990819, 0.158236172, 0.000265419, 
           0.000350991, 0.000797708, 0.002045032, 0.004423651, 0.009891574, 0.014068661,
           0.025816717, 0.042786133, 0.064541793, 0.094419567, 0.087747831, 0.150259097,
           0.204358173, 0.262953419, 0.33083108, 0.375502704, 0.490372592, 0.477174158, 
           2.581671736, 6.555705758, 12.48774924, 14.93888701, 45.39681199, 0.079915794,
           0.170419342, 0.328220401, 0.518945027, 0.580150952, 1.331591473, 2.12045173,
           3.161822688, 3.227089671, 9.534780896, 15.21445872, 43.75788555, 0.009079362,
           0.014793849, 0.030457925, 0.052358623, 0.093404303, 0.158671285, 0.194060493,
           0.265419061, 0.301243382, 0.34431959, 0.444105554, 0.583631858, 0.70531852,
           0.85151656,  0.001368521, 0.002565587, 0.004990894, 0.009708884, 0.023577045, 
           0.042596278, 0.139037672, 0.35035461, 0.790168497, 1.782093191, 6.035963023,
           12.18408373, 0.000878195, 0.00147354, 0.003578357, 0.008070378, 0.019598079,
           0.053174171, 0.096068647, 0.15534557, 0.313575941, 0.437359849, 1.062086699,
           2.67630886, 6.035963023, 17.63368819, 25.52084038, 0.000249872, 0.000468441, 
           0.000878195, 0.00190874, 0.003323322, 0.005178848, 0.009708884, 0.018201366,
           0.03674096, 0.063970055, 0.124442089, 0.224827349, 0.437359849, 0.850804425,
           1.595023516, 2.777095585, 6.26328067, 11.74189267, 29.58784359, 0.007495202,
           0.013541434, 0.02836387, 0.051244298, 0.096068647, 0.193922708, 0.313575941,
           0.707219965, 1.655083643, 4.17057466, 5.816912528, 9.760285571, 24.59448435,
           61.97477049, 93.07231189, 0.068879002, 0.111378685, 0.167266222, 0.30219628,
           0.632979498, 1.231345739, 1.782093191, 2.777095585, 6.74392123, 10.50927495,
           16.37693619, 27.47913992, 1.590846429, 2.381273094, 3.780408641, 4.548107892,
           5.754676834, 8.121866764, 10.99114833, 14.62618565, 19.46333925, 22.83285598,
           1.590846429, 1.701466712, 1.819788499, 2.081683142, 2.361344909, 3.564447449,
           4.111834376, 4.823679594, 5.471708208, 7.100061396, 9.936825506, 14.87405515,
           22.45242199, 29.87791907, 42.88287288, 1.590846429, 2.046990115, 2.817096993,
           4.077431425, 5.073144504, 6.154864961, 7.404742172, 9.853660867, 14.14268785,
           23.02561113, 25.68357272, 37.4877591, 59.51406022, 97.71206913, 137.9059423]

A_w     = [23.63, 23.63, 23.63, 23.63, 23.63, 23.63, 23.63, 23.63, 23.63, 23.63, 23.63, 
           23.63, 23.63, 11.83, 11.83, 11.83, 11.83, 11.83, 11.83, 11.83, 11.83, 11.83, 
           11.83, 11.83, 11.83, 11.83, 11.83, 11.83, 11.83, 35., 35., 35., 35., 35., 35.,  
           35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35.,
           35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35., 35.,
           50., 50., 50., 50., 50., 50., 50., 50., 50., 50., 50., 50., 50., 50., 48.8, 
           48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 
           48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 
           48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 
           48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8,
           48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 
           48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 48.8, 20., 20., 20., 20., 20., 20., 20., 
           20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 
           20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20., 20.]

Loading = [0.0151, 0.0301, 0.0452, 0.0601, 0.0754, 0.1049, 0.1346, 0.1494, 0.0356, 0.0497,
           0.0638, 0.092, 0.1201, 0.0101, 0.0202, 0.0606, 0.101, 0.1208, 0.161, 0.2011,
           0.2411, 0.261, 0.0154, 0.0233, 0.0308, 0.0463, 0.077, 0.1384, 0.2299, 0.0041,
           0.00478, 0.00671, 0.0108, 0.0158, 0.0247, 0.0324, 0.0425, 0.0507, 0.073, 0.0746,
           0.0883, 0.1008, 0.125, 0.145, 0.1616, 0.1755, 0.2123, 0.215, 0.473, 0.664, 0.83,
           0.869, 1.077, 0.021, 0.03, 0.033, 0.044, 0.053, 0.065, 0.104, 0.143, 0.153, 0.279,
           0.334, 0.548, 0.022, 0.0233, 0.0294, 0.0369, 0.053, 0.0757, 0.0863, 0.1015, 0.1106,
           0.121, 0.1463, 0.1719, 0.1945, 0.214, 0.01, 0.0140456, 0.0202307, 0.0295084, 0.0488118,
           0.0694273, 0.125418, 0.180647, 0.25373, 0.356379, 0.596975, 0.777518, 0.0053306,
           0.00703063, 0.0119262, 0.0187596, 0.0306435, 0.0513313, 0.0711966, 0.0939026, 0.133562,
           0.157297, 0.244331, 0.370089, 0.500557, 0.739354, 0.849106, 0.00140456, 0.0019728, 
           0.00270205, 0.00414464, 0.00574861, 0.00739354, 0.0103847, 0.0145859, 0.021275, 0.0287751,
           0.0414464, 0.0567673, 0.0807428, 0.117771, 0.161306, 0.215443, 0.306435, 0.409281, 0.604534,
           0.00470036, 0.00643788, 0.00962956, 0.0133562, 0.0187596, 0.0284153, 0.0370089, 0.0589511,
           0.0950916, 0.147706, 0.176158, 0.220934, 0.338887, 0.53306, 0.677019, 0.0105162, 0.0136966,
           0.017178, 0.0241276, 0.0370089, 0.0539809, 0.065194, 0.0849106, 0.133562, 0.163348, 
           0.202307, 0.260196, 0.679178, 0.742095, 0.809634, 0.832677, 0.860337, 0.89571, 0.923415,
           0.946525, 0.968107, 0.978909, 0.482065, 0.494333, 0.506602, 0.529612, 0.555671, 0.627761,
           0.652304, 0.676859, 0.699862, 0.741292, 0.791939, 0.845687, 0.894857, 0.924079, 0.957935,
           0.133678, 0.182741, 0.244074, 0.316136, 0.356009, 0.39281, 0.426549, 0.478691, 0.546163,
           0.636639, 0.655048, 0.721004, 0.799239, 0.880553, 0.93579]