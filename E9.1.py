def read_file():
    f=open("/home/urumees/Desktop/think python/module 9/words.txt",'r')
    for line in f:
        word = line.strip()
        if len(word) > 20:
            print word
read_file()
