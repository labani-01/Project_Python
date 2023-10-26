import numpy as np
import numpy.random
import math
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from lrpackage import lrmonte 
 
q = 2 # charge assuming it is a alpha particle
B = 1.2 # magnetic field magnitude
E_1 = 1.2 #electric field magnitude
R = 1 #distance of the detector from the source
m = 4 # mass
C = q / m # constant for convenience
v = 1 #magnitude of the initial velocity of the charged particle

def gauss(x):
    return 1*np.exp(-x**2/2)/np.sqrt(2*math.pi)
    
    
x_1 = lrmonte.RejectionSampling(-math.pi, math.pi, 0.8, 100000)
x, y = x_1.random_generate()
print(x, y) 
z = lrmonte.accept_reject(gauss, x, y) 
print(len(z)) 


v_x = []
v_y = [] 

N = len(z) 
 
    
class ComponentVelocity:
    
    def __init__(self, a_1, a_2):
        self.a_1 = a_1
        self.a_2 = a_2
        
    def component(self):
        x = self.a_1*np.cos(self.a_2)
        y = self.a_1*np.sin(self.a_2) 
        return x, y 


def component(z, v):
    for i in range(0, N):
        V = ComponentVelocity(v, z[i])
        vx, vy = V.component() 
        v_x.append(vx)
        v_y.append(vy) 
    return v_x, v_y 

#v0x, v0y = component(z, v) 
#print(v0x[5], v0y[5]) 

