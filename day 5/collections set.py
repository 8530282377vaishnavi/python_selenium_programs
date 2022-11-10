# Collections Set
#-->set are unorderd and un indexed . meance the item is stored in random order.
#-->Sets are written in curly bracket {}.
#-->does not contain duplicate element.

#example 1: creating a set
myset={"banana", "apple", "mango", "chiku"}
print(myset) # items are exicuted in random order


#example 2: accesing element from set : we cant access the index value becoz set is unindexed
# myset={"banana", "apple", "mango", "chiku"}
# for i in myset:
#     print(i)

#example 3: Value is exist in set or not
# myset={"banana", "apple", "mango", "chiku"}
# print("banana in myset")  # result true or false in booleans


#example 4: adding the item in set
# add() and update these two functions are use
myset = {"banana", "apple", "mango", "chiku"}
myset.add("cherry") # in add function we can add only one item
print(myset)
#myset.update(["kiwi","dragan fruit"]) #using update function we can add multiple items
#print(myset)

#example 5: find the number of items in set
# myset={'chiku', 'kiwi', 'dragan fruit', 'apple', 'mango', 'banana'}
# print(len(myset))

#remove the items from the sets : remove(), discard()
# myset = {'chiku', 'kiwi', 'dragan fruit', 'apple', 'mango', 'banana'}
# myset.remove("chiku")
# print(myset)
# myset.remove("xyz")  #shows the key error
# print(myset)
# myset = {'chiku', 'kiwi', 'dragan fruit', 'apple', 'mango', 'banana'}
# myset.discard("kiwi")
# print(myset)
# myset.discard("xyz")  # not shows the key error
# print(myset)




#example 6 : i want to clear the items
#myset = {'chiku', 'kiwi', 'dragan fruit', 'apple', 'mango', 'banana'}
# myset.clear() # helps only clearing the data or items
# print(myset)


#example 7: i want to delet whole items with set mean i want to delete whole set
# myset = {'chiku', 'kiwi', 'dragan fruit', 'apple', 'mango', 'banana'}
# del myset
# print(myset) # shows the name error


#example 8: i want to join 2 sets : "union" function and also update function
#set1={"a","b","c", "d"}
#set2={1,2,3,4}
#1st method
# set3=set1.union(set2)
# print(set3)
#2nd method
#set1.update(set2)
#print(set1)

#example 9: i want to print same number or intersect number from the set then use intersection method
set1={1,2,3,4}
set2={1,5,6,3,7,8,9}
set2.add(10)
print(set2)
print(set1.intersection(set2))
