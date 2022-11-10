# Access specifire * public - All people can access  your information
#private -  only you can access your information
#protector - only particular peoples which people you want to access your informations these can access your data
# we can use access specifires for both variables as well as methods

# program to illustrate public access modifire in a class
class Ajinkya:
# constractor
       def __init__(self,name, age):
           # public data members
           self.Name=name
           self.Age= age
# public member function
       def displayage(self):
          print("Age:", self.Age )

obj=Ajinkya("Vaishnavi", 25)

# accessing public data member
print("Name:", obj.Name)
print("Age :", obj.Age)
# calling public member function of the class
obj.displayage()

# priavate access specifires and modifire   __ is used for private access specifire
class geek:

    __name= None
    __roll= None
    __branch = None
# constactor
    def __init__(self,name,roll, branch):
        self.__name=name
        self.__roll=roll
        self.__branch= branch
        #private member function
    def __displayDetails (self):

# accessing the private data members
       print("Name:", self.__name)
       print("Roll:", self.__roll)
       print("Branch:", self.__branch)
        #access private member function
    def accessprivatefunction(self):
       self.__displayDetails()
object= geek("Vaishnavi", 123442, "Information technology")
# calling public member function of a class
object.accessprivatefunction()


# protected access specifires
# their is only use _ single underscore

class geek:

    _name= None
    _roll= None
    _branch = None
# constactor
    def __init__(self,name,roll, branch):
        self._name=name
        self._roll=roll
        self._branch= branch
        #protected  member function
    def _displayDetails (self):

# accessing the protected data members
       print("Name:", self._name)
       print("Roll:", self._roll)
       print("Branch:", self._branch)
        #access protected  member function
    def accessprivatefunction(self):
       self._displayDetails()
object= geek("Vaishnavi", 123442, "Information technology")
# calling public member function of a class
object.accessprivatefunction()



