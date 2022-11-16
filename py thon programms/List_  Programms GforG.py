# List Collection Datatype program's
# def swap(List):
#     List[0],List[-1]=List[-1],List[0]
#     return (List)
# List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
# List2=swap(List)
# print(List2)
#
# #Python program to swap two elements in a list
# def swaplist(List):
#     List[1],List[5]=List[5],List[1]
#     return List
#
# List = ["vaishnavi", "ajinkya", "santoshi", "rupali", "nayana", "patil"]
# List3=swaplist(List)
# print(List3)
#
# # ways of find the length of list
# def Length(List):
#     return (len(List))
# List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
# len=Length(List)
# print("The No. of items in list",len)
#
#
# def length_list(List):
#   count=0
#
#   for i in List:
#     count=count+1
#   return (count)
# List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
# length2=length_list(List)
# print("The No. of items in list",length2)
#
# #Check if element exists in list in Python
# def exist_element(List):
#     if "ajinkya" in List:
#         return True
#     else:
#         return False
# List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
# exist=exist_element(List)
# print(exist)
#
#
# #find the second largest no in list
#
# def second_max(list1):
#     max_var=max(list1)
#     list1.remove(max_var)
#     print(list1)
#     return max(list1)
#
#
#
# list1 = [ 20,4,12,10]
# second_maxno=second_max(list1)
# print("The second max no. is ",second_maxno)
#
# def second_max(list1):
#     list1.sort()
#     list2=list1[-2]
#     return list2
#
# list1 = [ 20,4,12,10]
# second_maxno=second_max(list1)
# print("The second max no. is ",second_maxno)
#
#
# def second_max(list1):
#     max1=max(list1)
#     max_ver=0
#     for i in list1:
#         if i!=max1:
#             if i>max_ver:
#                 max_ver=i
#     return max_ver
#
#
#
#
# list1 = [ 20,4,16,10]
# second_maxno=second_max(list1)
# print("The second max no. is ",second_maxno)
#
#
#
# def sum_list(list11):
#     a=0
#
#     for i in list11:
#         a=a+i
#     return a
#
#
#
# list11=[4, 5, 1, 2, 9, 7, 10, 8]
# sum_lis=sum_list(list11)
# print("sum of all no",sum_lis)
# list12=length_list(list11)
# print(list12)
# aveg=(sum_lis/list12)
# print("avrg is",aveg)
#
#
# # count the accuracy of element in the list
#
#
# def accuracy_list(lst):
#   x = 10
#
#   count=0
#   for i in lst:
#     if x==i:
#         count=count+1
#   return  count
# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# accuracy=accuracy_list(lst)
# print(accuracy)
#
# # find the smallest no. in list
# def smallest_no(list1):
#     list1.sort()
#     return list1[0]
# list1 = [10, 20, 4]
# smallest_no1=smallest_no(list1)
# print(smallest_no1)
#
# def multiply(list1):
#     a=1
#     for i in list1:
#         a=a*i
#     return a
# multiply_no=multiply(list1)
# print(multiply_no)
#
# # find the even no. in list
# def even_no(list2):
#     list11=[]
#     for i in list2:
#         if i%2==0:
#             list11.append(i)
#     return list11
#
# list2 = [2, 7, 5, 64, 14]
# even_no=even_no(list2)
# print(even_no)
#
#
#
# list11=[1,2,3,4,5,8,6]
# max=list11[0]
# for i in list11:
#     if i > max:
#         max=i
# print("the large  is",max)
#
#
# #Find words which are greater than given length k
# # def greater(s,k):
# #     a = []
# #     m=s.split(" ")
# #     for i in m:
# #         if  len(i) > k:
# #             a.append(i)
# #     return a
# #
# # s="hello geeks for geeks is computer science portal"
# # k = 4
# # greater_len=greater(s,k)
# # print(greater_len)


s="hello geeks for geeks is computer science portal"
k = 4
a = []
m=s.split(" ")
for i in m:
    if  len(i) > k:
            a.append(i)
print(a)


str2=""
# second large no find

def sec_large(ls):
    max=ls[0]
    max2=0
    for i in ls:
        if i > max:
            max=i

    print("max no. is",max)
    max_m=0
    for j in ls:
          if j!=max:
              if j>max_m:
                   max_m=j
    return max_m
ls=[2,4,6,5,8,7,6,9]
print("second max no. is :",sec_large(ls))

# Python program to print all even numbers in a range
# Input: start = 4, end = 15
# Output: 4, 6, 8, 10, 12, 14
def even_range(start,end):
    for i in range(start,end+2):
        if i%2==0:
             print(i)
start=4
end=15
even_range(start,end)

# Python program to count Even and Odd numbers in a List
# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2
def eve_odd(ls11):
    even_count=0
    odd_count=0
    for i in ls11:
        if i%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
    return 'even count is:',even_count,"odd count is:",odd_count
ls11=[2, 7, 5, 64, 14]
print(eve_odd(ls11))

# Python program to print positive numbers in a list
# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64

def positive(ls12):
    print("all positive no's are")
    for i in ls12:
        if i >=0:
            print(i,end=" ")

ls12=[12, -7, 5, 64, -14]
positive(ls12)

# Python program to print negative numbers in a list
# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64

def negative(ls12):
    print("all negative no's are")
    for i in ls12:
        if i < 0:
            print(i,end=" ")

ls12=[12, -7, 5, 64, -14]
negative(ls12)


# Remove multiple elements from a list in Python
# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]

def list_remove(List11,remove):
    new_list=[]
    for i in List11:
        if i not in remove:
            new_list.append(i)
    return "removed no",new_list
List11=[12, 15, 3, 10]
remove=[12,3,33]
print(list_remove(List11,remove))

# def list_remove(List11,remove):
#
# List11=[12, 15, 3, 10]
# remove=[12,3,33]
# print(list_remove(List11,remove))


# str11="abcabc"
# str22=str11[0:3]
# str23=str11[3:6]
#
# print(str22)
# print(str23)

# Method1
lista=["vaishnavi","patil",]
# list.reverse()
# print(list)

#method2
lista=list[::-1]
print(lista)
