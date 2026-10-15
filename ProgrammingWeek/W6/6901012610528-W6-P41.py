# code run in Thonny Python 3.14.4
# W6 : ASCII code
s = "Hello" # similar to array of characters
i = 0
while(i < len(s)):
    print( ord(s[i]) )
    i = i + 1

print( ord("a") ) # Output: 97
print( chr(97) ) # Output a