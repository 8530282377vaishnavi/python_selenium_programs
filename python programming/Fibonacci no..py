# Fibonacci number # 0+1=1+2=3+2=5
#0,1,1,2,3,5

# n=int(input("enter the number:"))
#
# if n==1:
#     f1=0
#     print(f1)
# elif n==2:
#     f1=0
#     f2=1
#     print(f1,f2)
# else:
#     f1=0
#     f2=1
#     print(f1,f2)
# for i in range(2,n):
#     f3=f1+f2
#     f1=f2
#     f2=f3
#     print(f2)

# method 2
# def fun(n):
#   n1=0
#   n2=1
#   print(n1,n2)
#
# for i in range(1,10):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3
# using recursion function print fibonacci no series
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=5
print(fibo(5))
for i in range(20):
    print(fibo())





