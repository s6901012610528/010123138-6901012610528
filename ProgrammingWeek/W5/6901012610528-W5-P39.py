# code run in Thonny Python 3.14.4
# W5 : Average
a = [ 5, 9, 2 ]
sum = 0
i = 0 # index

while ( i < len(a)): # len(a) is length of a
    sum = sum + a[i] # element at index i
    i = i + 1
    
print(sum/len(a))