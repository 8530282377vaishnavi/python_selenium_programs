#create string variable

#example1 :way of creating string varibles are
# s="welcome"
# s='welcome'
# s=str("welcome")
# s=str('welcome')
#
#
#Example 2 :creating empty string variable
# name=''
# name=" "
# name=str()

#example 3 : how to string memory will change
# mutable  can  change the value of variable *mute can  change

#imutable can  not change the value of variable   *imute can not  change
#string is imutable

str1="welcome"
print(id(str1))    #id shows the memory location of variable

str1=str1+  "  to python"
print(id(str1))
print(str1)


#example 4  : + and * with the string
# str="welcome"
#
# print(str+"to python") #concatination
# print(str*2)  # * is used to print the variable multiple times

#slicing concept :cut the strings based on the provided value
#Example 5
   # 0123456   for starting point
   # 1234567   for ending point
s="welcome"
# -7-6-5-4-3-2-1
# starting point is 0
# ending point is 1
#         [0:1]
print(s[1:3]) # i.e 1=start point and 3 is end point 1=0 and 3=1
print(s[2:4])
print(s[:5])
print(s[0:-1]) # meance split last value
print(s[1:-1])
print(s[1:5])
print(s[3:])

#example 61
# print ord()  char()
# ord ()it return  the ASCII code of the character
# print(ord('A'))
# print(ord('a'))
# chr () it retun the character represented by ASCII number
# print(chr(97))
# print(chr(65))

#example 7
#print max() = maximum character in string
# min()  =  shows min character in string
# len()  = shows the length of character

print(max("abcde"))  #maximum character in string
print(min("abcde"))  #shows min character in string
print(len("vaishnavi"))#shows the length of character

# Example 8
# use in and not in operator
# in and not in operator returns alays boolean value i.e true or false
# str='vaishnavi'
# in
# print('vaish' in str) #true
# print('ajinkya' in str) #false
# not in
# print('vaish' not in str) #false
# print('ajinkya' not in str) #true

#example 9  : string comparision using relational operator
# it always return in boolean
# print("tim"=="tia")
# print("free"!="freedom")
# print("arrow">"aron")
# print("teeth"<"tee")
# print("right">="left")
# print("yellow"<="fellow")
# print("abc">"")

#Example 10   : testing string  return in booleans true or false
a="welcome in python"
print(a.isalnum())  # isalnum is used to check the string contain number or not
print(a.isalpha())  # isalpha is used to check the string contain alphabate  or not
print("2022".isdigit()) #isdigit is used to check the string contain digit or not
print("first.name".isidentifier()) #isidentifier is used to check the string contain python reserve keyword or not
print(a.islower()) #islower is used to check the string contain all charactor is in lower case or not
print("VAISHNAVI".isupper()) #isupper is used to check the string contain all charactor is in upper case or not
print(" ".isspace()) #isspace is used to check the string contain in string their is space  or not

#example 11 : serching for substring function
# a= "welcome in python automation"
# print(a.endswith("tion")) # give the true or false
# print(a.startswith("welcome")) # give the true or false
# print(a.find("come"))
# print(a.find("become")) # if character is not their then print the negative value
# print(a.count('a'))  # count how many time this character in this string

#example 12 : how to convert the string
s="Welcome in PYTHON"
s1=s.capitalize()
print(s1)
s2=s.title()
print(s2)
s3=s.upper()
print(s3)
s4=s.lower()
print(s4)
s5=s.replace("in", "on")
print(s5)
s6=s.swapcase()   # lower to upper and upper to lower
print(s6)


#Example 13
# most importent interview que.
#Reverse string
#method 1
#  b="welcome"
#  revr_str=""
#  for i in b:
#      revr_str=i+revr_str
# print("reverse string is :",revr_str)

b='ajinkya'
rev_str2=''
for i in b:
    rev_str2=i+rev_str2
print("reverse string is :",rev_str2)

#
#
#method2  using splicing
s="vaishnavi"
rev_str=s[::-1]
print(rev_str)
s="vAishnavi"
print(s.count('a'))
n=s.lower()
print(n.count('a'))
print(s)
#
s="ajinkYA"
print(s.lower())



#  example 14 i want to print "WEL-COME"
# str="welcome"
# str2=str.upper()
# print(str2)
# str3=str2[0:3]
# str4=str2[3:7]
# str5=str3+"-"+str4
# print(str3)
# print(str4)
# print(str5)


#Example 15 : i want to print welcome in even order

ss="welcome"
ss2=""
for i in range(len(ss)):
    if i%2==0:
        ss2=ss2+ss[i]
print(ss2)



# for i in range(0,11,2):
#    print(i)
#    print("is even number")

# print(i)  and print(index)

str="python language"
str2=str[::-1]
print(str2)
# print(str[4:])
reverse=""
for i in str:
    reverse=i+reverse
print("the reverse value is:",reverse)

strr=len(str)




