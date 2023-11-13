import numpy as np
import numpy.random
import math
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from lrpackage import lrmonte 
import initial_condition
 


q = initial_condition.q
B = initial_condition.B
m = initial_condition.m
C = initial_condition.C
v = initial_condition.v
R = initial_condition.R
E_1 = initial_condition.E_1
N = initial_condition.N

#initialZ = [0, 0, v0x, v0y] # = [positionX, positionY, velocityX, velocityY]

def ivf(t, Z) :
    """ This function takes time and Z array
    Z = [positionX, positionY, velocityX, velocityY] 
    returns time derivative of each of them.
    """
    
    # Z[2] is vx, Z[3] is vy
    dxdt = Z[2]
    dydt = Z[3]
    dvxdt = C * B * Z[3]
    dvydt = C * E_1 - C * B * Z[2]
    return [dxdt, dydt, dvxdt, dvydt]
    
 


    
def final_value(n, array_1, array_2, arr_1, arr_2):
    """ This function takes positionX, positionY, velocityX, velocityY, length arrays
    and solve the ODE using the fucntion ivf.
    returns x and y values of the trajectroy for the given time span.
    """
    
    for i in range(0, n):
        initialZ = [0, 0, array_1[i], array_2[i]]
        sol = solve_ivp(ivf, [0, 2], initialZ, method='RK45')  
        X = np.array(sol.y[0]) 
        Y = np.array(sol.y[1])
        arr_1 = np.concatenate((arr_1, X)) 
        arr_2 = np.concatenate((arr_2, Y))
    return(arr_1, arr_2) 
  


