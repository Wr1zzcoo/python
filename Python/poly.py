# Abstraction , Encapsulation , Inheritance and Polymorphism
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
# AddSubCalculator is inheriting the features and properties of AdditionCalculator & subtractionCalculator
class AddSubCalculator(AdditionCalculator,SubstractionCalculator):
    def __init__(self):
        print("hello from Calculator")

class CommonCalculator(AdditionCalculator,SubstractionCalculator,MultiplicationCalculator,DivisionCalculaotr):
    def __init__(self):
        print("hello from Calculator")
x = AddSubCalculator()
x.add(1,2)
x.sub(2,1)

y = CommonCalculator()
y.mul(1,2)
y.div(6,2)


class PolyAdditionCalculator(AdditionCalculator):
    def __init__(self):
        print("Hello from PolyAdditionCalculator")
    # Method Overloading (Polymorphism)
    def add(self, *args,binary=False):
        if binary and len(args) == 2:
            return super().add(args[0].args[1])
        else:
            sum = 0
            for i in args:
                sum += 1
            return sum

pa = PolyAdditionCalculator()
print(pa.add(1,2,binary=True))