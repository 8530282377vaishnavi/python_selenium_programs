#count the digit

n=12345
a=0
while n!=0:
    n=n//10
    a=a+1
print(a)

# reverse the digit
n=123456
rev=0
while n>0:
    s=n%10
    rev=(rev*10)+s
    n=n//10
print(rev)


# write a palendromic sequence of digit
n=121
p=n
r=0
while n!=0:
    s=n%10
    r=(r*10)+s
    n=n//10
print(r)
if r==p:
    print("THis is palendronic sequence of no. ")
else:
    print("N0t palendromic ")

# addition of digits
n=12345
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)

# square root of each digit with additoin

n=123
sum2=0
while n!=0:
    s=n%10
    a=s*s
    sum2=sum2+a
    n=n//10
print(sum2)




