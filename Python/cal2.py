class Calculator:
    def __init__(self): #dunder INT or python class constructor
        print("Hello from constructor")
    def add(self,a,b):
        return a + b

c = Calculator()
# print(c.add(1,2)) # dunder methods (magic methods)

#print(c.add(1,2))