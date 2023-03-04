# Create a base class Polygon with basic features and properties like no of sides , write init and str 
# dunders to initialize and print info on the object
# define methods like area , volume , perimeter etc
# Inherit the base class to create like SQAURE , RECTANGLE , QUADILETRAL , PENTAGON , HEXAGON etc
# with respective properties and methods.
class Polygon:
    def __init__(self,sides):
        print("bbesh is gulu")
        self.sides=sides
    def __str__(self):
        return f"This polygon has {self.sides} sides"
    
class rectangle(Polygon):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        super().__init__(4)
    def __str__(self):
        return f"This is rectangle with length {self.l} and breadth {self.b}"
    def area(self):
        print(f"The area of rectangle is ",self.l*self.b)      
    def perimeter(self):
        print(f"The perimeter of rectangle is ",2*(self.l+self.b)) 
        
class square(Polygon):
    def __init__(self,l):
        self.l=l
        super().__init__(4)
    def __str__(self):
        return f"This is square with length {self.l}"
    def area(self):
        print(f"The area of square is ",self.l*self.l) 
    def perimeter(self):
        print(f"The perimeter of square is ",4*(self.l)) 
        
class pentagon(Polygon):
    def __init__(self,side_len,apothem):
        self.side_len=side_len
        self.apothem=apothem
        super().__init__(5)
    def __str__(self):
        return f"This is pentagon with side length {self.side_len}"
    def area(self):
        p=5*self.side_len
        print(f"The area of pentagon is ",(p*self.apothem)/2)
    def perimeter(self):
        print(f"The perimeter of pentagon is ",5*self.side_len) 

class hexagon(Polygon):
    def __init__(self,side_len,apothem):
        self.side_len=side_len
        self.apothem=apothem
        super().__init__(6)
    def __str__(self):
        return f"This is pentagon with side length {self.side_len}"
    def area(self):
        p=6*self.side_len
        print(f"The area of pentagon is ",(p*self.apothem)/2)
    def perimeter(self):
        print(f"The perimeter of pentagon is ",6*self.side_len)                                            
        
p1=Polygon(4)
print(p1) 
print("\n")

p2=rectangle(8,7)
print(p2)
p2.area()
p2.perimeter() 
print("\n")

p3=square(8)
print(p3)
p3.area()
p3.perimeter()
print("\n")

p4=pentagon(12,8)   # here the 1st argument is the side 
                    #length and the second argument is the apothem
print(p4)
p4.area()
p4.perimeter()
print("\n")

p5=hexagon(12,10)   
print(p5)
p5.area()
p5.perimeter()
print("\n")