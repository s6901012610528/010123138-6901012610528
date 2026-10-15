# code run in Thonny Python 3.14.4
# W7 : Process line-by-line
a = []
with open("number.txt", "r") as file:
    for line in file:
        num = int( line )
        a.append( num )
    print( a )

# [5, 2, 7]