# code run in Thonny Python 3.14.4
# W4 : print_line()
def print_line(n):
    while (n > 0):
        print("*",end=" ")
        n = n-1    
    print()
    
n = int(input("number : "))
print_line(n)