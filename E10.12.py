def reverse_pair():
    t = ['apple','bat','cat','tab','elppa','tac']
    '''f = open('/home/urumees/Desktop/think python/module 10/alice.txt')
    for line in f:
        word = line.strip()
        t = t + [word]'''
    for word in range(len(t)):
        for item in range(word+1,len(t)):
            print list(t[word])[::1]
            print list(t[item])[::-1]
            if list(t[word])[::1] == list(t[item])[::-1]:
                print t[item]
    #f.close
reverse_pair()
