def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@my_decorator
def world():
    print("world")
world()

