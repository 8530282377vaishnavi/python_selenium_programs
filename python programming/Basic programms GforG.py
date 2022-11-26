#add a two numbers
# def sum(a,b):
#     print (a+b)
# a=int(input("enter firs no.:"))
# b=int(input("enter second no.:"))
# sum(a,b)
# sum=a+b
# print(sum)
# print(a+b)

# find the maximum of two numbers
# def max_no(c,d):
#     if c>d:
#         print("The maximum number is",c)
#     elif d>c:
#         print("The maximum number is",d)
# c=int(input("enter first no.:"))
# d=int(input("enter second no.:"))
# max_no(c,d)


# find the simple interest
# def simple_interst(p,r,t):
#
#     SI=p*r*t/100
#     return ("the simple interest is",SI)
# p=1000
# r=4
# t=5
# print(simple_interst(p,r,t))

# compound interest
# def compound_interest(p,r,t):
#     CI=p*(1+r/100)**t
#     Compound_interest=CI-p
#
#     return ("The compound interest is",Compound_interest)
# p=5000
# r=4
# t=5
# print(compound_interest(p,r,t))

# Armstromg number
#
# def Length_Of_No(n):
#
#     length = 0
#     while n:
#          n = n//10
#          length=length+1
#
#     return (length)
# n=1634
# calcuatedlength=Length_Of_No(n)
# print(calcuatedlength)
#
# def Armstrong_No(n):
#     result=0
#
#     while n!=0:
#         s=n%10
#         digit=s**calcuatedlength
#         result=result+digit
#         n=n//10
#     return result
#
# armstrongno=(Armstrong_No(n))
# print(armstrongno)
# def IsArmstrong(n,armstrongno):
#     if n==armstrongno:
#         print("This no. is armstrong no")
#     else:print("This is not armstrong no.")
# IsArmstrong(n,armstrongno)
#
#
# # find the area of circle
# def Area_Circle(r):
#     pi = 3.142
#     return  pi*(r*r)
#
#
# print(Area_Circle(5))

n=567//10
print(n)
# prime no.
# def Prime_no(num):
#     if num>1:
#         for i in range(2,num-1):
#             if num%i==0:
#                 print("This no. is not a prime",num)
#                 break
#         else:
#             print("The given no. is prime no.",num)
# num=5
# Prime_no(num)

# Python Program for n-th Fibonacci number
# def Fibonicci(n):
#     f1=0
#     f2=1
#     print (f1,f2)
#
#     for i in range(1,10):
#        f3=f1+f2
#        f1=f2
#        f2=f3
#        return f3
# n=1000
#
# print(Fibonicci(n))

# def Fibonicci(n):
#     f1 = 0
#     f2 = 1
#     print (f1,f2)
#
#     for i in range(1,n+1):
#        f3=f1+f2
#        f1=f2
#        f2=f3
#        print(f3)
# n=10
# Fibonicci(n)


# def Fibonicci(n):
#      f1 = 0
#      f2 = 1
#      print (f1,f2)
#
#      for i in range(1,10):
#         f3=f1+f2
#         f1=f2
#         f2=f3
#         print(f3)
#         if f3>n:
#             return False
#         if f3==n:
#
#             return True
#      return False
#
#
# n = 5000
#
# f=Fibonicci(n)
# if f==True:
#     print(n,"No. is fib")
# else:
#     print(n,"No. not is fib")
#
#
#
# # Ascii value of char
# a="g"
# print(ord(a))
# print(chr(99))

# Python Program for Sum of squares of first n natural number