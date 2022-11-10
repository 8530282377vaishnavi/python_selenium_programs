# two types of variables are local and globle variable
# globle variable ---> the variable which is created out side of function called as a globle variable
# local variable ----> the variable which created inside the function called as local variable

# example 1:
# global_var= 20 # globle variable
#
# def fun():
#     local_var=200 # local variable
#     print (local_var)  # only print inside the function
#     print(global_var)   # run in both inside and outside function
# fun()
#
# print(local_var ) #  this is invalid statement when local variable print out side the function it shows error
# print(global_var) # globle variable is valid in both outside and inside the function

# example 2 :
# xy=100       # this is globle variable
# def fun():
#     xy=200   # this is local variable
#     print(xy)
# fun()
# print(xy)

# example 3 :
# xy=100       # this is globle variable
# def fun():
#     global xy=200 # this is invalid state ment
#     global xy
#     xy=200   # now this is globle variable
#     print(xy) #200
# fun()
# print(xy) # 200 (becoz value is changed)

# example 4:
x=100
#
def fun():
    global x
    x=500
    print (x)
#fun()   # if comment the calling function then direct main x value is print
print (x)

# example 5:
def cool():
    global x
    x=400
    print(x)
cool()
print (x)  #if we use globle funct. inside the function this varible is also global variable
