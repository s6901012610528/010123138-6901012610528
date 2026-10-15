# code run in Thonny Python 3.14.4
# W7 : Append to file
with open("output.txt", "a") as file:
    file.write("ECE\n")
    file.write("KMUTNB\n")
    
with open("output.txt", "r") as file:
    for line in file:
        print( line )