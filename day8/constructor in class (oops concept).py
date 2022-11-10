# constructor in class ---> constructor is a special type of subroutine called to create an object.
# a special type of method used to initialize an object  (__init__(self):)
# __init__() (constractor)    ---. invoke at the time of object creator
 # example 1:
class Studant:
    def m1(self):
        print("good morning")
    def __init__(self):
        print("my name is vaishnavi")

mc1=Studant()
mc1.m1()

#example 2
class Employee:
    def __init__(self, aname, asalary, arole):
        self.name= aname
        self.salary= asalary
        self.role= arole



vaishnavi=Employee("vaishnavi", 900000, "Atomation test Engineer ")
print(vaishnavi.name)

# example 3
class myclass:
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2  # this is conversion of local variable tho class variable

    def add(self):
      print(self.val1+self.val2)

mc=myclass(100,200)
mc.add()

# how to call currunt class method in another method
class myclass:
    def m1(self):
        print("this is my no.")
        self.m2(8530282377)
    def m2(self,a):
        print("this is my no.=", a)
m3=myclass()
m3.m1()


# constractor with argument
class myclass:
    name="vaishnavi"
    def __init__(self, name ):
        print(name)      # constactor woth lacal  variable argument
        print(self.name) # its represents the class variable  (for class variable always use self. keyword)
c1=myclass("ajinkya ")


# requirement   -->  class-employee , constractor- accept eid, ename, sal , print-eid ,ename ,sal
class Empoyee:
    def __init__(self,eid,ename,sal):
        self.eid=eid    # assining the value of local variable to class variable
        self.ename=ename
        self.sal=sal
vaishu=Empoyee(" 12 ", "Vaishanvi", "10,00000")
print(vaishu.ename, vaishu.eid, vaishu.sal)

# another method
class Emp:
    def __init__(self,ename,eid,sal):
        self.ename = ename
        self.eid = eid
        self.sal = sal
    def display(self):
        print("Empname:{} Empid: {} Empsal: {}" .format(self.ename, self.eid, self.sal))
        print("Empname:%s Empid: %d Empsal: %d" %(self.ename, self.eid, self.sal))
c1=Emp("Vaishanvi", 77, 1000000)
c2=Emp("Ajinkya", 76, 1300000.0)
c1.display()
c2.display()


#__str__ constractor  --> execute automatically when you print referance variable
# __str-- constractor is automaticaly invoke at the time when we print the the referance variable (object)
# it return only string value
# __str__--> which is invoke whenever you print the referance variable
class myclass:
    pass
c1=myclass()  # c1 object is nothing but referance variable
print(c1)  #  this showas the location of object

# overriding method meance __str__ method is always executed bydefault when you printing the referance variable but in
# overriding concept we are directly call the __str__(self) constractor then what we print under the __str__ constractor this is directly overiding on referance variable print statement
class Vaishanvi:
    def vaishu(self):
        return ("Rupali")
    def __str__(self):
        return("welcome")  # str is overriding the vaishu def function   # and main __str__ returns only string
m1=Vaishanvi()
print(m1)

# another example __str__
class Emp:
    def __init__(self,ename,eid,sal):
        self.ename = ename
        self.eid = eid
        self.sal = sal
    def __str__(self):
        return("Empname:{} Empid: {} Empsal: {}" .format(self.ename, self.eid, self.sal))
c1=Emp("Vaishanvi", 77, 1000000)
print(c1)     # their is no need to calling other method


#__del__ which is invoke when you distroying the object

class Ajinkya:
    def __del__(self):
        print("destroy")
w1=Ajinkya()
del w1  # the del function is used to delet the object
