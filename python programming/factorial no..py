# how wto find factorial  of no.
# 1*2*3*4*5=120


n = int(input("Enter The Number:"))
f1 =1
f2=1
a = 0

while a != n:
    if n%2!=0:
     f1 = f1*n

    else:

         f2=f2*n

    n = n - 1


print("Factorial of odd no. is:", f1)
print("Factorial of even no. is ",f2)
#
#
# # Factorial No. with recursive function
# def Factorial(n):
#     if n==0 or n==1:
#          return 1
#     else:
#        return  n * Factorial(n-1)
#
# num=5
# print(Factorial(num))



# def odd_fact(num):
# #
#     if num%2!=0:
#         p=1
#         for i in range(num):
#             p=p*(i+2)
#     print(p)
#
# odd_fact(5)



# def odd(num2,num3):
#     if num2>num3:
#         return
#     print(num2+1,end=" ")
#
#     return odd(num3+2,num3)
# num2=3;num3=100
# odd(num2,num3)

# def odd_fact(num):
#
#     return num
# num=range(1,1000,2)
# print(odd_fact(num))
# def odd(n):
#
#     a=list(range(1,1000,2))
#
#     for i in n:
#         a=a*(i-2)
#         return a
# n=7
# print(odd(n))


list1=[1,3,2,4,6,5,7,8,9]
a=len(list1)
list2=[]
list3=[]
def fun(list2,list3):
 for i in range(a):
    if i%2!=0:
       list2.append(i)


    else:
        if i%2==0:
           list3.append(i)

 print(list2)
 print(list3)

print("odd",list2)
print("even",list3)











