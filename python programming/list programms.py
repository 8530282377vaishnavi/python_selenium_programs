# list sort
List1 = [1, 4, 3, 2, 5, 6, 8, 7, 9, 11]
List1.sort()
print(List1)

n=len(List1)
#sort a list without using sort
for i in range(n):
    for j in range(i+1,n):
        if List1[i]>List1[j]:
            List1[i],List1[j]=List1[j],List1[i]
print(List1)

# To remove Duplicates in list
List2 =  [1, 2, 1, 3, 3, 4, 2, 5, 6, 4, 7, 7, 6, 8]
set1 = set(List2)
List3 = list(set1)
print(List3)

# List reverse sort
List4=[9, 8, 7, 5, 4, 3, 2, 4, 6, 1, 10]
List4.sort()
print(List4)
List4.reverse()
print(List4)

# Find the list middle element
# List5 = [1, 2, 3, 4, 5, 6, 7, 8, 6, 7]
# if len(List5) % 2 == 0:
#     X=len(List5)//2
#     y=len(List5)//2 -1
#     print(List5[X],List5[y])
# else:
#     n=len(List5)//2
#     print(List5[n])


# find the last and first element in list
def fun2(List6):
  a = List6[0]
  b = List6[-1]
  return a,b

def fun(List6):

    x=len(List6)//2
    y=len(List6)//2-1
    return (List6[x],List6[y])


List6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The first and last element in list is: ",fun2(List6))
print("The last element in list: ",fun(List6))



# second largest no. in list
List=[1, 2, 3,11,15,18,14, 4, 5, 6, 7, 8, 9, 10,2]
list11=set(List)
print(list11)
List7=list(list11)
List7.sort()
print(List7)

print("This is second largest no.",List7[-2])

#  find the pair with given no. in a list which has sum of k

# List8=[2,4,6,1,3,5,7,5,9,0,10]
# n=len(List8)
# k=10
# for i in range(n):
#      for j in range(i+1,n):
#          if List8[i]+List8[j]==k:
#              print(List8[i],List8[j])









lis=[5,7,4,3,9,8,1,21]
k=17
n=len(lis)
for i in range(n):
    for j in range(i+1,n):
        if lis[i]+lis[j]==k:
            print(lis[i],lis[j])



# conversion of two list into dict.
# def list_dict():
#     List11=[1,2,3,4]
#     List12=["vaishnavi","ajinkya","patil","name"]
#     name=dict(zip(List11,List12))
#     print(name)
#
# list_dict()

# conversion of dict to tuple
def list_tuple():
  x={1: 'vaishnavi', 2: 'ajinkya', 3: 'patil', 4: 'name'}
  for i in x.items():
    print(i)

list_tuple()

#  Remove empty tuples from a list
# tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
# Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]
# def remove_tuple(tuples):
#     new_list=[]
#     for i in tuples:
#         if i==tuple():
#             continue
#         new_list.append(i)
#     return new_list
# tuples = [(',','8'), (), ('0', '00', '000'), ('birbal', ',' '45'), (),  (","),()]
# print(remove_tuple(tuples))


#
def remove_tuple(tuples):

    for i in tuples:
        if len(i)==0:
            tuples.remove(i)

    return tuples
tuples = [(',','8'), (), ('0', '00', '000'), ('birbal', ',' '45'), (),  (","),()]
print(remove_tuple(tuples))


# Program to print duplicates from a list of integers
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]
def dupli_list(lis1):
    set11=[]
    lis11=[]
    for i  in lis1:
        if i in set11:
            lis11.append(i)


        else:
            set11.append(i)

    return  set(lis11)
lis1=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(dupli_list(lis1))


# Convert List to List of dictionaries
# Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]

def list_dict(test_list,key_list):
    res2=[]
    n=len(test_list)
    for i in range(0,n,2):
        # rec22.append({key_list[0]:test_list[i], key_list[1]:test_list[i+1]})
        res2.append({key_list[0]: test_list[i], key_list[1] : test_list[i + 1]})


    return res2


test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]
print(list_dict(test_list,key_list))

#
def test_str(test_list ,key_list):
   n = len(test_list)
   res = []
   for idx in range(0, n, 2):
       res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx + 1]})

# printing result
   return ("The constructed dictionary list : " + str(res))
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]
print(test_str(test_list,key_list))


#
lis111=["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

dict1=dict(zip(lis111,lis111))
print(dict1)


# Convert a list to dictionary
# Input : ['a', 1, 'b', 2, 'c', 3]
# Output : {'a': 1, 'b': 2, 'c': 3}
def list_dict(abc):
    dect={abc[i]:abc[i+1] for i in range(0,len(abc),2)}
    return dect
abc=['a', 1, 'b', 2, 'c', 3]
print(list_dict(abc))
# sort list without using sort
def sort_list(temp):
    for i in range(0,len(temp)):
        for j in  range(i+1,len(temp)):
            if temp[i]>temp[j]:
                temp[i],temp[j]=temp[j],temp[i]
    return temp

temp=[1,2,4,3,6,5,8,7,9,6]
print(sort_list(temp))