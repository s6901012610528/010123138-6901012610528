# code run in Thonny Python 3.14.4
# W5 : Problem Solving
a = [-1, 5, 9, 3]
i = 0
tmp = a[0]

while(i < len(a)):
    if(tmp < a[i]):
        tmp = a[i]
    i = i + 1
    
print(tmp)