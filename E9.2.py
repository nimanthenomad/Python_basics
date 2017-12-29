from __future__ import division
def read_file():
    total = 0
    count = 0

    f=open("/home/urumees/Desktop/think python/module 9/words.txt",'r')

    for line in f:
        word = line.strip()
        total = total + 1
        count = count + has_not_e(word)
    print ("percentage of words without having 'e' in the file=",(count/total)*100)

def has_not_e(word):
    if 'e' not in word :
        return 1
    else:
        return 0


read_file()
