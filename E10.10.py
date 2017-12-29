import time


def make_word_list():
    l=[]
    t = []
    f = open('/home/urumees/Desktop/think python/module 10/alice.txt')
    start = time.time()
    for line in f:
        word = line.strip()
        t.append(word)
    l.append(time.time() - start)
    start = time.time()
    for line in f:
        word = line.strip()
        t = t + [word]
    l.append(time.time() - start)
    f.close()
    return l

def output():
    l = make_word_list()
    print "time for append methord=",l[0]
    print "time for add methord=",l[1]
    print "is time for append > time for add methord"
    print l[0] > l[1]
output()
