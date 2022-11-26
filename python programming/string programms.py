# removing ith char of string
def remove_char(a,c):
   b=" "
   for i in a:
       if a.index(i)== c:
           continue

       b=b+i
   return (b)
a="vaishnavi"
c=4
remove_char=remove_char(a,c)
print(remove_char)

# Python program to Remove Last character from the string
# nput:  “GeeksForGeeks”
# Output: “GeeksForGeek”
def remove_last(str11):
    output=" "
    last=str11[-1]
    for i in str11:
        if i ==last:
            continue
        output=output+i
    return output
str11='GeeksForGeeks'
print(remove_last(str11))



# check the given string is binary
str = "vaish0101010"
for i in str:
    if i=="0"or i=="1":
       print("yes")

    else:
        print("no")


# find the uncommon words in string
#  A = "Geeks for Geeks"
#  B = "Learning from Geeks for Geeks"

def un_common(A,B):
    c=A.split()
    d=B.split()
    e=[]
    for i in d:
        for j in c:
         if i not in c:
            e.append(i)
         if j not in d:
                e.append(j)

    return set(e)
A = "Geeks for Geeks  abc mnc"
B = "Learning from Geeks for Geeks python"
print(un_common(A,B))


# Python – least Frequent Character in String
# The original  string is : GeeksforGeeks
# The minimum of all characters in GeeksforGeeks is : f
str="geeksforgeeks"
rec={}
for i in str:
    if i in rec:
      rec[i]+=1
    else:
        rec[i]=1
rec2=min(rec,key=rec.get)
print(rec2)


# Python – Avoid Spaces in string length
# Input : test_str = ‘geeksforgeeks 33 best’
# Output : 19
# Explanation : Total characters are 19.
#
# Input : test_str = ‘geeksforgeeks best’
# Output : 17
# Explanation : Total characters are 17 except spaces.
def  remove_space(string):
    remove_space=" "
    for i in string:
        if i.isspace():
             continue
        else:
           remove_space=remove_space+i
    print(remove_space)
    print(len(remove_space))
string='geeksforgeeks best'
remove_space(string)
string2=string.replace(" ","")
print(len(string2))


# Input: hello world
# Output: HellO WorlD
def str(contact):
    contact2=contact.split()
    contact5=[]
    for i in contact2 :
        x=i[0].upper()+i[1:-1]+i[-1].upper()
        contact5.append(x)
    contact5=" ".join(contact5)
    print(contact5)
contact="hello world"
str(contact)

# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
sam_str="google.com"
dict={}
for i in sam_str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def str_len(string11):
    for i in string11:
        if len(string11)<2:
            return " ","empty string"
        return string11[0:2]+string11[-2:]

string11="w3"
print(str_len(string11))

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
def replace(sample):
    char=sample[0]
    sample=sample.replace(char,"$")
    sample=char+sample[1:]
    print(sample)
sample="restart"
replace(sample)

# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def get_string(a,b):
    get2=b[:2]+a[2:]
    get3=a[:2]+b[2:]
    return get2+" "+get3
# abz xyc
print(get_string("xyz","abc"))

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
def add(str_ing):
    if len(str_ing)>=3:
        if "ing" in str_ing:
          string2=str_ing+"ly"
        else:
            string2=str_ing+"ing"
    print(string2)

str_ing="abc"
add(str_ing)

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor'
# from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def replace(aa):
   snot=aa.find("not")
   print(snot)
   spoor=aa.find("poor")
   print(spoor)
   if spoor > snot and spoor>0 and snot>0:
       aa=aa.replace(aa[snot:spoor+4],"good")
       return  aa
   else:
      return aa


aa='The lyrics is not poor!'
print(replace(aa))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


def longest_word(list_long):

    c1=[len(i) for i in list_long]
    print(c1)
    freq2={list_long[i]:c1[i] for i in range(len(list_long))}
    print(freq2)
    print("Length of the longest word:",max(freq2.values()))
    print("Longest word:",list(freq2.keys())[list(freq2.values()).index(16)])




list_long=["This","is","my","Exercises","vaishanviajinkya"]
longest_word(list_long)

# 9. Write a Python program to remove the nth index character from a nonempty string.
def remove_index(vv,nth_index):
    vv2=" "
    for i in vv:
        if vv.index(i) == nth_index:
             continue

        vv2=vv2+i
    return (vv2)
vv="vaishnavi"
nth_index=1
remove_index=remove_index(vv,nth_index)
print(remove_index)



