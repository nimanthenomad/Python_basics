def print_hist(s):
    l = histogram(s).keys()
    l.sort()
    print l

def histogram(h):
    d = dict()
    for c in h:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print_hist('brontosaurus')
