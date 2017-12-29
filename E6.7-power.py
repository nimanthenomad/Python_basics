import math
def is_power(a,b):
    if a%b == 0:
        for i in range(a):
            if math.pow(b,i) == a:
                return True
    else:
        return False
def insert():
    a=input("enter the value of a:")
    b=input("enter the value of b:")
    print is_power(a,b)
insert()
