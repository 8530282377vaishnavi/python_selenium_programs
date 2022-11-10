'''def pattern(n):
    k =2 * n-2
    for i in range(0,n):
        for j in range(0, k):
            print(end="")
        k=k - 1
        for j in range(0,i+1):
            print("*",end="")
        print()
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end="")
        k =k+1
        for j in range (0,i+1):
            print("*",end="")
    print()
pattern(5)'''

# square pattern
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="   ")
#     print()

# incresing trangle pattern
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="  ")
#     print()
# # decrease trangle pattern
n=5
for i in range(n):
    for j in range(i,n):
        print("*", end="  ")
    print()



# for right side trangle (decreasing angle of space and increasing angle of star
# n=5
# for i in range(n):
#
#     for j in range(i,n):
#         print(" ", end=" ")
#
#     for j in range(i+1):
#         print("*", end=" ")
#
#     print()

# increasing angle of space and decreasing angle of star
n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")

    print()

#hill pattern
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#
#     for j in range(i):
#         print("*", end=" ")
#
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# reverse hill  pattern
# n=5
# for i in range(n):
#
#     for j in range(i+1):
#         print( ' ', end=' ' )
#
#     for j in range(i,n-1):
#         print( '*', end=' ')
#
#     for j in range(i,n):
#         print( '*', end=' ')
#     print()

# n=5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for i in range(i+1):
#         print("*" , end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*",end=" " )
#     for j in range(i,n):
#         print("*", end=" ")
#     print()


# holow star pattern
for i in range(7):
    for j in range(7):
        if i+j==3 or i-j==3 or j-i==3 or i+j==9:
            print("*", end="   ")
        else:
            print(end="   ")
    print()