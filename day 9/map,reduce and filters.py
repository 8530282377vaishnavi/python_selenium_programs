#map

def new(a):
    return a*a
a=map(new,[2,3,4,5,7])
print(list(a))

def division(a):
    return a+200
x=map(division,[2,3,4,5,7])
print(list(x))

# using lambda function
# def map(lst):
#
#     c=list(map(lambda x: x+3,lst))
#     return c
#
# lst=[12,3,4,6,7]
# map12=map(lst)
# print(map)



lst=[12,3,4,6,7]
c=list(map(lambda x: x+3,lst))

print(c)


# filter
def filters(a):
    if a>=3:
        return a
j=filter(filters,[1,2,8,7,9])
print(list(j))

z=filter(lambda x:x>=3,[1,2,8,7,9])
print(tuple(z))


# reduce function
from functools import reduce
def redu(x,y):
    return x+y
a=reduce(redu,[1,2,3,4,5,6,77])
print(a)

#lambda
s=reduce(lambda a,b:a*b,[1,2,5,4,6,7])
print(s)


# map ,filters and reduce
abc=reduce(lambda x,y:x+y,map(lambda x :x*2, filter(lambda x:x<=4,[1,2,3,4,5,6])))
print("mix",(abc))

# use map() and filter together
a2=map(lambda x:x+2,filter(lambda x:(x>=4),[1,2,6,7,4,6,3]))
print("aa",list(a2))

a3=filter(lambda x:(x>=4),map(lambda x:(x*4),[1,2,3,4,5,6]))
print(list(a3))