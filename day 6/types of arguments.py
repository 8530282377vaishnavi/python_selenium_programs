# types od arguments •	two types of argument / parameters can pass to the function
# 1.Positional argument
# 2. keyword argument
# #example 1 :
# def fun(i,j):
#     print(i,j)
# fun(10,20) # this is positional argument
# fun(i=10, j=20) # this is keyword argument  (when we specify any kay word this is key word argument )
#
#
# # example 2: default value assigned the positional argument
# def fun (i,j=200):
#     print(i,j)
# fun(100,20) #100 20
# fun(100) # 100,200

# example 3:
# keyword argument
def greating(name, greatmsg):
    print(name,greatmsg )
greating(name='vaishnavi', greatmsg='hello')
greating( greatmsg='hello',name='vaishnavi')

# example 4:
def cal(a,b,c):
    print(a,b,c)
cal(10,20,30) # 10,20,30 positional argument
cal(a=10,b=20, c=30) # 10,20,30 # keyword argument
cal(b=20, a=10, c=30) # 10,20,30 #keyword argument

# cal(10,b=20, c=30)
cal(10,20, c=30)
# cal(a=10,b=20,30)    # this is give an error becoz the main reson is the positional argument never appear before keyeord argument
# #SyntaxError: positional argument follows keyword argument
# cal(a=10,30,b=20) # it also shows error
#
