class Employee:
    a = 1

class Programmer:
    b = 2

class Manager:
    c = 3


class Staff(Employee, Programmer, Manager):
    pass

o = Staff()
print(o.a)            
print(o.a, o.b)       
print(o.a, o.b, o.c)  
