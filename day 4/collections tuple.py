#collections tuple
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# print(mytuple)
# mytuple1=()#also we can creat empty tuple


#exampe 1 : how access tuple number
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# print(mytuple[2]) #here index start from zero
# print(mytuple[3])
# print(mytuple[-4])
# print(mytuple[5])

# #example 2 : range of indexes
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# print(mytuple[2:5])
# print(mytuple[3:6])
# print(mytuple[-3:-1])


#change the items from the tuple or not
#we can not modify existing value
#we can not append and insert the new value
#we can not remove the value
#tuples are more secure then list
#we can change the the item in tuple or not ans is we cant change item in tuple
#like modify existing value , append existing value,insert existing value or remove existing value.
#but their is work around by using indirect process we are modify,append,insert,remove the items
#1st tuples are convert to list i.e tuple-->list
#2nd do some modification in list i.e tuple-->list(modify)
#3rd then convert list in to tuple i.e tuple-->list(modify)-->tuple


#example 2 i want to replace the value in tuples
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# mylist=list(mytuple)
# print(mylist)
# mylist[0]='orange'
# mytuple=tuple(mylist)
# print(mytuple)


#example 3: i want to read tuple items using loop
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# for i in mytuple:
#     print(i)


#example 4: i want check the item in the existing tuple or not
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# if "apple" and  "mango" in mytuple :
#     print("yes this fruit is available")
# else:
#     print("No this fruit is not available ")


#example 5: find the total count in tuple
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# print(len(mytuple))

#example 6 : add items in tuple : this is not possible becoz the tuples are imutable we cant change the item/value
# mytuple=("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# mylist=list(mytuple) # i convert tuple into list
#using append() and insert() we can add the items in list (without list we cant add value in tuple)
# print(mylist.append("orange")) #append is add the value at the end of list #modify
# mytuple=tuple(mylist) #convert list to tuple
# print(mytuple)
# print(mylist.insert(3,"pear")) #write the which position i want
# mytuple=tuple(mylist)
# print(mytuple)

#example 7: copy items to new tuple its possible without list
#mytuple = ("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
#1st method
# mytuple2=mytuple
# print(mytuple2)
#2nd method
# mytuple3=tuple(mytuple2)
# print(mytuple3)

#example 8: i want to remove the tuple : it is not possible becoz tuples are imutable
#mytuple = ("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
#print(mytuple.remove("apple")) #this is invalid remove function can not support the tuple collection
#del mytuple #delete is supported this
#print(mytuple)

#example 9: i want to join two  tuples

# mytuple1 = ("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# mytuple2=(1,2,3,4,5,6,7,8,9,10)
#method 1 addition/concadination only use for joining two tuples
# mytuple=mytuple1+mytuple2
# print(mytuple)
#we can joins a multiple tuples though concadination/addition of tuples
# mytuple1 = ("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# mytuple2=(1,2,3,4,5,6,7,8,9,10)
# mytuple3=(11,22,33,44,55,66)
# mytuple=mytuple1+mytuple2+mytuple3
# print(mytuple)

#example 10: comparision of tuples
# mytuple1 = ("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
# mytuple2=(1,2,3,4,5,6,7,8,9,10)
# if mytuple1==mytuple2:
#     print("yes both are equal")
# else:
#     print("no both are not equal")

#example 11: using item i want to find index number
mytuple1 = ("apple", "banana", "mango", "cherry", "dragan fruit", "greps")
print(mytuple1.index("cherry"))