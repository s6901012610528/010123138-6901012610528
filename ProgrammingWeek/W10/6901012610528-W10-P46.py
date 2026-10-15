# code run in Thonny Python 3.14.4
# W10 : Nested Loop
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ]

def print_all(a): # same as before (for 1D array)
    i = 0 # index
    while (i < len(a)):
        print( a[i] )
        i = i + 1

def print_2Dn(m):
    i = 0 # index
    while ( i < len(m)): # outer loop
        j = 0
        while ( j < len( m[i] )): # nested loop
            print( m[i][j] )
            j = j + 1
        i = i + 1

print_2Dn( m ) # send an array, m