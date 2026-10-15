# code run in Thonny Python 3.14.4
# W10 : Function and Array
a = [ 5, 9, 2 ]
b = [ 6, 1, 8 ]

def print_all(a):
    i = 0
    while (i < len(a)):
        print( a[i] )
        i = i + 1

def add_all(a, x):
    i = 0
    while ( i < len(a)):
        a[i] = a[i] + x
        i = i + 1
        
def add_x(a, x):
    a = a + x
    return a

add_all(a, 3)
print_all(a)

add_all(b, 2)
print_all(b)

a = 5
print(add_x(a, 3))

b = 2
print(add_x(b, 7))
