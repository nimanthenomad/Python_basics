
def check_fermat(a,b,c,n):
    if a**n + b**n == c**n and n>2:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No that doesen't work"
def take_input():
    a=int (input("Enter a number for a: "))
    b=int (input("Enter a number for b: "))
    c=int (input("Enter a number for c: "))
    n=int (input("Enter a number for n: "))
    return check_fermat(a,b,c,n)
take_input()
