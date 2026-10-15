# code run in Thonny Python 3.14.4
# W7 : File Operations
# Open a text file for reading ("r")
file = open("example.txt", "r")

# Read the entire content and print it
content = file.read() # call a method
print( content ) # Content is a string

# Always close the file when finished
file.close()
