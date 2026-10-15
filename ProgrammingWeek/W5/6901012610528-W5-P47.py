# code run in Thonny Python 3.14.4
# W5 : Maximum value
a = [ 5, 9, 2 ]
max = a[0]
i = 1 # index can start from 1?

while ( i < len(a)):
    if(max < a[i]):
        max = a[i]
    i = i + 1
        
print(max)