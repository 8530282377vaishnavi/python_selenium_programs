#OOPs Polymorphism
# overiding and overloading concepts

# some times object comes in many types or forms.
# if we have a button, there are many different draw outputs(round button, check button, button with image) but they do not share the same logic: onclick().
# we access them using the same method. this idea is called polymorphism.
#  one thing behave a different ways

# method overriding
# two name  having a same method but different task
# one of the method overrides the other
#if there is any method in the superclass and a method ith the same name in asubclass, then by exicuting  the method of the corresponding class will be exicuted
# we can override the method as well as variable

#  overriding a variabls
# same method wehich is recreat with in the child class
class parent:
    name="Vaishnavi"
class child(parent):
    name = "Ajinkya"
obj=child()
print(obj.name)

# overriding methods
class __bank:
    def rate_of_intrest(self):
        return 0
class ICICI(__bank):
    def rate_of_intrest(self):
        return 10.5
obj1=ICICI()
print(obj1.rate_of_intrest())

obj2=__bank()
print(obj2.rate_of_intrest())


# overloading concept
# in python you can define a method in such a way there are multiple ways to call it
# give a single method or function , we can specify no. of parameters our self
# single method with different behaviour
class Human:
    def sayHello(self, name=None):
        if  name != None:
            print("Hello" , name)
        else:
            print("Hello")

    def add(self, a=None,b=None):

        if a != None and b!= None:
            return a+b
        else:
            return a

obj3=Human()
obj3.sayHello("Vaishnavi")
obj3.sayHello()
print(obj3.add(1,3))

# example 2
class Birds :
    def fly(self ,name=None):
        if name== 'parrot':
            print("This bird is fly")
        if name== "penguin":
            print("This is not fly")
        if name is None :
            print("No inputs")

    def fly(self ,lastname=None):
        if lastname== 'monkey':
            print("This bird is  fly")
        if lastname== "penguin":
            print("This is not fly")
        if lastname is None :
            print("No inputs")
obj4=Birds()
obj4.fly("monkey")
