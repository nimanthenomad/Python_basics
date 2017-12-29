from __future__ import division
def square_root(a):
    C = 0.00000001
    x= a - 1
    while True:
        print x
        y =( x + (a / x)) / 2
        if abs(y - x) < C:
            break
        x = y
square_root(49)
