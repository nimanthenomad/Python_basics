def convert(s,num):
    j = 0
    for i in s:
        temp = ord(i) + num
        s[j] = chr(temp)
        j = j + 1
    return s
a = list('cheer')
print convert(a,7)
