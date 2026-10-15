# code run in Thonny Python 3.14.4
# W7 : Read a line
with open("document.txt", "r") as f:
    line = f.readline() # Read a line from file
    while line :
        print( line ) # print it
        line = f.readline() # read the next line