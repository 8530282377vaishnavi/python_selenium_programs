# Method1
lista=["vaishnavi","patil",]
# list.reverse()
# print(list)

#method2
lista=list[:-1]
print(lista)
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


# write the largest number
a=22
b=33
if a>b:
    print("a is larger than b")
elif b>a:
    print("b is larger than a")
else:
    print("invalid number")


# largest number of 3
c=555
if a>b and a>c:
    print("a is larger no. than both b and c")
elif b>a and b>c:
    print("b is larger no. than both a and c")
elif c>a and c>b:
    print("c is larger no. than both a and b")
else:
    print("invalid no. ")




#sort a dictionary
dict={2: "Vaishnavi", 4:"Ajinkya", 5:"Patil",1:"Santoshi", 3:"Vishwas"}
d=sorted(dict.keys())
dict2={}
for i in d:
    dict2[i]=dict[i]
print(dict2)

# find the common letter between two strings

def Common_letter():
  v="Vaishnavi"
  a="Ajinkya"
  str1=set(v)
  str2=set(a)
  print(str1 & str2)
Common_letter()



def symentric(v):
    mid=(len(v)+1)//2
    half=(v[0:mid])
    secondhalf=(v[mid:len(v)])
    if half==secondhalf:
        return True
    else:
        return False
v = "amaama"
issymentric=symentric(v)
if issymentric==True:
    print("The given string is symentric ")
else:
    print("The given string is not symentric ")

def palendromic(v):
    palendrom=v[::-1]
    if v==palendrom:
        return True
    else:
        return False

palendrom=palendromic(v)
if palendrom==True:
    print("The given string is palendrom")
else:
    print("The given string is  not palendrom")



# Ways to remove i’th character from string in Python

def remove_char(str1):
   if indexvalue>=len(str1) or indexvalue<len(str1):
       return "invalid index"


   str2=" "
   for i in str1:
     if i==str1[indexvalue]:

       continue

     str2 = str2 + i
   return str2

str1 = "python"
str3=len(str1)
indexvalue=-12

removechar=remove_char(str1)
print(removechar)


# count the length of string
def count_length(str1):
    a=0
    for i in str1:
        a=a+1

    return a
str1="ajinkya"
length_str=count_length(str1)
print('length of str is ',length_str)

def even_len(s):

   s2=s.split()
   s3=list(s2)
   print(s3)
   s4=[]

   for i in s3:
       if len(i)%2==0:
        s4.append(i)
   return s4



s="I am vaishnavi "
even_length=even_len(s)
print(even_length)

# count the no of digit and letters in given string

def count_dl(a):
   count_no=0
   count_str=0

   for i in a:
      if i.isdigit():
          count_no=count_no+1
      if i.isalpha():
          count_str=count_str+1
   return (count_no),count_str

a="python234programming"
count_dl=count_dl(a)
print("the count is",count_dl)


