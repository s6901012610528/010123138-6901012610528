# code run in Thonny Python 3.14.4
# W6 : String Concatenation ( + )
s = "Hello"
t = ""
i = 0
while(i < len(s)):
    t = t + str(i) + "\t" + s[i] + "\n"
    i = i + 1
    print( t )