class Employee:
    salary = 50000
    increment = 1.5
    no_of_leaves = 8
    pass

    @property
    def total_compensation(self):
        return self.salary + (self.increment * self.salary) + (self.no_of_leaves * 1000)
    

e=Employee()
print(e.salary)
print(e.total_compensation)