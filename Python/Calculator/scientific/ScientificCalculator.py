import math

class ScientificCalculator:
    def __init__(self,x):
        self.x = x
    def square(self):
        return self.x * self.x

    def cube(self):
        return self.x ** 3

    def squareRoot(self):
        return math.sqrt(self.x)
    
    def cubeRoot(self):
        return self.x ** (1/3)
    
    
