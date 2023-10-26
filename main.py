import numpy as np
import numpy.random
import math
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from lrpackage import lrmonte
import random
import initial_condition
import trajectroy



q = initial_condition.q
B = initial_condition.B
m = initial_condition.m
C = initial_condition.C
v = initial_condition.v
R = initial_condition.R
E_1 = initial_condition.E_1
N = initial_condition.N
v0x = []
v0y = []
allArrays_1 = np.array([])
allArrays_2 = np.array([])

theta = initial_condition.z
#theta_1 = sns.histplot(theta, kde=True, stat="density", linewidth=0)
plt.hist(theta) 
plt.show() 
 
    
sol_1, sol_2 = initial_condition.component_1(theta, v) #stores initial velocities
 
    
    
f_x, f_y = trajectroy.final_value(N, sol_1, sol_2, allArrays_1, allArrays_2) #storing the x and y values from the trajectory for each particle after solving the ODE
f_x_1 = np.array(f_x) # have assigned it as np.array. If we don't do so then the next comparison cannot be done.
f_y_1 = np.array(f_y) 
#print(f_x_1, f_y_1)


condition = np.power(f_x_1, 2) + np.power(f_y_1, 2) >= 1 #Length of the detector is 1, so this condition checks for which x, y radius is grater that 1
filtered_array_x = f_x_1[condition]
filtered_array_y = f_y_1[condition]
#print(filtered_array_x, filtered_array_y) 
angle = []  
for i in range(0, len(filtered_array_y)): #this loop helps to evaluate the final angle for each quadrants.
    if filtered_array_x[i] < 0:
        if filtered_array_y[i] > 0:
            d = math.pi + math.atan(filtered_array_y[i]/filtered_array_x[i])
        else:
            d = - math.pi + math.atan(filtered_array_y[i]/filtered_array_x[i]) 
    else:
        d = math.atan(filtered_array_y[i]/filtered_array_x[i])
    angle.append(d) 
    
 
#phi_1 = sns.histplot(angle, kde=True, stat="density", linewidth=0)
plt.hist(angle)  
plt.show() 
 
