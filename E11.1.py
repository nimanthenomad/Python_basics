def words():
    word_dict = dict()
    f = open("/home/urumees/Desktop/think python/alice.txt")
    i = 0
    for line in f:
        word = line.strip()
        if word not in word_dict:
            word_dict[i] = word
            i = i + 1
    print word_dict
    f.close()
words()
