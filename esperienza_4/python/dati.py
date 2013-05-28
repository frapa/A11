from math import *

# prima serie
temperature = (20.81, 18.14, 16.05, 13.77, 12.44, 10.29, 8.51, 6.7, 4.6,
        2.26, 0.05, 1.89, 3.62, 5.55, 7.68, 9.38, 11.35, 13, 15.01, 17.03, 19.06, 21.03,
        # seconda serie
        23.2, 21.45, 19.73, 17.57, 15.58, 13.27, 11.57, 9.38, 7.5, 5.76, 3.1, 2.5, 4.64,
        6.48, 8.8, 10.56, 12.44, 14.3, 16.24, 18.65, 20.5, 22.42, 23.95)

# prima serie
altezze = (0.98, 0.892, 0.825, 0.727, 0.681, 0.599, 0.529, 0.454, 0.355, 0.285, 0.209, 0.271,
        0.344, 0.416, 0.505, 0.57, 0.645, 0.708, 0.786, 0.857, 0.927, 0.991,
        # seconda serie
        0.98, 0.897, 0.814, 0.721, 0.632, 0.531, 0.463, 0.377, 0.303, 0.242, 0.144, 0.116, 0.201,
        0.267, 0.364, 0.435, 0.51, 0.589, 0.673, 0.783, 0.868, 0.953, 1.03)

# prima serie
pressioni = (96308, 95445, 94788, 93827, 93376, 92572, 91885, 91083, 90112, 89426, 88681, 89289,
        90004, 90710, 91505, 92143, 92878, 93496, 94261, 94957, 95643, 96271, 
        # seconda serie
        97273, 96459, 95645, 94733, 93861, 92870, 92203, 91360, 90634, 90215, 89254, 88980,
        89813, 90460, 91412, 92108, 92572, 93347, 94171, 95249, 96083, 96916, 97671)

h0 = 0.98

theta = temperature
theta1 = temperature[:22]
theta1g = theta1[:11]
theta1s = theta1[11:]
theta2 = temperature[22:]
theta2g = theta2[:11]
theta2s = theta2[11:]

ris_theta = 0.01
dtheta = ris_theta / sqrt(12)

H = altezze
H1 = altezze[:22]
H1g = H1[:11]
H1s = H1[11:]
H2 = altezze[22:]
H2g = H2[:11]
H2s = H2[11:]

h = [dato - h0 for dato in H]
h1 = h[:22]
h1g = h1[:11]
h1s = h1[11:]
h2 = h[22:]
h2g = h2[:11]
h2s = h2[11:]

ris_h = 0.001
dH = ris_h / sqrt(12)
dh = dH * sqrt(2)

p = pressioni
p1 = p[:22]
p2 = p[22:]

# dati fit
A_1 = -0.77568
B_1 =  0.038037

A_2 = -0.98683
B_2 =  0.042153

p_A1 =  8.8634e+04
p_B1 =  372.42

p_A2 =  8.7792e+04
p_B2 =  400.76

A_1r1 = -0.69496
B_1r1 =  0.033530
sA_1r1 =  0.0013622
sB_1r1 =  7.4495e-05

A_1r2 = -0.78154
B_1r2 =  0.038898
sA_1r2 =  2.2201e-04
sB_1r2 =  2.6090e-05

A_2r1 = -1.0508
B_2r1 =  0.045501
sA_2r1 =  8.2565e-04
sB_2r1 =  4.1996e-05

A_2r2 = -0.96070
B_2r2 =  0.038765
sA_2r2 =  3.0893e-04
sB_2r2 =  3.5466e-05

# errori corretti
dh1_corr = 0.0092390
dh2_corr = 0.013388
