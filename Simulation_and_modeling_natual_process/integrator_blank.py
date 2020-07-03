

import numpy as np
import math

class Integrator:
    def __init__(self, xMin, xMax, N):
        ################################
        self.Min = xMin
        self.Max = xMax
        self.N = N

    def integrate(self):       
        ##################################

        delta_x = (self.Max - self.Min) / (self.N-1)
        self.S = 0
        for i in range(self.N-1):
            x = self.Min + i*delta_x
            f = (x**2)*(np.exp(-x))*(np.sin(x))
            self.S += f*delta_x

    def show(self):
        ##################################
        print(self.S)
        print(round((self.S), 5))
        

examp = Integrator(1,3,200000)
examp.integrate()
examp.show()
