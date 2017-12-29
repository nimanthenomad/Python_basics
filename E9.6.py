def is_abecedarian(s):
    flag = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] < s[j]:
                flag = flag + 1
    if flag == 0:
        print "this is not a abecedarian word"
    else:
        print "this is a abecedarian word"

is_abecedarian('zoomby')
