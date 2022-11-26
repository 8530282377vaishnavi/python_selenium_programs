# 1)count string charactor
# method 1
from collections import Counter
str="vaishnavi and ajinkya "
rec=Counter(str)
print("the each charactor no. of str is:",(rec))

# method 2
for_frq={}
for i in str:
    if i in for_frq:
        for_frq[i]+=1
    else:
        for_frq[i]=1
print(for_frq)
#covert the string into charactor
v="vaishnavi"
print(v.count("a"))
va=Counter(v)
for i in v:
    print(i)

# 2)count the word in string
# example 1
rec=len(str.split())
print("the word count in string is:",rec,"words")

#exmple 2
str3="ajinkya is my name name is my patil"

rec2=str3.split(" ")
print(rec2)
rec3=(Counter(rec2))
print(rec3)

# 3)swaping the two numbers
# method 1
num1=11
num2= 22
print("the value of num1 before swaping:",num1)
print("the value of num2 before swaping:",num2)
temp=num1
num1=num2
num2=temp

print("the value of num1 after swaping:",num1)
print("the value of num2 after swaping:",num2)

# method 2
# num3=input("enter num3 value:")
# num4=input("enter num4 value:")
#
# num3,num4=num4,num3
# print("the value of num3 after swaping:",num3)
# print("the value of num4 after swaping:",num4)

# sclicing
str="vaishnavi is my name"
print(str[3:-9])

# reverse string
ajinkya="My name is ajinkya"
revr=ajinkya.split(" ")
revr3=(revr[::-1])

print(revr3)

#
revr2=(ajinkya[::-1] )
print(revr2)

b="monday sunday"
c=b.split(" ")
abc=c[::-1]
print(abc)


# a=int(input("enter first no.:"))
# b=int(input("Enter second no.:"))
# c=a**b
# print(c)



str2="MOM"
rec3=(str2[::-1])
print(rec3)
if str2==rec3:
    print("str2 and rec3 are equal")
else:
    print("str2 and rec3 are not equal")

rev=""
for i in str2:
    rev=i+rev
print("reverse:",rev)
if rev==str2:
    print("the str2 is palendrom")
else:
    print("the str2 is not palendrom")


# reverse the string
v="vaishnavi"
print(v[::-1])



# find the missing number  in the array
def missing_no(a):
    n=a[-1]
    total=n*(n+1)//2
    print(total)
    sum1=sum(a)
    print(sum1)
    print("The missing no. is ",total-sum1)


a=[1,2,3,5,6,7,8]
missing_no(a)
