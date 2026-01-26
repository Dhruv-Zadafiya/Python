
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()   
d.bark()    

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show_details(self):
        print("Roll No:", self.roll)

s = Student("Dhruv", 101)
s.show_name()
s.show_details()


# Multilevel inheritence


class Grandfather:
    def house(self):
        print("Grandfather owns a house")

class Father(Grandfather):
    def car(self):
        print("Father owns a car")


class Son(Father):
    def bike(self):
        print("Son owns a bike")


s = Son()
s.house()   
s.car()     
s.bike()   

