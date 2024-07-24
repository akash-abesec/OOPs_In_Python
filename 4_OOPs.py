"""
Super method:- super() method is used to access methods of the parent class.
Ex :-
"""


class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)


car1 = ToyotaCar("prius", "electric")
print(car1.type)


"""
class method :- A class method is bound to the class & receives the class as an implicit first argument.
 Note :- Static method can't access or modify class state & generally for utility. 
 
 class Student:
    @classmethod       # decorator
    def college(cls):
        pass
        
Ex :-
"""


class Person:
    name = "anonymous"

    def ChangeName(self, name):
        self.__class__.name = "Rahul"


p1 = Person()
p1.ChangeName("rahul kumar")
print(p1.name)
print(Person.name)


class Person:
    name = "Anonymous"

    @classmethod
    def ChangeName(cls, name):
        cls.name = name


p1 = Person()
p1.ChangeName("Rahul kumar")
print(p1.name)
print(Person.name)

"""
Property :- we use property decorator on any method in the class to use the method as a property.
Ex:-
"""


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.math = math
        self.chem = chem

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        @property
        def percentage(self):
            return str((self.phy + self.chem + self.math) / 3) + "%"


std1 = Student(98, 97, 96)
print(std1.percentage())
std1.phy = 86
# print(calcpercentage())
print(std1.percentage())

"""
Polymorphism :- Operator Overloading :- when the same operator is allowed to have different meaning according to the context.
Ex :-  
"""
print(2+3) #3
print("apna" + "college") # apna college
print([1,2 3] + [4, 5, 6]) # merge

"""
Operator & Dunder Functions -
a + b #addition                    a __add__(b)
a - b #subtraction                 a __sub__(b)
a * b #mulitplication              a __mul__(b)
a / b #division                    a __truediv__(b)
a % b #modular                     a __mod__(b)
Ex :-
"""


class Complex :
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i+", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumber()
num2 = Complex(4, 6)
num2.showNumber()
num3 = num1.add(num2)
num3.showNumber()
