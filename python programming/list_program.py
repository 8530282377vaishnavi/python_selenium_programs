#1. Write a Python program to sum all the items in a list.
list11=[1,3,2,4,5,6,7]
sum=0
for i in list11:
    sum=sum+i
print("total sum is :",sum)

#  Write a Python program to multiply all the items in a list.
multiply=1
for i in list11:
    multiply=multiply*i
print("total multiplication is", multiply)

# Write a Python program to get the largest number from a list.
max=list11[0]
for i in list11:
    if i>max:
        max=i
print("this is largest no",max)


# Write a Python program to get the smallest number from a list
for i in list11:
    if i<max:
        max=i
print("This is smallest no",max)

# 5. Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
Sample_List = ['abc', 'xyz', 'aba', '1221']
count=0
for i in Sample_List:
    if len(i)>=2 and i[0]==i[-1]:
        count=count+1
print(count)

# 6. Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given
# list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



def last(n):
    return n[-1]
def sorted_tuple(tuples):
    return (sorted(tuples,key=last))

tuples= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted_tuple(tuples))

# Write a Python program to remove duplicates from a list.
list1=[10,20,40,30,20,10,70,80,90,80,70]
list2=set(list1)
print(list2)

# method 2
unique=[]
for i in list1:
    if i not in unique:
        unique.append(i)
print(unique)

#  Write a Python program to check a list is empty or not.
def check_list(lis):
    if lis==[]:
        return True
    else:
        return False
lis=[1,2,3]
print(check_list(lis))
mylis=[]
# mylis=lis.copy()
print(mylis.append(lis))
print(mylis)

# Write a Python program to find the list of words that are longer than n from a given list of words.
# "The quick brown fox jumps over the lazy dog"
def longer_word(words,n):
    lis2=[]
    a=words.split()
    for i in a:
        if len(i)>n:
            lis2.append(i)
    return lis2

words="my name is vaishnavi"
n=3
print(longer_word(words,n))

# Write a Python function that takes two lists and returns True if they have at least one common member.
def common_no(atleast,num):
    for i in atleast:
        for j in num:
            if i==j:
              return True

atleast=[1,2,3,5,4,6]
num=[5,9,8,7,0,11]
print(common_no(atleast,num))

#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# Click me to see the sample solution
# method 1
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Sample_List2=[]
for i in Sample_List:
    if Sample_List.index(i)==0 or Sample_List.index(i)==4 or Sample_List.index(i)==5:
        continue
    Sample_List2.append(i)
print(Sample_List2)

# method 2
for i in Sample_List:
    if Sample_List.index(i)==0 or Sample_List.index(i)==4 or Sample_List.index(i)==-1:
        Sample_List.pop(0)
        Sample_List.pop(4)
        Sample_List.pop(-1)
print(Sample_List)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def remove_even(eve_odd):
    eve_odd2=[]
    for i in eve_odd:
        if i%2==0:
            continue
        eve_odd2.append(i)
    return eve_odd2
eve_odd=[1,3,2,4,5,6,7,8,9]
print(remove_even(eve_odd))


# . Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)
# Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).
l=[]
for i in range(1,30+1):
    l.append(i*i)
print(l)
print("firs 5 elements :",l[:5])
print("last 5 elements :",l[-5:])

# Write a Python program to generate and print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included).
v=[]
for a in range(1,30+1):
    if a==1 or a==2 or a==3 or a==4 or a==5:
         continue
    v.append(a**2)
print(v)

# Write a Python program to generate a 3*4*6 3D array whose each element is *.
arrey=[[["*" for column in range(6)]for column in range(4)]for row in range(3)]
print(arrey)
print()
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

#  Write a Python program to generate all permutations of a list in Python.
def permutation(abc):
    size=len(abc)
    aa=abc+abc
    temp=[]
    for i in range(size):
        for j in range(size):
            print(aa[i+j],end=" ")
        print()
permutation(abc="abc")

#
import itertools
print(list(itertools.permutations(["a","b","c"])))

# Write a Python program to get the difference between the two lists.
list_diff1=[1, 3, 5, 7, 9]
list_diff2=[1, 2, 4, 6, 7, 8]
list_diff1_set=set(list_diff1)
print(list_diff1_set)
list_diff2_set=set(list_diff2)

lis11=(list_diff1_set & list_diff2_set)
lis11.remove(1)
for i in list_diff1:
    if i not in list_diff2:
              list_diff2.append(i)

print(set(list_diff2))

diff2=list(set(list_diff1) - set(list_diff2))
print("1",diff2)
diff1=list(set(list_diff2) - set(list_diff1))
print("2",diff1)
total_diff=diff2+diff1
print(total_diff)

list111 = [1, 3, 5, 7]
list222=[1, 2, 4, 6, 7]
diff_list1_list2 = list(set(list111) - set(list222))
print(diff_list1_list2)
diff_list2_list1 = list(set(list222) - set(list111))
total_diff = diff_list1_list2 + diff_list2_list1
print("total differance is",total_diff)


# 20. Write a Python program access the index of a list.
for num_index,num_value in enumerate (list222):
    print(num_index,num_value)

# Write a Python program to convert a list of characters into a string
lis_str=["ab", "bc","ac", "ca"]
char=" ".join(lis_str)
print(char)

# 21. Write a Python program to convert a list of characters into a string.
print(lis_str.index("ab"))


#22. Write a Python program to find the index of an item in a specified list.
