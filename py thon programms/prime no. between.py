# prime no. betweeen 100 to 200

# num1=int(input("enter the first value:",))
# num2=int(input("enter the first value:",))
#
# for num in range(num1,num2+1):
#        if num>1:
#               for i in range(2,num):
#                   if (num %i)==0:
#                      print(num)


# 2)prime no.
num3=int(input("enter upper no.:"))
num4=int(input("enter lower no.:"))
for num5 in range(num3,num4+1):
  if num5>1:
       for i in range(2,num5):
              if(num5%i)==0:
                  break
       else:
         print(num5)
