#  Abstract class contains one or more abstract methods
# A abstract method this is a method which is declared but their is not have any implimentations
# Abstract class can not be instantiated and required sub class to provide implimentation fo the abstract method
#sub class of abstract class in python are not required to impliment abstract methods of the parent class .

# ABC is apredefine abstract class
# from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def display(self):
#         None

# class B(A):
#     def display(self):
#         print("This my abstract method")
#
# object1=B()
# object1.display()
#
#
# # example 2
# from abc import ABC
#
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
# class Tiger(Animal):
#     def eat(self):
#         print("Eat NON-VEG")
#
# class Cow(Animal):
#     def eat(self):
#         print(" Eat VEG")
#
# animal=Tiger()
# animal.eat()
#
# animal2=Cow()
# animal2.eat()


# example 2
from abc import ABC, abstractmethod
class X(ABC):
    def m1(self):
        pass
    def m2(self):
        pass
class Y(X):
    def m1(self):
        print("this is m1 method")

yobj=Y()
yobj.m1    # this is not shown any result thir should must have consider abstract class both methods


class Z(Y):
    def m2(self):
        print("This is my m2 method")

zobj=Z()
zobj.m1()
zobj.m2()

# example 3
from abc import ABC, abstractmethod
class A(ABC):
    def __init__(self,value):
        self.value=value
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class B(A):
    def add(self):
        print(self.value + 200)

    def sub(self):
        print(self.value -100)
bobj=B(300)
bobj.add()
bobj.sub()

# why abstract method and class is used ?
#-->you want to secure  class and  method then use abstract class and method
#--> 2nd condition you know the requirement but not know how to impliment this then us abstract


