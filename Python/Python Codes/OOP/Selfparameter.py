class Employee:
    name = "Dhruv"
    age = 21   # this is class attribute
    salary = 50000
    designation = "Developer"
    location = "Surat"
    Experience = "Fresher"

    def getinfo(self):
        print(f"This location is {self.location}. This salary is {self.salary}")

    def greet(self):
        print("Hello", self.name)  # this is object attribute

    def __init__(self):
        print("This is constructor")


Object = Employee()
Object.id = 101
Object.name = "Raj"
Object.dob = "01/01/2000"

print(Object.name, Object.age, Object.salary, Object.designation, Object.location, Object.Experience, Object.id, Object.dob)

Object.getinfo()
Employee.getinfo(Object)  

Object.greet()
Employee.greet(Object)  
# Here name is object attribute and age and salary are class attribute as they directly belong to the class

Object.__init__()  # Dunder method it is called by directly