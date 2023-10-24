import numpy as np
import numpy.random
import math
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from lrpackage import lrmonte

 
#a = numpy.random.uniform(-1, 1, 10)
#print(a) 
#print(a*2) 
#b = a**2 + a**2 < 0.1
#print(a[b]) 
#print(b) 
#print(b.sum())
#print(len(b)) 

#Define the parameters of the ellipse 

#Inverse cdf method
 

#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.stats import norm
#
# Draw random samples from standard normal distribution
#
#x = np.random.randn(10)
#
# Plot probability distribution function
#
#x_sorted = np.sort(x)
#plt.figure(figsize=(7, 5))
#plt.plot(x_sorted, norm.pdf(x_sorted))
#plt.title("Normal distribution", fontsize=16) 
#plt.show() 
#print(x) 
numpy.random.normal(loc=0.0, scale=1.0, size=None)

#import math
import random

#def sample():
    #mn=0 # Lowest value of domain
    #mx=2*math.pi # Highest value of domain
    #bound=64/(99*math.pi) # Upper bound of PDF value
    #while True: # Do the following until a value is returned
       # Choose an X inside the desired sampling domain.
       #x=random.uniform(mn,mx)
       # Choose a Y between 0 and the maximum PDF value.
       #y=random.uniform(0,bound)
       # Calculate PDF
       #pdf=(((3+(math.cos(x))**2)**2)*(1/(99*math.pi/4)))
       #return x, pdf
       
#x, y = sample(1000) 
#plt.plot(x, y)
#plt.show() 

#a = get_truncated_normal(mean=0, sd=1, low=-math.pi, upp=math.pi)
#a.rvs() 
#print(a)

#from scipy.stats import truncnorm
#array = truncnorm(a=-math.pi/1., b=math.pi/1., scale=3).rvs(size=10e5)
#print(array) 

from scipy.stats import truncnorm

#l = math.pi

#def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    #return truncnorm(
        #(low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

#X = get_truncated_normal(mean=0, sd=1, low=-l, upp=+l)
#z = X.rvs(100)
#plt.hist(z)
#plt.show()
def gauss(x):
    return 1*np.exp(-x**2/2)/np.sqrt(2*math.pi)
    
    
x_1 = lrmonte.RejectionSampling(-math.pi, math.pi, 0.8, 100000)
x, y = x_1.random_generate()
print(x, y) 
z = lrmonte.accept_reject(gauss, x, y) 
print(len(z)) 


v = 1
v0x = []
v0y = []
allArrays_1 = np.array([])
allArrays_2 = np.array([])

N = len(z) 
def initial_condition(z, v):
    for i in range(0, len(z)):
        v0x.append(v*np.cos(z[i]))
        v0y.append(v*np.sin(z[i])) 
    return v0x, v0y 
    
sol_1, sol_2 = initial_condition(z, v)
print(sol_1[5])
print(sol_2[5]) 

# make sure everything is SI
q = 2 # charge assuming it is a alpha particle
B = 1.2 # magnetic field magnitude
E_1 = 1.2 #electric field magnitude
R = 1 #distance of the detector from the source
m = 4 # mass
C = q / m # constant for convenience


#initialZ = [0, 0, v0x, v0y] # = [positionX, positionY, velocityX, velocityY]
def ivf(t, Z) :
    # Z[2] is vx, Z[3] is vy
    dxdt = Z[2]
    dydt = Z[3]
    dvxdt = C * B * Z[3]
    dvydt = C * E_1 - C * B * Z[2]
    return [dxdt, dydt, dvxdt, dvydt]
    
    
def final_value(n, array_1, array_2, arr_1, arr_2):
    for i in range(0, len(z)):
        initialZ = [0, 0, array_1[i], array_2[i]]
        sol = solve_ivp(ivf, [0, 2], initialZ, method='RK45') # 1 microsecond = 1*10^6 
        X = np.array(sol.y[0]) 
        Y = np.array(sol.y[1])
        arr_1 = np.concatenate((arr_1, X)) 
        arr_2 = np.concatenate((arr_2, Y))
    return(arr_1, arr_2) 
  
f_x, f_y = final_value(len(z), sol_1, sol_2, allArrays_1, allArrays_2) 
f_x_1 = np.array(f_x) 
f_y_1 = np.array(f_y) 
print(f_x_1, f_y_1)

    
condition = np.power(f_x_1, 2) + np.power(f_y_1, 2) >= 1 
filtered_array_x = f_x_1[condition]
filtered_array_y = f_y_1[condition]
print(filtered_array_x, filtered_array_y) 
angle = []  
for i in range(0, len(filtered_array_y)):
    if filtered_array_x[i] < 0:
        if filtered_array_y[i] > 0:
            d = math.pi + math.atan(filtered_array_y[i]/filtered_array_x[i])
        else:
            d = - math.pi + math.atan(filtered_array_y[i]/filtered_array_x[i]) 
    else:
        d = math.atan(filtered_array_y[i]/filtered_array_x[i])
    angle.append(d) 
    
plt.hist(angle)
plt.show() 

