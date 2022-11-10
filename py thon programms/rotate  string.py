
#for rotating the left rotatingsting
def leftrotationstring(name):
    size=len(name)

    temp=name+name

    for i in range(size):
        for j in range(size):
            print(temp[i+j],end=" ")
        print()


string="NETSET"
leftrotationstring(string)


# for rotating the right rotatingsting
# def rightrotatestring(name):
#     size=len(name)
#     temp=name+name
#     for i in range(size):
#         for j in range(size):
#             print(temp[i-j],end=" ")
#         print()
#
# string="NETSET"
# rightrotatestring(string)

# def checkrotation(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#
#     s=str1+str1
#     if str2 in s:
#         print(str1,"matching with",str2)
#     else:
#         print(str1,"not matching with",str2)
# checkrotation("NETSET","NETSET")