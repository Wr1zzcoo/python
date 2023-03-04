class bulb:  
    def glow(self):  
        print("1.bulb is used to light the house.")

class tv:
    def watch(self):
        print("2.tv is used for entertainment.")

class vaccumcleaner:
    def clean(self):
        print("3.vaccumcleaner is used for cleaning.")

class charger:
    def charge(self):
        print("4.charger is used to charge devices.")

class electronic_device(bulb,tv,vaccumcleaner,charger):
    def __init__(self):
        print("")
        print("There are many type of electronic device")
        

a=bulb()
a.glow()
b=tv()
b.watch()
c=vaccumcleaner()
c.clean()
d=charger()
d.charge()
e=electronic_device()
e.glow()
e.charge()
e.clean()
e.watch()