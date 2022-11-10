num1=1000
num2=12.22

print(type(num1))
print(type(num2))

#find maximum value of given number
#max() function will return maximum value
print(max(12,20,33,22,55,66,58,90))

#find minimum value of given number
#min() function will return minimum value
print(min(20,30,50,5,60,90,9,8,70))

x=12,20,33,22,55,66,58,90
x2=list(x)
print(x)
x2.sort()
print(x2)
print(x2[-1])

#min. max. function both are available for both int and float
print(max(12.2,20.3,33.5,22.6,55.5,66.6,58.8,90.2))
print(min(20.6,30.2,50.3,5.0,60.3,90.2,9.6,8.5,70.5))
