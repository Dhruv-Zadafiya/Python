class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    def __mul__(self, other):
        return complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)
    def __repr__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = complex(2, 3)
c2 = complex(4, 5)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)
print(isinstance(c1, complex))
print(issubclass(complex, object))
print(issubclass(object, complex))
print(issubclass(complex, int))
