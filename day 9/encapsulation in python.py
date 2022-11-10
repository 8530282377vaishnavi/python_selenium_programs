# OOPs encapsulation in python
# in oops , you can restrict access to methods and variable
# this can privent the data from being modified by accident and is known as encapsulation
# encapsulation which is achived by using private variable and private method .
# access specifire concept is main in encapsulation
#public and private - in private their is variable and method and both are start with two underscore (__)
# private variable- Access only their own class
# private variable- access only their own class or method if define


# example private variable can access only with in the method
class Myclass:
    __a=12
    def display(self):
        print(self.__a)
object= Myclass()
object.display()   # this private variable is display becoz. i call this irh in the class


#print(Myclass.__a)  # their is error has to be shown becoz this is private variable can access  only with in the class


# example private method
class myclass:

    def __disp1(self):
        print("this is my disp1 method ")


    def disp2(self):
        print("This is my disp2 method ")
        self.__disp1()
object1=myclass()
#object1.__disp1() #this shows an error

object1.disp2()  # disp2 method is calling private method  __disp1


# Accessing private variables outside of the class   # Modify the private class 

class Myclass:
    __empid=101
    def  getempid(self,eid):
        self.__empid=eid

    def dispempid(self):
        print(self.__empid)
Employee= Myclass()

Employee.getempid(201)

Employee.dispempid()




