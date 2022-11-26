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

#sort a dictionary by key and value
dict={2: "Vaishnavi", 4:"Ajinkya", 5:"Patil",1:"Santoshi", 3:"Vishwas"}
d=sorted(dict.keys())
print(d)
dict2={}
for i in d:
    dict2[i]=dict[i]
print(dict2)
# Handling missing keys in Python dictionaries
def missing_key(d2):

   print(dict.get(5, "not found"))
   print(dict.get(6,"not found"))
d2= { 2: "Vaishnavi", 4:"Ajinkya", 5 : "Patil",1:"Santoshi", 3:"Vishwas"}
missing_key(d2)

# Python code to demonstrate a dictionary
# with multiple inputs in a key.
rec2 = {}
x, y, z = 10, 20, 30
rec2[x, y, z] = x+y-z
x, y = 3, 5
rec2[x, y, z] = x+y-z
print(rec2)


# Output : 600
def sum(input):

  sum=0
  for i in input.values():
    sum = sum+i
  print(sum)
input = {"a": 25, "b": 18, "c": 45}
sum(input)

# Find the size of a Dictionary in Python
import sys
print(sys.getsizeof(input),"bytes")

# Sort Python Dictionaries by Key or Value
# Input:
# key_value[2] = '56'
# key_value[1] = '2'
# key_value[4] = '12'
# key_value[5] = '24'
# key_value[6] = '18'
# key_value[3] = '323'
#
# Output:
# 1 2 3 4 5 6
def sort(key_value):
    key_value[2] = '56'
    key_value[1] = '2'
    key_value[4] = '12'
    key_value[5] = '24'
    key_value[6] = '18'
    key_value[3] = '323'
    d3=sorted(key_value)
    for i in d3:
        print(i,end=" ")
    print()


key_value={}
sort(key_value)

jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }
# 2. James's dictionary
james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }
# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }

# Insertion at the beginning in OrderedDict
# Input:
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)
#
# Output:  {'c':3, 'a':1, 'b':2}
#
# Input:
# original_dict = {'akshat':1, 'manjeet':2}
# item to be inserted ('nikhil', 3)
#
# Output:  {'nikhil':3, 'akshat':1, 'manjeet':2}


from collections import OrderedDict

in_orderdict=OrderedDict([('akshat',1), ('manjeet',2)])
in_orderdict.update({'nikhil':3})
in_orderdict.move_to_end('nikhil',last=False)
print(in_orderdict)

in_orderdict2=OrderedDict([('a',1),("b",2)])
in_orderdict2.update({'c':3})
in_orderdict2.move_to_end("c",last=False)
print(in_orderdict2)

# method 2
dic1=OrderedDict([('a',1),("b",2)])
dic2=OrderedDict([('c',3)])


#both=  OrderedDict(list(dic1.items())+list(dic2.items()))
both = OrderedDict(list(dic2.items()) + list(dic1.items()))
print("both",both)
#

