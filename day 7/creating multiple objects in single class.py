#
class Myclass():
    def __int__(self, n,r,m):
        self.name=n
        self.rlo=r
        self.marks=m
    def display(self):
        print("name is:",self.name)
        print("roll_no is:", self.rlo)
        print("Marks is:", self.marks)

nl=["A", "B", "c", "d"]
rl=[1,2,3,4]
ml= [100,70,60,69]
obj1=[]
# for i in range (0,4):
#     obj1.append(Myclass(nl[i],rl[i], ml[i]))
# obj1[2].display()

#
#  in single class we can creat multiple objects and they are store in differnt memory location
class myclass:
    def display(self):
        print("hello good morning")

object1= myclass()    # named object the object which is created by referance name  AND ALso called referance variable
object1.display()

object2=myclass()
object2.display()

object3=myclass()
object3.display()
object1=object3
print(id(object1))
print(id(object2))
print(id(object3))

print(id(object1))



#namelass object
myclass().display() #using the class (nothing but object) calling the function


# how to check the memory location of object







