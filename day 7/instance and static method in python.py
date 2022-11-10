# this declaration of methods and aab with in the class instance method and static method
class myclass:
    def m1(self):
        print("instance method") # this is instanc method

    @staticmethod #we should mention the annotation for static method
    def m2():     # dont use self keyword for static method
       print("static method")

mc=myclass() #for instance we should store the class in varible
mc.m1()
myclass.m2() # in static we can directly use the class their no need to store in variable















