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
# The original string is : GeeksforGeeks
# The minimum of all characters in GeeksforGeeks is : f



