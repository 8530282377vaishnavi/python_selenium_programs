#python package
# import module from singlle package
import sys
sys.path.append("C:/Users/Sujay Sankpal/PycharmProjects/pythonProject 1/pack 1");

# Approch 1
import module1
import module2

module1.display()
module2.show()

# Approch 2
from module1 import *
from  module2 import *

module1.display()
module2.show()

# import module from two different pakagees

# Approch 2
