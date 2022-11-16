

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


#

def rev_even(ls):
    l=ls.split()
    i=0
    ls1=[]

    while i<len(l):
        if i%2 == 0:
            ls1.append(l[i])
        else:
            ls1.append(l[i][::-1])
        i=i+1
    output=" ".join(ls1)
    return output
ls="one two three five six seveen"
rev_even=rev_even(ls)
print(rev_even)

# even index and odd index

a="vaishnavi"
print("even")
i=0

while i<len(a):
        print(a[i])
        i=i+2


print("odd")
i1=1
while i1<len(a):
       print(a[i1])
       i1=i1+2




#INPUT="aa3b4z2" output=aaabbbbzz
def increment(input):
    output=" "
    for i in input:
        if i.isalpha():
            x=i
        else:
            output=output+(x*int(i))
    return output


input="a2s3d4"
print(increment(input))

# input=2a3bc4 output=aabbbcccc
def increment2(input2):
    outcome1=" "
    for i in input2:
        if i.isdigit():
            x=int(i)
        else:
            outcome1=outcome1+(i*x)
    return outcome1
input2="2a3b4c"
increment2=increment2(input2)
print(increment2)



#input="a3b4c5" output=abc345
#  alphabet symbols and then digits
def add(s2):
    x=" "
    y=" "
    xy=" "
    for i in s2:
        if i.isalpha():
            x=x+i
        if i.isdigit():
            y=y+i

    xy=x+y
    return xy
s2="a2b3c4"
print(add(s2))

#method2
# Program to sort characters of the string, first alphabet symbols followed by digits
def add2(s3):
    x2=[ ]
    y2=[ ]
    xy=[]
    for i in s3:
        if i.isalpha():
            x2.append(i)
            x2.sort()
            print("alpha",x2)
        else:
            y2.append(i)
            y2.sort()
            print("digit",y2)
    xy=x2+y2
    a="".join(xy)

    return a
s3="c2b4a3"
print("string and digit",add2(s3))




def add(s2):
    x=" "
    y=" "
    xy=" "
    for i in s2:
        if i.isalpha():
            x=x+i
        if i.isdigit():
            y=y+i

    xy=x+y
    return xy
s2="2q3w4e"
print(add(s2))



# input="aaabbbcccc" output=3a3b4c

def freq(count_digstr1):
    privious=count_digstr1[0]
    count1=0
    i=1
    output11=" "
    while i<len(count_digstr1):
        if count_digstr1[i]==privious:
            count1=count1+1
        else:
            output11=output11+str(count1)+privious
            privious=count_digstr1[i]
            count1=1
        if i==len(count_digstr1)-1:
            output11=output11+str(count1)+privious
        i=i+1
    return output11

count_digstr1="aaaabbbbcccddd"
print(freq(count_digstr1))


# input="aaaabbbbcccddd" and output=4
def repeat_count(count_digit):
    previouss=count_digit[0]
    count=0
    output_count=0
    i=0
    while len(count_digit)>i:
        if count_digit[i]==previouss:
            count=count+1
            if count==1:
                count=0
            elif count>=2:
                count=1
        else:
            output_count=output_count+count
            previouss=count_digit[i]
            count=0
        i=i+1
    return output_count
count_digit="aaaabbbbcccddd"
print(repeat_count(count_digit))

# input=a4b4k3 output=aebfkn  #aphabate find acording to position no
def position(aplph):
    position2=" "
    for i in alpha:
        if i.isalpha():
            x=i
            position2=position2+x
        else:
            d=int(i)
            new=chr(ord(x)+d)
            position2=position2+new
    return position2


alpha="a3b5k3"
print(position(alpha))


a=int("4")
b=chr(ord("a")+a)
print(b)
print(chr(ord("a")+5))

# Wrt a prog to merge characters of 2 strings into a single string by taking characters altern
#method 1 if len is same
def marge(s,b):
   a=[i+j for i,j in zip(s,b)]
   a22="".join(a)
   return a22
s="ravi"
b="ajinkya"
marge=marge(s,b)
print(marge)
# method 2
def marge2(s1,s2):
    i=0
    j=0
    alternate=" "
    while i<len(s1) or j<len(s2):
        alternate=alternate+s1[i]+s2[j]
        i=i+1
        j=j+1
    return alternate
s1="REENA"
s2="SEENA"
marge2=marge2(s1,s2)
print(marge2)

# method 3 if the length does not match
def marge3(len1,len2):
    i=0
    j=0
    out=" "
    while i<len(len1) or j<len(len2):
        if i<len(len1):
           out=out+len1[i]
           i=i+1
        if j<len(len2):
            out=out+len2[j]

            j=j+1
    return out
len1="patil"
len2="ajinkya"
marge3=marge3(len1,len2)
print(marge3)


# Wrt Prog to print the characters present at even index and odd index?
def even_odd(eve_odd):
    i=0
    print("even str")
    while i<len(eve_odd):
        print( eve_odd[i])
        i=i+2
    i=1
    print("odd str")
    while i<len(eve_odd):
        print(eve_odd[i])
        i=i+2

eve_odd="vaishnavi"
even_odd(eve_odd)

# Write a Program To REVERSE internal content of every second word present in the given string?
# rev_word="one two three four five six seven"
def fun(rev_word):
    rev_word2=rev_word.split()
    reverse=[ ]
    i=0
    while i<len(rev_word2):
        if i%2==0:
            reverse.append(rev_word2[i])
        else:
            reverse.append(rev_word2[i][::-1])
        i=i+1
    reverse2=" ".join(reverse)
    return reverse2


rev_word="one two three four five six seven"
print(fun(rev_word))

#  Write a Program To REVERSE internal content of each word?
# input="vaishnavi ajinkya patil"
#output="ivanhsiav ayknija litap"

#method1
# def reverse(word):
#     word2=word[::-1]
#     word3=word2.split()
#     print(word3)
#     word4=word3[::-1]
#     word5=" ".join(word4)
#     return word5
# word="vaishnavi ajinkya patil"
# print(reverse(word))

#method 2
def reverse(word):
    word2=word.split()
    list11=[]
    for i in word2:
        list11.append(i[::-1])
    return " ".join(list11)
word="vaishnavi ajinkya patil"
print(reverse(word))


# Write a Program To REVERSE order of words present in the given string
# input="vaishnavi ajinkya patil" output="  patil  ajinkya vaishnavi"
def rev(revr):
    revr2=revr.split()
    print(" ".join(revr2[::-1]))

revr="vaishnavi ajinkya patil"
rev(revr)