# code run in Thonny Python 3.14.4
# W10 : Array of Arrays
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ]

def print_all(a): # same as before (for 1D array)
    i = 0 # index
    while (i < len(a)):
        print( a[i] )
        i = i + 1

def print_2D(m):
    i = 0 # index
    while ( i < len(m)):
        print_all( m[i] ) # send an array, m[i]
        i = i + 1

print_2D( m ) # send an array, m