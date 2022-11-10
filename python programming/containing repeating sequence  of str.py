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
def count_str(str):
    counter=1
    ch=str
    maincount=0
    a=len(str)
    for i in a:
        if str==ch:
            counter=counter+1
        else:
            if (counter>1):
                maincount+=1
                ch=str
        if (counter>1):
                maincount=maincount+1
                return maincount



str="aabbcc"
count_str(str)

