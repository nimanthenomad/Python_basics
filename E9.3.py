def read_file():
    total = 0
    count = 0

    f=open("/home/urumees/Desktop/think python/module 9/words.txt",'r')
    forbid = forbidden()
    for line in f:
        #temp = line.strip()
        word = line.strip(forbid)
        if len(word) != 0:
            count = count + 1
    print "number of words without having forbidden letters=", count

def forbidden():
    forbid =(raw_input("enter the forbiden letters:"))
    return forbid

read_file()
