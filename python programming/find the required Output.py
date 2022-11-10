# Find the required output
for i in range(1,21):
    if i==5:
        break

    else:
        print(i)
else:
    print("hello  World ")

#
def fun(n,list1=[]):
    list1.append(list1.append(n))
    return list1
for i in range(4):
    list2 = fun(i)
print(list2)