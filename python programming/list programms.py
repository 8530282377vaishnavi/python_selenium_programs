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



