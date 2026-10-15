# code run in Thonny Python 3.14.4
# W10 : Count
m = [ [ 5, 7, 3 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ]

def count_2Dn(m , x):
    count = 0
    i = 0 # index
    while ( i < len(m)): # outer loop
        j = 0
        while ( j < len( m[i] )): # inner loop
            if (m[i][j] == x):
                count = count + 1
            j = j + 1
        i = i + 1
    return count

print( count_2Dn(m , 3) )