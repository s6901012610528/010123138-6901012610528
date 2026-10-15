# code run in Thonny Python 3.14.4
# W11 : File name and Path
import os

print( os.getcwd( ) )
print( os.listdir( ) )

print( os.path.exists("output.txt") ) # the path exists ?
print( os.path.isfile("output.txt") ) # is it a file?
print( os.path.isdir("output.txt") ) # is it a directory?

file_size = os.path.getsize( "output.txt" )
print( "File Size is :", file_size, "bytes" )