# code run in Thonny Python 3.14.4
# W10 : Sum
m = [ [ 5, 7, 9 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ]

def sum_2Dn(m):
    sum = 0
    i = 0 # index
    while ( i < len(m)): # outer loop
        j = 0
        while ( j < len( m[i] )): # inner loop
            sum = sum + m[i][j]
            j = j + 1
        i = i + 1
    return sum

print( sum_2Dn(m) )