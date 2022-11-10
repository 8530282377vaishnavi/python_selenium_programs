# merging two dictionary
def Marge(dict1,dict2):
    res=dict1|dict2
    return res
dict1={1:"vaishnavi",2:"Vishwas",3:"Santoshi"}
dict2={4:"Ajinkya",5:"Rupali",6:"nayana"}
dict3=(Marge(dict1,dict2))
print(dict3)
