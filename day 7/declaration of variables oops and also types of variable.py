# declaration of variables inside  the class

class myclass:
    a,b=100,200  # these are class variables and these are access by using self keyword

    def add(self):
        print(self.a+self.b)
    def multipy(self):
        print(self.a*self.b)
mc=myclass()
mc.add()
mc.multipy()

#  There are three types of variables
# 1. local variables  ---> the variable with in the method called local variable
# 2. class variables  ---> the variable with in the class called class variable
# and 3. global variable ---> the variable with in the file called as global variable. (we can use every ware )

a,b=100,200 # this is global variable present outside the class but access everyware

class myclass:
    x,y=20,70   # this is class variable
    def addition(self,i,j):    # this is local variable
        print(i*j)  # accessing the local variable
        print(self.x+self.y) # accessing the class variable  (only class variable needs keyword to access )
        print(a+b)  # accessing the global variable
mc=myclass()
mc.addition(30,500)


# accessing the global variable, local variable and class variable with the same name

a,b=100,200

class myclass:
    a,b=20,100
    def add(self,a,b):
        print(a+b)   # accessing the local variable
        print(self.a+self.b) # accessing the class variable
        print(globals()['a']+globals()['b']) # accessing the global variable by using the function globals()[value]  (if names are different)
mc=myclass()
mc.add(300,400)



