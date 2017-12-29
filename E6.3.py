def is_between(x,y,z):
    if x<=y:
        if x<=z:
            return True
    else:
        return False
x=input("enter value of x:")
y=input("enter value of y:")
z=input("enter value of z:")
print is_between(x,y,z)
