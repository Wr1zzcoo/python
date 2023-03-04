class Person:
    def __init__(self,gender):
        self.sex = gender
    def __str__(self):
        return "Person is a {}".format(self.sex)
    def cry(self):
        print("Crying!")

a = Person("male")
print(type(a))
# a.cry()
b = Person("female")
print(type(b))
# b.cry()