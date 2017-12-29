"""Write a function that takes a string as an argument and displays
the letters backward, one per line."""
def print_rev(str):

    for i in str[::-1]:
        print i

def insert():
    x=list(raw_input())
    print_rev(x)
insert()
