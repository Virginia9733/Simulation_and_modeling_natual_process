from math import sin,exp


class Integrator:                             #definisco i numeri che mi interessano (https://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do)
    def __init__(self, xMin, xMax, N):
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
        self.Int = 0.
        ################################


    def integrate(self):
        Deltax = (self.xMax - self.xMin)/(self.N-1)
        for i in range(self.N-1):
            x = self.xMin + i*Deltax
            fx = (x ** 2) * exp(-x) * sin(x)
            self.Int += fx*Deltax

    ##################################

    def show(self):
        print(self.Int)
        print(round((self.Int), 5))

##################################

examp = Integrator(1, 3, 200000)
examp.integrate()
examp.show()