def insert():
    x=input("enter value for a:")
    y=input("enter value for b:")
    a=max(x,y)
    b=min(x,y)
    print "gcd=",gcd(a,b)
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
insert()
