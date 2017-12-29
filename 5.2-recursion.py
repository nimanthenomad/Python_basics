def recursive(s,n):
    if n <= 0:
        print "end of recursion.."
        return
    print s
    recursive(s,n-1)
s='hello'
n=2
recursive(s,n)
