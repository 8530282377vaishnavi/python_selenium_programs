n=5

for i in range (n):
     for j in range(i+1):
         print(j+1,end=" ")
     print()

for i in range(n):
    for j in range(i,n-1):
        print(j+1,end=" ")
    print()

