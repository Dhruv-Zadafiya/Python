a= lambda x: x**3
a(4)

x=lambda age : 'adult' if age>18 else 'child'
x(19)

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7)) 

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

names = ["dhruv", "alex", "john"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)


nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)



data = [(1, 3), (4, 1), (2, 5)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)


marks = {"Math": 80, "Sci": 95, "Eng": 70}
sorted_marks = sorted(marks.items(), key=lambda x: x[1])
print(sorted_marks)


def power(n):
    return lambda x: x ** n

square = power(2)
cube = power(3)

print(square(4)) 
print(cube(2))    


nums = [1, 2, 2, 3, 4, 3, 5]
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print(unique)


def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

print(is_palindrome("madam"))
print(is_palindrome(12321))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)


text = "Hello Python"
vowels = "aeiouAEIOU"

v = c = 0
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "scored", self.marks)

s1 = Student("Dhruv", 90)
s1.display()



