class Person:  #This is the class Person
    #pass (if you want to add any attributes in class , after sometime so by using pass it will not show any error )
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person('Sameer',19,'male')  #p1 is object of Person class
# del p1 #used for deleting any object
print(p1.name)
print(p1.age)
print(p1.gender)