# code run in Thonny Python 3.14.4
# W10 : Matrix
A = [[1, 2],\
     [3, 4]]

B = [[5, 6],\
     [7, 8]]

def addm(A, B):
    result = []
    i = 0
    while i < len(A): # loop every row
        row = []
        j = 0
        while j < len(A[i]): # loop every column
            row.append( A[i][j] + B[i][j] )
            j = j + 1
        result.append( row )
        i = i + 1
    return result

print( addm(A, B) )