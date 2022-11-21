# Pyhton object oriented programming
#  Almost everything in Python is oobject with properties and methods 
# Class = Blueprint 

# class Person: 
#     X = 5
# P1 = Person()
# print(P1.X)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def greeting(self,):
#          print("Heloo my name is " + self.name)
# p1 = Person("Abdi", 30)
# print(p1.name, p1.age)
# p1.greeting()

# p1.age = 31
# del p1.age
# print(p1.age)

# Subclasss/Parent*child class/Inheretance

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, gradyear):
#         super().__init__(name, age)
#         self.gradyear = gradyear

# def welcome(self):
#                 print("Congradulations" + self.name + "Welcome to the class of " + self.gradyear)
# student1 = Student("Ali", 25, 2002)
# student1.welcome()

class Person: 
    def __init__(self, name, age):
            self.name = name
            self.age = age

class Student(Person):
        def __init__(self, name, age, year):
            super().__init__(name, age)
            self.graduationyear = year

        def welcome(self):
            print("Welcome", self.name, self.age, "to the class of", self.graduationyear)

stuent1 = Student("Bhavya",12, 2020)
stuent2 = Student("Ali", 25,2021)
stuent2.welcome()