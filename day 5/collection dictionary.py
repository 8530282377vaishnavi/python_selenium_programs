# collection dictionary....
# dictionary is unordered but it contain index.
# dictionary is mutable(changeable).
# it contain only keys and value are store in {} curly bracket.
# main thing dictionary are like hashmap the hashmap are present in java.
#key is always (must)unique and the values may or maynot be unique.

#example 1 :
dictionary1={"product": 3000, "product2":2000, "product3":5000}   #i.e the "product" is key(always unique)and 3000 is a value
#print(dictionary1) # output :{'product': 3000, 'product2': 2000, 'product3': 5000}

# dictionary1={"product": 3000, "product2":2000, "product":5000}   #i.e the "product" is key(always unique)and 3000 is a value
# print(dictionary1) # output :{'product': 5000, 'product2': 2000}


#example 2 :
#want to acces the values from the dictionary
mydict={
    "brand": "hyundai",
    "Model": "i10",
    "year" : 2021

}
def Marge(dictionary1,mydict):
    res=dictionary1|mydict
    return  res
dictionary1 = {"product": 3000, "product2": 2000, "product3": 5000}
mydict = {
        "brand": "hyundai",
        "Model": "i10",
        "year": 2021
    }
mydict3= Marge(dictionary1,mydict)
print(mydict3)



# print(mydict)
# print(mydict["brand"]) # using key we can access the value
#by using get method
print(mydict.get("Model"))


#example 3 :
#want to change the values in dictionary
# mydict={
#     "brand": "hyundai",
#     "Model": "i10",
#     "year" : 2021
# }
# mydict["year"]=2022
# print(mydict)


#example 4 :
#want to read keys and values fron the  dictionary
# mydict={
#     "brand": "hyundai",
#     "Model": "i10",
#     "year" : 2021
# }
#
# for i in mydict:
#     print(i) #in this for loop only give the keys
#
# for i in mydict:
#     print(mydict[i]) # in this for loop only give the values
#
# for i in mydict.values():
#     print(i)  # in this for loop only give the values
#
#
# for x,y in mydict.items():
#     print(x,y)  # using item() in for loop we can read both keys and values


#example 5 :
#check the key in the dictionary is exist or not
# mydict={
#     "brand": "hyundai",
#     "Model": "i10",
#     "year" : 2021
# }
# #1st method
# if "Model" in mydict:
#     print("exist")
# else:
#     print("not exist")
# # 2nd method
# print("brand" in mydict)


#example 6 :
#number of item in dictionary
# mydict={
#     "brand": "hyundai",
#     "Model": "i10",
#     "year" : 2021
# }

#print(len(mydict))

# example 7  :
# for add new item in dictionary
#mydict["colur"]= "red" # we can add only 1 item not multiple item
#print(mydict)



# example 8 :
#removing items from dict. pop() and del ()
mydict={
    "brand": "hyundai",
    "Model": "i10",
    "year" : [2021, 2022]
}

# mydict.pop("year")
# print(mydict)

# del mydict["brand"]
# print(mydict)
#
# del mydict
# print(mydict)

# mydict.clear()
# print(mydict)


#example 9:
#i want copy the directory

mydict={
    "brand": "hyundai",
    "Model": "i10",
    "year" : 2021,
    "brand": "TATA"

}

#without copy function
# mydect2=mydict
# print(mydect2)

#with copy function
mydect2=mydict.copy()
print(mydect2)
