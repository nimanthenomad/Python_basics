def check(str):
    if str[::1] == str[::-1]:
        return True
    else:
        return False
a = list('apple')
print check(a)
