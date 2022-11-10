

def reverse_string(string):
    str2=string[::-1]
    print(str2)
    str3=str2.split(" ")
    str3.reverse()

    return str3

string="Hello world with python"
List=[]

reverse=reverse_string(string)
print(reverse)

string="Hello world with python"

# remove degits from string
# method 1
string2="Vais12hn89avi12"
string3=""
for i in string2:
    if  i<='9':
        continue
    else:
        string3=string3+i
print(string3)

#method2
# for i in string2:
#     if not i.isdigit():
#         print(i,end="")




def reverse_str(str11):
    str12=str11[::-1]
    str13=str12.split()
    str13.reverse()
    return str13


str11="Hello world python"
print(reverse_str(str11))




        










