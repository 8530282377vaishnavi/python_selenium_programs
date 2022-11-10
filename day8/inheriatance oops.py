# # oops concept Inheritance
# single inheritance  --> contain only one class and one child
class A:
    def myfun(self):
        print("I love my country")

class B(A):
      def mylife(self):
          print("All indians are my brothers and sisters")


m1=A()
m1.myfun()   # class Ais not access class B function
m2=B()      # but class B can access both class's functions function of A and functions of B
m2.myfun()
m2.mylife()


# Multilevel  Inheritance   ---> Class A<--class B(A)<--class C(B)......
# In multi level inheritance there is
# class A access(call) only class A fun   --> A is main parent superclass
# class B can access(call) both class A as well as self functions meance both  ---> B is child of A
# class c can access (call) class A, class B and self class c function    ---> C is child of B
#this is a multilevel inheritance
class A:
    x,y=11,22
    def mysum(self):
        print(self.x+self.y)
class B(A):
    a,b=200,500
    def mymultiplication(self):
        print(self.a*self.b)
class C(B):
    i,j=900,950
    def mysubsraction(self):
        print(self.i-self.j)
a = A()
a.mysum()

b = B()
b.mysum()
b.mymultiplication()

c = C()
c.mysum()
c.mymultiplication()
c.mysubsraction()

#Hierarical inheritance ---> there is only one parent and many  childs
# class A (parent)<--- class B and class C (child)
class A :
    x,y=400,600
    def fun(self):
        print(self.x*self.y)

class B(A):
    m,n=9000,80000
    def myadd(self):
        print(self.m+self.n)

class C(A):
    i,j=5000,2
    def mydivision(self):
        print(self.i/self.j)

class D(A):
    v,a=2000,6000
    def mysub(self):
        print(self.v-self.a)


a=A()   # class A access(call) only class A fun   --> A is main parent superclass
a.fun()

b=B()   # class B can access only class A and class B's functions
b.fun()
b.myadd()

c=C()  # class c can access only class A and class C's functions
c.fun()
c.mydivision()

d=D()  # class d can access only class A and class D's functions
d.fun()
d.mysub()



#  Multiple inheritance   # it contains multiple parent and single child
# class A :
#     x,y=400,600
#     def fun(self):
#         print(self.x*self.y)
#
# class B:
#     m,n=9000,80000
#     def myadd(self):
#         print(self.m+self.n)
#
# class C(A,B):
#     i,j=5000,2
#     def mydivision(self):
#         print(self.i/self.j)
#
# class D(A,B,C):
#     v,a=2000,6000
#     def mysub(self):
#         print(self.v-self.a)

# super()
# invoke the parent class method
# invoke the parent class variable
# invoke the parent class constractor


# this is invoke the parent class method
class A:
    def myfun(self):
        print("This is method of class A")

class B(A):
    def mydb(self):
        print("This is a method of class B")
        super().myfun()  # using super() there is c calling  parent class
obj=B()
obj.mydb()


# This is invoke the parent class variable








