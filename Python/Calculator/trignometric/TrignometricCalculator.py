import math

class TrignometricCalculator:
    def __init__(self,x): 
        self.x = x
    def sine(self):
        return math.sin(self.x)
    
    def cosine(self):
        return math.cos(self.x)

    def tangent(self):
        return math.tan(self.x)

    def secx(self):
        return 1 / math.cos(self.x)
    
    def cosecx(self):
        return 1 / math.sin(self.x)
    
    def cotangent(self):
        return 1 / math.tan(self.x)