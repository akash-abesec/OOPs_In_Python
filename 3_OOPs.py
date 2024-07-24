"""
del keyword :- Used to delete object properties or object itself.
Ex:-
"""
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Akash")
print(s1.name)
print(s1)
del s1.name
del s1


"""
# Private (like) Attributes and Methods :-
Private attributes & Methods are meant to be used only within the class and are not accessible from outside the class
"For making private we add two "__" before the attributes"
Ex:-Public
"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.acc_pass)


# Ex:-Private
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12345", "ABCDE")
print(acc1.acc_no)
print(acc1.reset_pass())


class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def Welcome(self):
        self.__hello()


p1 = Person()
print(p1.Welcome())


"""
# Inheritance :- When one class(child/derived) derives the properties & method of another class(parent/base).
Ex:-
"""

class Car:
    @staticmethod
    def Start():
        print("Car started...")

    @staticmethod
    def Stop():
        print("Car Stopped...")


class Toyota_car(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyota_car("Fortune")
car2 = Toyota_car("Prius")
print(car1.name)  # Fortune
print(car1.Start())
print(car2.Stop())


"""
# 1.Single Inheritance :- Above example
               Base(Parent)
                |
              Derived(Child)
"""

"""
# 2.Multi-Level Inheritance :-
            Base(Parent)
                |
            Derived(parent/Child)
                |
            Derived(child)
            
Ex:-
"""


class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("car stopped...")

    
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortune(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortune("Diesel")
car1.start()


"""
# 3.Multiple Inheritance :-
               (Parent1)          ( Parent2)
                 \                  /
                  \                /
                   \              /
                       (Derived)

Ex:-
"""


class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):
    varC = "Welcome to class C"


c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


