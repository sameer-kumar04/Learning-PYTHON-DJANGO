from Inheritance2 import Garage
#importing a class from diffferent python file in same directory called Inheritance
class Bike(Garage):
    pass

p1 = Bike()

print(p1.brand)
print(p1.engine)
print(p1.year)