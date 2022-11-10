
# s1=len(string)
# s2=len(string2)

# def two_string(string,string2):
#     for i,j in zip(string,string2):
#        if i==j:
#          return "yes"
#
#     return "no"
#
# string="hello"
# string2="yh"
# str1=two_string(string,string2)
# print(str1)


# def two_string(string,string2):
#     # for i,j in zip(string,string2):
#     for i ,j in zip(string,string2):
#
#      if i & j:
#           return "yes"
#
#     return "no"
#
#
#
# s1="hello"
# s2="yh"
# string=set(s1)
# string2=set(s2)
# str1=two_string(string,string2)
# print(str1)


def two_string(string, string2):
    if set(string) & set(string2):
            return "yes"

    return "no"


string = "hello"
string2 = "sh"
str1 = two_string(string, string2)
print(str1)




#



def remove_space(stri):
    count=0
    for i in stri:
        if not i.isspace():
            count=count+1

    return count

stri='geeksforgeeks 33 best'
remove_space=remove_space(stri)
print(remove_space)



# half is uppercase
def half_uppercase(test_str):
    b=len(test_str)
    a=len(test_str)//2
    stri1=test_str[0:a].lower()
    stri2=test_str[a:b].upper()
    print(stri2)
    stri3=stri1+stri2
    return stri3




test_str = 'geeksforgeek'
print(half_uppercase(test_str))



def fun(str11):
    str1=False
    str12=False

    for i in str11:
        if i.isalpha():
            str1=True
        if i.isdigit():
            str12=True
    return str1 and str12
str11="welcomeourcountry"
function=fun(str11)
print(function)


# capitalization of first and last letter in string
def stat(s):

   s3=s.title()
   print(s3)
   a=s3.split()
   print(a)
   s2=" "
   for i in a:
      s2=s2+i[:-1]+i[-1].upper()+' '
   return s2
s="hello how are you"
capitalization=stat(s)
print(capitalization)

# count the matching chatractor in string


def match_char(str1,str2):

   str11=set(str1)
   str22=set(str2)
   print(str11)
   print(str22)
   str33=str11 & str22
   return (len(str33))

str1 = 'abcdef'
str2 = 'defghia'
match_charactor=match_char(str1,str2)
print(match_charactor)

# remove duplicates for given string

def remove_dupl(remove):
    remove_d=set(remove)
    return remove_d
remove="geeksforgeeks"
remove_duplicate=remove_dupl(remove)
print(remove_duplicate)

# least freq in a string

def least_freq(test_str):

    list1=list(test_str)
    freq=[list1.count(l) for l in list1]
    print(freq)
    count_str=dict(zip(list1,freq))
    count_str2=min(count_str,key=count_str.get)
    return "list freq is ",count_str2


test_str = "GeeksfoarGeeks"
least_freq=least_freq(test_str)

print(least_freq)



# max frequency
def max_freq(test_str):

    list1=list(test_str)
    freq=[list1.count(l) for l in list1]
    print(freq)
    count_str=dict(zip(list1,freq))
    print(count_str)
    count_str2=max(count_str,key=count_str.get)
    return "max freq is ",count_str2


test_str = "GeeksfoarGeeks"
max_freq=max_freq(test_str)
print(least_freq)

#Python – Odd Frequency Characters


test_str = "geekforgeeks"
def odd_freq(test_str):
    duplicate_r=set(test_str)
    res=[]
    for i in duplicate_r:
        if (test_str.count(i))%2!=0:
            res.append(i)
    return res

print(odd_freq("geekforgeeks"))


def occurance(str1):
    str2 = " "
    str3=" "
    for i in str1:
        if i == "r":
            str2 = str1.replace("r", "$")

            str2=str2[:0]+"r"+str2[0+1:]

    return str2
str1= "restartthecomputer"
occurances = occurance(str1)
print(occurances)


#Find all of the numbers from 1–1000 that have a 6 in them
for i in range(0,100,6):
    print(i)

# write the frequency of charactor
def freq(a):
  b=list(a)
  freq=[b.count(l) for l in b]
  print(freq)
  freq2=dict(zip(a,freq))
  return max(occurance.items())


# charactor with highst occurance
a="aabbccyyyyy"
List=list(a)
freq=[List.count(l) for l in List]
occurance=dict(zip(List,freq))
print("max",max(occurance.items()))

print(occurance)

# wap reverse every word of string in proper manner
reverse="this is my book"
reverse_str=reverse[::-1]
reverse_str2=reverse_str.split()
rev=reverse_str2[::-1]
print(rev)

#how to remove duplicate from the given string
dupli="vaishnavi"
dupli2=set(dupli)
print(dupli2)


# print all permutation of sting
a="123"
print(a)
b="ajinkya"

v="vaishnavi"
