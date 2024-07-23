"""
OOPs_Python :- To map real world scenarios, we started using object in code. This is called Object oriented programming.
Procedural - functional - OOPs :- for redundancy decrease anf reusability increase.

Class & Object in Python :- Class is a blueprint for creating objects.
"""

# creating class


# class Students:
#     name = "Karan Kumar"
#
#
# # creating objects (instance)
# s1 = Students()
# print(s1.name)
#
#
# # Ex:-
# class Car:
#     color: "blue"
#     brand: "mercedes"
#
#
# car1 = Car()
# print(car1.color)  # blue
"""
Constructor :- Constructors are generally used for instantiating an object. The task of constructors 
is to initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor and is always called when an object is created.

__init__ Function :- All classes have a function called __init__() which is always executed when the object is being initiated.

"""

# Creating class :-
# class Student:
#     def __init__(self, full_name):
#         self.name = full_name
#
#
# # Creating Object
# s1 = Student("Karan")
# print(s1.name)


"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

"""

# Ex:-
# class Student :
#     def __init__ (self):
#         print(self)
#         print("adding new Student in DataBase...")
#
#
# s1 = Student()
# print(s1)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in database...")
#
#
# s1 = Student("karan", 97)
# print(s1.name, s1.marks)  # karan
# s2 = Student("arjun", 88)
# print(s2.name, s2.marks)

"""
Output :- 
Adding new student in database...
karan 97
Adding new student in database...
arjun 88

"""

# Class & Instance Attributes :-
"""
class.attr
obj.attr
"""

"""
Methods :- Methods are functions that belongs to objects.


# Creating class 
class Student:
    def __init__(self, full_name):
        self.name = full_name

    def Hello(self):
        print("Hello", self.name)


# Creating Object
s1 = Student("karan")
s1.Hello()

# Types of methods :-
1.Instance Method
2.Class Method
3. Static Method
"""


# Example:-
# class Student:
#     college_name = "ABC College"
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def welcome(self):
#         print("Welcome student", self.name)
#
#     def get_marks(self):
#         return self.marks
#
#
# s1 = Student("karan", 97)
# s1.welcome()
# print(s1.get_marks())


