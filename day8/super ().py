# super () in inheritance
#--> to invoke the parent class method
#--> t0 invoke the parent class variable
#--> to invoke the parent class constractor



# to invoke the parent class method
class A:
    def m1(self):
        print("This is method from A")   # A is parent class
class B(A):     # their is mandetory for class mention
    def m2(self):
        print("This is method from B")  # calling the parent class method from child class uses the super() keyword
        super().m1()
# for invoking the parent class method using child class  use  super () keyword
b=B()
b.m2()


# to invoke the parent class variable
class A:
    a,b=100,200   # parent class variable

class B(A):
    i,j=5000,6000    #  child class variable
    def m1(self,x,y):   # local variable
        print(x+y)   #7200
        print(self.i+self.j) #11000
        print(self.a*self.b) #20000
b=B()
b.m1(1200,6000)


# i give same name for all variable   # in that case we use the super() keyword
a,b= 15,20  # these are global variable
class A:
    a,b=100,200   # parent class variable

class B(A):
    a,b=5000,6000    #  child class variable
    def m1(self,a,b):   # local variable
        print(a+b)   #7200   # invoke the local variable
        print(self.a+self.b) #11000 # invoke the child class variable
        print(super().a+super().b)   # invoke the parent class variable
        print(globals()['a']*globals()['b']) # invoke the goble variables

obj2=B()
obj2.m1(1200,6000)



# super() keyword invoke the parent class constractor
class A:
     def  __init__(self):
         print("constractor from A")
class B(A):
    pass
obj1=B()             # if their is B is not having constractor then the directly(automaticaly) invoke the parent class

# class B is also having a constractor
class A:
    def __init__(self):
        print("constractor from A")

class B(A):
    def __init__(self):
        print("Constractor from B" )       # in this case directly invoke the class B
        super().__init__()     # this is 1st approch
        A().__init__()       # this is anther approch
obj1 = B()

