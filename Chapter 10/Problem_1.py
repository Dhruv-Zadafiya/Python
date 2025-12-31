class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return TwoDVector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"TwoDVector({self.x}, {self.y})"
    
class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __add__(self, other):
        return ThreeDVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f"ThreeDVector({self.x}, {self.y}, {self.z})"
    
v1 = TwoDVector(1, 2)
v2 = TwoDVector(3, 4)

v3 = v1 + v2
print(v3)  

v4 = ThreeDVector(1, 2, 3)
v5 = ThreeDVector(4, 5, 6)

v6 = v4 + v5
print(v6) 
