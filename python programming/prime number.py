# to find the no. is prime no. or not
# main thing is the natural no. > 1
# and it is divisible by one and itself

n=int(input("Enter the No.:"))
count=0

if n>1:
    for i in range(1,n+1):
        if (n%i) == 0:
            count = count+1
    if count == 2:
        print(" This is prime no.")
    else:
        print("This is not a prime no.")


