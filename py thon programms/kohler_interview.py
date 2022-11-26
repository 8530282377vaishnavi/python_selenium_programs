dictionary={"a":1,"b":2, "c":[1,2,3]}
# for i in dictionary.values():
#     print()
print(dictionary.get("c"))
for i in dictionary.get("c"):
    print(i)
dictionary2={("a","b"):1}
dictionary3={}
dictionary3["a","b"]=1
for i in dictionary3:
    print(i,dictionary3[i])
print("vaishnavi",dictionary3)
for x,y in list(dictionary2.items()):
    print(x,y)
a=list(dictionary2.keys())
print(a)

print(dictionary2)
for x in dictionary2.keys():
  print(dictionary2)

for x,y in dictionary2.items():
    print(x,y)


list1=["key1","key2","key3"]
list2=[2,3,4,5]
dictionary11={list1[i]:list2[i] for i in range(len(list1))}
print(dictionary11)

dictionary2={}

dictinary2=dict(zip(list1,list2))
print(dictinary2)

a=1
b=1
print(id(a))
print(id(b))
print(a==b)

string=" kohlar is product based companey "
split=string.split()
reverse=split[::-1]
print(" ".join(reverse))











n=5
for i in range(n):
    print("i ",i)
    for j in range(i+1):
        print("j ",j)
        print("*",end=" ")
    print()


