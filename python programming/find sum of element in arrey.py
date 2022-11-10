# find the sum of element in array

arr = [1234567]
print(sum(arr))

# find the common char. betn two strings

def Common_letter():
   v="vaishnavi"
   A="ajinkya"
   v1=set(v)
   A2=set(A)

   s1=(v1 & A2)
   print(s1)
Common_letter()


#count the frequency of words in a string
def count_freq():
    Words="sheena loves eating apple and mango and her sister also loves eating apple and mango "
    Words2=Words.split()
    dicti={}
    for i in Words2:
        if i not in dicti.keys():
            dicti[i]=0
        dicti[i]=dicti[i]+1
    print(dicti)
count_freq()


# Words1=Words.split()
#     dicti={}
#     for i in Words1:
#        if i not in dicti.keys():
#           dicti[i]=0
#        dicti[i]=dicti[i]+1
#     print(dicti)
#
# count_freq()
