# code run in Thonny Python 3.14.4
# W7 : with statement
with open("example.txt", "r") as file:
    content = file.read()
    print( content )

# Recommended Way
# The file will be automatically closed