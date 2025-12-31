class employee():
   def show(self):
       print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class programmer(employee):
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
        print(f"The language is {self.language}")

    def showLanguage(self):
        print(f"The language is {self.language}")


a=employee()
a.name="Dhruv"
a.salary=50000
a.show()

b=programmer()
b.name="Amit"
b.salary=60000
b.language="Python"
b.show()
b.showLanguage()

print(issubclass(programmer, employee))
print(issubclass(employee, programmer))  