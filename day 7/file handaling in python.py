# file handaling in python
#writing the content in file
# file=open('C:\python\python.txt','w' ) # open the file for writing
# file.write("Welcome in Python ")
# file.write("world\n")
# file.write('My name is vaishnavi \n') # /n is used for writing the content in next line
# file.close()


# reading the content from file
file=open('C:\python\python.txt', 'r') # open the file for reading
#print(file.read())  # reading the entire content in the file
# print(file.read(10)) # reading the no. of characters in the file
# file.close()
# print(file.readline()) # read only first line in the file
# print(file.readlines()) # reading the entire content in the file in the array format ['Welcome in Python world\n', 'My name is vaishnavi \n']
# file.close()


# append the data in file
# file= open('C:\python\python.txt', 'a') # i want add new line in existing file  (append the data)
# file.write("I want to learn Python language \n")
# file.close()

# reading all the data from file using for loop statment
file= open('C:\python\python.txt', 'r')

for l in file:
    print(l)
file.close()
