# repeating sequence
# str="aabbccdd"
# str2=list(str)
# print(str2)
# #str2=str.split()
# last_seq=" "
# currunt_seq=0
# max_seq=0
# for c in str2:
#     if c==last_seq:
#         currunt_seq=+1
#         if currunt_seq>max_seq:
#             max_seq=currunt_seq
#     else:
#             currunt_seq=1
#             last_seq=c
# print(max_seq)



#
# def repeat_count(count_digit):
#     last_char = ""
#     current_seq_len = 0
#     max_seq_len = 0
#
#     for c in count_digit:
#         if c == last_char:
#             current_seq_len += 1
#             if current_seq_len==1:
#                 current_seq_len=0
#
#             if current_seq_len > max_seq_len:
#                     max_seq_len = current_seq_len
#         else:
#             current_seq_len = 1
#             last_char = c
#
#     return current_seq_len
# count_digit="aaabbbbcccddd"
# print(repeat_count(count_digit))



def repeat_count(count_digit):
    previouss=count_digit[0]
    count=0
    output_count=""
    i=0
    while i<len(count_digit):
        if count_digit[i]==previouss:
            count=count+1
        else:
            output_count=output_count+str(count)+previouss
            previouss=count_digit[i]
            count=1
        if i==(len(count_digit)-1):
            output_count = output_count + str(count) + previouss

        i=i+1
    count2 = 0
    for c in output_count:
            if c.isdigit():
                if int(c)>=2:
                    count2=count2+1
    return count2

count_digit="aaaabbbbccbggzaabb"
print(repeat_count(count_digit))


# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

list1=[12, 67, 98, 34]


# Input : list1 = [“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”]
#            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# Output : [‘a’, ‘d’, ‘h’, ‘b’, ‘c’, ‘e’, ‘i’, ‘f’, ‘g’]


def sort_ls2(list13,list14):
    z2=dict(zip(list13,list14))
    sort_by_value={x:y for x,y in sorted(z2.items(), key=lambda y: y[1])}
    lss=[]
    for i in sort_by_value.keys():
        lss.append(i)
    return lss
list13= ["a", "b", "c", "d", "e","f", "g", "h", "g"]
list14 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
print(sort_ls2(list13,list14))

# Python program to find Cumulative sum of a list
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]

def cumulative(sum):
    j=0
    lss1=[]
    for i in range(0,len(sum)):
        j= j+sum[i]
        lss1.append(j)
    return (lss1)

sum=[10,20,30,40,40]
print(cumulative(sum))


