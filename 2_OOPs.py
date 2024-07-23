"""
#Create student class that takes name & marks of subjects as arguments in constructor, then create method to print
#the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is :", sum/3)


s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()  # Hi Tony Stark your average score is : 98.0
"""

"""
Static Methods :- Methods that doesn't use the self parameter (work at class level)



class Student:
    @staticmethod  # Decorator
    def college():
        print("ABC college")

# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
# without permanently modifying it.
"""

"""
                                              OOP
                                               |
      ------------------------------------------------------------------------------------------------------
      |                             |                                  |                                   |
Abstraction                   Encapsulation                       Inheritance                       Polymorphism
                            (Data + Method)                            |
                                                                       |
                            ---------------------------------------------------------------------------------- 
                            |                                          |                                     |
                    Single Inheritance                      Multi-level inheritance                  Multiple Inheritance
"""

"""
# Abstraction :- Hiding the implementation details of a class and only showing the essential features to the user.
# Ex- Car system.
# Ex :-
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car Started...")


car1 = Car()
car1.start()   # Car Started...
"""

"""
# Encapsulation :- wrapping data and functions into a single unit(Object).
# Python Program for demonstrating protected members.
class Base1 :
    def __init__(self):
        self._p = 78

class Derived(Base1):
    def __init__(self):
        Base1.__init__(self)
        print("We will call the protected member of base class :", self._p)
        self._p = 433
        print("We will call the modified protected member outside the class :", self._p)

    @property
    def p(self):
        return self._p


obj_1 = Derived()
obj_2 = Base1()
print("Access the protected member of obj_1 :", obj_1._p)
print("Access the protected member of obj_2 :", obj_2._p)


Output :- 
We will call the protected member of base class : 78
We will call the modified protected member outside the class : 433
Access the protected member of obj_1 : 433
Access the protected member of obj_2 : 78
"""


"""
#Create Account class with 2 attributes , balance & account no. Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Credit Method
    def Credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance", self.get_balance())

    # Debit Method
    def Debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.Debit(1000)
acc1.Credit(500)
acc1.Credit(40000)
"""