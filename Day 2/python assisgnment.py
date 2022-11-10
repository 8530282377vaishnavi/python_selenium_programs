#Example 6: check the given number is positive or negative  (>0 or <0)
#Check largest of 2 number
#Check largest of 3 number
#print week number if provide weekname as week number.#


#Example 6: check the given number is positive or negative  (>0 or <0)
a=11
if a>0:
    print("Positive number")
else:
    print("Negative Number")

#Check largest of 2 number
a=22
b=44
if (a>b):
    print("largest number a")
elif(b>a):
    print("largest number b")
else:
    print("invalid number")

#Check largest of 3 number
num1=11
num2=46
num3=44
if (num1>num2) and (num1>num3):
    print ("largest number is num1")
elif (num2>num1) and (num2>num3):
    print ("largest number is num2")
elif (num3>num1) and (num3>num2):
    print ("largest number is num3")
else:
    print ("not valid number")


#print week number if provide weekname as week number.
weekname="friday"

if weekname==("sunday"):
    print("week no.=1")
elif weekname==("Monday"):
    print(2)

else :
   print(" not valid week no ")

#Check largest of 2 number
a=-200
b=11
c=444
if (a>b) and (a>c):
    print("a is largest number")
elif(b>a) and (b>c):
    print("b is largest number")
elif(c>a) and (c>b):
    print("c is largest number")
else:
    print("invalid numbers")



