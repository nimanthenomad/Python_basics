'''Use incremental development to write a function called hypotenuse that
returns the length of the hypotenuse of a right triangle given the lengths
of the two legs as arguments. Record each stage of the development process
as you go.'''
import math
def hypotenuse(x,y):
    return math.sqrt(x**2+y**2)
x=input("enter the value of base:")
y=input("enter the value of latitude")
print "hypotenuse length=:",hypotenuse(x,y)
