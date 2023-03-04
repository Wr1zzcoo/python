class SimpleCalculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)

    def mul(self):
        print(self.a*self.b)

    def div(self):
        try:
            print(self.a / self.b)
        except:
            print("Exceptin Raised")