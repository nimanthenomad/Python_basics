import random
def make_random():
    l = []
    for i in range(1,23):
        x = random.randint(1,365)
        l.append(x)
    return l

def check(l):
    list.sort(l)
    for i in range(1,23):
        if l[i] == l[i+1]:
            return True
        return False

def count():
    same = 0
    experiments = 15
    for e in range(experiments):
        l = make_random()
        temp = check(l)
        if temp == True:
            same = same + 1
        print ("number of birthdays comes in a same day= ",same)
count()
