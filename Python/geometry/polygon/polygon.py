class Polygon:
    def __init__(self,*args):
        self.args = args
    
    def __str__(self) -> str:
        print("The total no of polygon sides is : {}".format(len(self.args)))
        if len(self.args) == 1:
            return("It's a sqaure")
        elif len(self.args) == 2:
            return("It's a rectangle")

     