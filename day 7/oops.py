#class and object reffered in nootbook
# Example 1:
# a)
# class Myclass:
#     def myfun(self):
#         pass
#     def display(self):
#         print("vaishnavi")
# mc1=Myclass()
# mc1.myfun()  # mc1 is an object
# mc1.display()

#b)
# class myclass:
#     def myfun(self):
#         print("hello world")
#     def display(self, name):
#         print(name)
#
# mc1=myclass()
# mc1.myfun()   # myfun() is an method
# mc1.display("ajinkya")


#  python code with harry
# class Studant :
#     pass
# Vaishnavi= Studant()
# Rupali= Studant()
#
# Vaishnavi.name= "Vaishnavi"
# Vaishnavi.std= 12
# Vaishnavi.section= 1
#
# Rupali.name="Rupali"
# Rupali.std=12
# Rupali.section= 1
# print(Rupali.section, Vaishnavi.std)


#
# # instance and variable  (we cant change class variable using instance )
# class Employee:
#     no_of_leaves = 8
#     pass
# ajinkya= Employee()
# vaishnavi= Employee()
#
#
# ajinkya.name= "Ajinkya"
# ajinkya.salary= 1200000
# ajinkya.role= "Software Developer"
#
# vaishnavi.name= "vaishnavi"
# vaishnavi.salary= 900000
# vaishnavi.role = "Automation Test Engineer"
# print(vaishnavi.salary)
# print(vaishnavi.no_of_leaves)
# print(ajinkya.__dict__)
# Employee.no_of_leaves=10
# print(Employee.no_of_leaves)
# ajinkya.no_of_leaves=7
# print(ajinkya.__dict__)
# print(ajinkya.no_of_leaves)

# self and __init__() (constractor)
# class Employee:
#
    # def printdetail(self):
    #     return f"name is {self.name}. salary is {self.salary} and role is {self.role}"

#     no_of_leaves = 8
#     pass
# ajinkya= Employee()
# vaishnavi= Employee()
#
#
# ajinkya.name= "Ajinkya"
# ajinkya.salary= 1200000
# ajinkya.role= "Software Developer"
#
# vaishnavi.name= "vaishnavi"
# vaishnavi.salary= 900000
# vaishnavi.role = "Automation Test Engineer"
#
# print(vaishnavi.printdetail())
# print(ajinkya.printdetail())

# __init__() (constractor)
class Employee:
    def __init__(self, aname, asalary, arole):
        self.name= aname
        self.salary= asalary
        self.role= arole



vaishnavi=Employee("vaishnavi", 900000, "Atomation test Engineer ")
print(vaishnavi.name)





# class methods in python
