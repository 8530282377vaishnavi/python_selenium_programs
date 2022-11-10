# Functions : it means a set of statements which will perform task
#*main two things : 1. Function declaration/creation
#                   2. calling a function / invoking the function
#def() ---> is used to create a function / to define the function
#functionname()----> calling a function
#example 1: no arguments no return things
# def myfun():      # this is creation of function and also the define the function
#     print("Hello world")
# myfun()    # this is calling the function


#example 2: single argument no return
# def myfun(name):      # by passing some parameter (argument)
#     print("hello world with", name) # whole code called declaration
# myfun("vaishnavi")


#example 3: two argments and it contain return
# def cal(a,b):
#     return (a+b)
# cal(100,500)
#1st method
#print(cal(100,500)) # directly print the result
#2nd method
# for store the value in variable
# sum=cal(10,20)
# print(sum)
#once you created a function you can call any number of time


#EXAMPLE 4: RETURN none    function does not take argument it not return any value (none)
# def fun():
#     return      # if we not mention in return any thing then the result is  none
# print(fun())

# def fun():
#     i=10
# print(fun())      # if we not mention in return any thing then the result is always none

#BOTH ARE SAME


#example 5:
# def fun(a,b):
#     print(a+b)  # if directly use print after creation their is directly run
# fun(11,20)
#
# def function(c,d):
#     return (c*d)    # in return funct. their is need the print function
# print(function(20,40))

# function does not take argument it not return any value (none)
#function does not take argument it returns some value
# function take argument it not return  value
# function take argument it also returns value

# # the idea is put some commenly and repeatedly done task together and make a function , so that intead of writing same code again and again  for different inputs we can call the function .
# the main advantage of functions is code reusability
# three types  of functions are :
# 1) predefined function
# 2) user defined function
# 3) Anonymous function


# def max_of_three( x, y, z ):
#     if (x > y) and (x > z):
#         return (x)
#
#     elif (y > x) and (y > z):
#         return(y)
#     elif (z > y) and (z > x):
#         return (z)
#     else:
#         return ("no one is maximum no.")
#
# # def max_of_three( x, y, z ):
# #     return max_of_two( x, max_of_two( y, z ) )
# variable=print(max_of_three (3, 6, -5))
#
# # max_of_three ()
# #   if (variable> x):
# #     return x
# #   elif(variable<y) :
# #      return y
# #   else:
# #      return ("no one is maximum no.")


num1= int(input("enter the first number :"))
num2= int(input("enter the second number :"))
num3= int(input("enter the third number :"))
# num1,num2=num2,num1
# print(num1)
# print(num2)

if (num1>num2)  and (num1>num3):
    if (num2>num3):
        print("the second largest value is:",num2)
    else:
        print("the second largest value is:",num3)
elif (num2>num1) and (num2>num3):
    if (num1>num3):
        print("the second largest value is:",num1)
    else:
        print("the second largest value is:",num3)
else:
    if (num1>num2):
        print("the second largest value is:",num1)
    else:
        print("the second largest value is:",num2)








