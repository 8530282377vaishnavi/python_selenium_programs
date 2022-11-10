# List Collection Datatype program's
def swap(List):
    List[0],List[-1]=List[-1],List[0]
    return (List)
List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
List2=swap(List)
print(List2)

#Python program to swap two elements in a list
def swaplist(List):
    List[1],List[5]=List[5],List[1]
    return List

List = ["vaishnavi", "ajinkya", "santoshi", "rupali", "nayana", "patil"]
List3=swaplist(List)
print(List3)

# ways of find the length of list
def Length(List):
    return (len(List))
List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
len=Length(List)
print("The No. of items in list",len)


def length_list(List):
  count=0

  for i in List:
    count=count+1
  return (count)
List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
length2=length_list(List)
print("The No. of items in list",length2)

#Check if element exists in list in Python
def exist_element(List):
    if "ajinkya" in List:
        return True
    else:
        return False
List=["vaishnavi","ajinkya","santoshi","rupali","nayana","patil"]
exist=exist_element(List)
print(exist)


#find the second largest no in list

def second_max(list1):
    max_var=max(list1)
    list1.remove(max_var)
    print(list1)
    return max(list1)



list1 = [ 20,4,12,10]
second_maxno=second_max(list1)
print("The second max no. is ",second_maxno)

def second_max(list1):
    list1.sort()
    list2=list1[-2]
    return list2

list1 = [ 20,4,12,10]
second_maxno=second_max(list1)
print("The second max no. is ",second_maxno)


def second_max(list1):
    max1=max(list1)
    max_ver=0
    for i in list1:
        if i!=max1:
            if i>max_ver:
                max_ver=i
    return max_ver




list1 = [ 20,4,16,10]
second_maxno=second_max(list1)
print("The second max no. is ",second_maxno)



def sum_list(list11):
    a=0

    for i in list11:
        a=a+i
    return a



list11=[4, 5, 1, 2, 9, 7, 10, 8]
sum_lis=sum_list(list11)
print("sum of all no",sum_lis)
list12=length_list(list11)
print(list12)
aveg=(sum_lis/list12)
print("avrg is",aveg)


# count the accuracy of element in the list


def accuracy_list(lst):
  x = 10

  count=0
  for i in lst:
    if x==i:
        count=count+1
  return  count
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
accuracy=accuracy_list(lst)
print(accuracy)

# find the smallest no. in list
def smallest_no(list1):
    list1.sort()
    return list1[0]
list1 = [10, 20, 4]
smallest_no1=smallest_no(list1)
print(smallest_no1)

def multiply(list1):
    a=1
    for i in list1:
        a=a*i
    return a
multiply_no=multiply(list1)
print(multiply_no)

# find the even no. in list
def even_no(list2):
    list11=[]
    for i in list2:
        if i%2==0:
            list11.append(i)
    return list11

list2 = [2, 7, 5, 64, 14]
even_no=even_no(list2)
print(even_no)
