def Gretting_Function(name,age):
    print('Hello ' + name + " you are " + str(age) + " years old")

Gretting_Function('Sameer',20)

def Various_Names(*name):
    print('Hello ' + name[0])

Various_Names('Sameer','Sudhir','Harsh','Rohan')