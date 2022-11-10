#collections = list

# Example 1 :how to create a list
'''in the list single variable which can be store multiple value
list collection which is ordered and changeable
list is mutable
in python list written in square bracket []
it is an index collection of items in sequential manner'''


# """mylist1=[100,200,300,499,400,5000]
# mylist2=["apple", "banana", "mango", "cherry"]
# mylist3=["my age is", 20]
# mylist=list()
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)"""


#Example 2 :i want to accessing the item from the list
# mylist2=["apple", "banana", "mango", "cherry", "drgan fruit", "greps"]
# #in list every item represent by index and index is start from 0
# #then how i can extract item from the list
# print(mylist2[5]) #greps
# print(mylist2[4])
# print(mylist2[2])
# print(mylist2[0])
# print(mylist2[3])

#Example 3 : i want to print range of index
# mylist2=["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# print(mylist2[2:5])  #['mango', 'cherry', 'dragan fruit'] display 2 to 5 between number
# print(mylist2[3:6])  # ['cherry', 'dragan fruit', 'greps']


# Example 4 :i want to change/replace the item from the list
#first of all take in mind the list are mutable we can change any time
# mylist2=["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# print(mylist2)
# #show and count the index i want to replace/change cherry to kiwi
# mylist2[3]="kiwi"
# print(mylist2)
#i want to show the index number of item
# print(mylist2.index("mango"))
# print(mylist2.index("greps"))

#Example 5 :i want to read list items using loop
# mylist2=["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# for i in mylist2:
#     print(i)

#Example 6 :check item is exist in the list or not
# mylist2=["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
#
# if "cherry" and "apple" or "banana" in mylist2:
#     print("Yes these fruits are present in the list")
# else:
#     print("No these fruits  are not present in the list")
#

# Example 7 :i want to check list length counting item from the list
# mylist2=["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# print(len(mylist2)) #how many items are present in the list


#Example 8 :i want add new item in the list the functins such as append() and insert()
# mylist2=["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# # mylist2.append("kiwi")
# # print(mylist2) # new item is added at the end of the list using append
# mylist2.insert(1,"kiwi")
# print(mylist2)

#Example 9 :i want to remove the item from the list
#ine function is pop()and another is  keyword del (delete) is use
#mylist2 = ["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# mylist2.pop(2) #here should specify index not value
# print(mylist2)

#del
# del mylist2[3]  #it removes single item based on the index
# print(mylist2)
#in both pop and del we only should use the index value  for deleting the item

#for clearing all the items should use clear function
# mylist2.clear()
# print(mylist2)

#Example 10 :for copy item to new variable
#one approch is list()
# mylist2 = ["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# mylist3=list(mylist2)
# print(mylist2)
# print(mylist3)

#another approch is .copy()
# mylist2 = ["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# mylist3=mylist2.copy()
# print(mylist3)
# print(mylist2)

#Example 11 :i want to join/combine  two list
# mylist1=[100,200,300,499,400,5000]
# mylist2 = ["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# #first approach using concatenation or addition
# mylist3=mylist1+mylist2
# print(mylist3)
#second approch using loop statement append function
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)
#third approch using extend
#mylist1.extend(mylist2)
#print(mylist1)

#example 12 : comparision  of two lists
# mylist1 = ["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
# mylist2=[1,2,3,4,5,6,7,8,9,10]
#
# if mylist1==mylist2:
#     print("yes both are equal")
# else:
#     print("no both are not equal")
#example 13: i want to concatenation two list index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
LIST3=[i+j for i,j in zip(list1,list2)]


# list3 = [i+j for i,j in zip(list1,list2)]
# print(list3)

#another method for loop
# for i,j  in zip(list1,list2):
#     print(i+j,end ='')

mylist1 = ["apple", "banana", "mango", "cherry", "dragan fruit", "greps"]
mylist1.reverse()
print(mylist1)

mylist2=[3,4,2,3,4,1,5,1,10,11,6,7,8]
set=set(mylist2)
print("The converted set :",set)


mylist2.sort()
print(mylist2)