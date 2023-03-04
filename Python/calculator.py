class AdditionCalculator:
    #Dunder INIT or python class constructor
    def __init__(self):
        print("hello from calculator")
    def add(self,a,b):
            print(a + b)

class SubstractionCalculator:
    def sub(self,a,b):
        print(a - b)    
class MultiplicationCalculator:
    def mul(self,a,b):
        print(a * b)

class DivisionCalculaotr:
    def div(self,a,b):
        if b == 0:
            print("Denominator is ZERO")
        else:
            print(a / b)
a = AdditionCalculator()
a.add(1,2)
b = SubstractionCalculator()
b.sub(2,1)
c = MultiplicationCalculator()
c.mul(1,2)
d = DivisionCalculaotr()
d.div(4,2)


    