import numpy as np
import numpy.random
import math
 

class RejectionSampling:

    def __init__(self, xmin, xmax, pmax, N):
        self.xmax = xmax
        self.xmin = xmin
        self.N = N
        self.pmax = pmax
        
    def random_generate(self):
        x = np.random.uniform(self.xmin, self.xmax, self.N)
        y = np.random.uniform(0, self.pmax, self.N) 
        return(x, y) 
        

#x_1 = RejectionSampling(-math.pi, math.pi, 100000)
#x, y = x_1.random_generate() 
#print(x, y) 
        
    
def accept_reject(func, x, y):
    mask = y<func(x) 
    #plt.scatter(x[mask], y[mask], s=0.1)
    #plt.show() 
    #plt.hist(x[mask]) 
    #plt.show() 
    #print(x[mask]) 
    return(x[mask]) 
    
#accept_reject(gauss, x, y) 
