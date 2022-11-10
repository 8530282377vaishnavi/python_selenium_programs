# armstrong numbers
# 145 = 13=1, 43=64, 53=125

for i in range(1001):
    num=i
    result=0
    n=len(str(num))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(result)

n=54
a=n//10
print(a)
