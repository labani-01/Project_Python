import numpy as np
import numpy.random
import math
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from lrpackage import lrmonte 



q = float(input("Please enter the charge of the particle = ")) # charge assuming it is a alpha particle
B = float(input("Please enter the value of magnetic field in the z direction = ")) # magnetic field magnitude
E_1 = float(input("Please enter the value of electric field in the y direction = ")) #electric field magnitude
R = 1 #distance of the detector from the source
m = float(input("Please enter the mass of the particle = ")) # mass
C = q / m # constant for convenience
v = 1 #magnitude of the initial velocity of the charged particle
s = int(input("Sample size = "))

def gauss(x):
    """ Take x values,
        returns the functional vaule.
    """
    return 1*np.exp(-x**2/2)/np.sqrt(2*math.pi)
    
    
x_1 = lrmonte.RejectionSampling(-math.pi, math.pi, 0.8, s)
x, y = x_1.random_generate()
#print(x, y) 
z = lrmonte.accept_reject(gauss, x, y) # distribution of initial angle that can be thought of as the distribution of initial particles from source"
#print(len(z)) 


v_x = []
v_y = [] 

N_1 = np.array(z) 
N = len(z) # number of particles
print("Number of particles = ", N) 

    
class ComponentVelocity:
    """
    A class to represent the component of initial velocity.
    
    ...
    
    Attributes
    ----------
    z : list
      it has the initial angular distribution of particles.
    v : float
      it is the magnitude of initial velocity which is same for 
      all the particles
      
    Methods
    -------
    __init__(self, z, v):
        construct all the necessary attributes for the object.
    component(self):
        will evaluate the x and y component of velocity and will
        return them.
    """
    
    
    def __init__(self, a_1, a_2):
        self.a_1 = a_1
        self.a_2 = a_2
        
    def component(self):
        x = self.a_1*np.cos(self.a_2)
        y = self.a_1*np.sin(self.a_2) 
        return x, y 


def component_1(z, v):
    """ takes array of initial angle and magnitude of velocity
    returns two arrays of x and y component of velocity.
    """
    
    for i in range(0, N):
        V = ComponentVelocity(v, z[i])
        vx, vy = V.component() 
        v_x.append(vx)
        v_y.append(vy) 
    return v_x, v_y 

#v0x, v0y = component(z, v) 
#print(v0x[5], v0y[5]) 

