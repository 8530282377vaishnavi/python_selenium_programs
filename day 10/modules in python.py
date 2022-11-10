# module is a python file (.py) containing a set of functions you want to include in your application
# A module contents are accessed with the import statement 
#Approch1

# import operations
# operations.add(200,400)
# operations.mul(300,88)

#Approch 2
from operations import add,mul
add(1000,4000000)
mul(500,600)

# Approch 3
from operations import *
add(1000,4000000)
mul(500,600)


# Approch
import animal
animal.fly()
animal.Colour()

import Birds
Birds.Fly()
Birds.colour()

from animal import fly,Colour
from Birds import Fly,colour

fly()
Colour()
Fly()
colour()


##approch 3
from animal import *
from Birds import *

fly()
Colour()
Fly()
colour()

import animal  #  using class and object also perform  module
a=A()

a.Birds()
a.Animal()


# how to use dir keyword
import Birds
print(dir(Birds))




str1="Sachin"
str2="patil"
print(str1+str2)