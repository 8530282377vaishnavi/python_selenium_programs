# patilvv.123vgs@gmail.com
import re
def Solve(s):
    path="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if re.match(path,s):
        return True
    return False

s="patilvv.123vgs@gmail.com"
print(Solve(s))

# import re
#
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


if __name__ == '__main__':
    email = "rohit.gupta@mcnsolutions.net"
    check(email)

    email = "praveen@c-sharpcorner.com"
    check(email)

    email = "inform2atul@gmail.com"
    check(email)
