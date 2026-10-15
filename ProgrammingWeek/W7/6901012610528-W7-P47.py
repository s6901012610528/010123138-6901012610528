# code run in Thonny Python 3.14.4
# W7 : Write to file
with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to Thailand\n")
    
with open("output.txt", "r") as file:
    for line in file:
        print( line )