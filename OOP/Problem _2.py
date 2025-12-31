class calculator():
    def __init__(self,n):
        self.n=n
    
    def square(self):
        return self.n*self.n
    def cube(self):
        return self.n*self.n*self.n
    def squareroot(self):
        return (self.n**0.5)
    
a=calculator(9)
print(a.square())
print(a.cube())
print(a.squareroot())

b=calculator(16)
print(b.square())
print(b.cube())
print(b.squareroot())   