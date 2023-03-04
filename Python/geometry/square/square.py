from polygon.polygon import Polygon
class Square(Polygon):
    def __init__(self, *args):
        self.s
        args=args
        self.length = self.args[0]
      
      
    def __str__(self) -> str:
        if len(self.args) == 0:
            return "Square unintialization"
        elif len(self.args) == 1:
            return "Improper Square initialization"
        else:
            return "Square Initialized"
    
    def Area(self):
        print("Area of the square is : {}".format(self.length * self.length))

    def Perimeter(self):
        print("Perimeter of suare is :{}".format(4*self.length))