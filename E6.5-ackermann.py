def ack(m,n):
    if m == 0 :
        return n+1
    if n == 0 :
        return ack(m-1,1)
    return ack(m-1,ack(m,n-1))
def insert():
    x=input('enter the value of m:')
    y=input('enter the value of n:')
    print ack(x,y)
insert()
