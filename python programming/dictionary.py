# merging two dictionary
def Marge(dict1,dict2):
    res=dict1|dict2
    return res
dict1={1:"vaishnavi",2:"Vishwas",3:"Santoshi"}
dict2={4:"Ajinkya",5:"Rupali",6:"nayana"}
dict3=(Marge(dict1,dict2))
print(dict3)




dis={"Name": "vaishnavi",
     "last Name": "patil",
     "Roll No.": 22}
# /html/body/div[4]/div[2]/div/div[2]/div/div/div[1]/article/div[3]/div[5]

# changing the items in dict
dis["Name"]="ajinkya"

# adding the item in dict
dis["phone no."]=5485255


# revrse the dictionary
print(str(dis))
rec=dict(reversed(list(dis.items())))
print(str(rec))

# dict convert into list
lists=[]
for i,j in dis.items():
    lists.append([i,j])
print(lists)

print(dis)
print(dis.values())
print(dis.get("lst Name"))

list1=list(dis.items())
print("1",list1)

list2=list(dis.values())
print("2",list2)

list3=list(dis.keys())
print("3",list3)

#sort a dictionary
dict={2: "Vaishnavi", 4:"Ajinkya", 5:"Patil",1:"Santoshi", 3:"Vishwas"}
d=sorted(dict.keys())
dict2={}
for i in d:
    dict2[i]=dict[i]
print(dict2)
