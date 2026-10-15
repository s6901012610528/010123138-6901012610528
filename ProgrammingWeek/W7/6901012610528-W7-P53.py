# code run in Thonny Python 3.14.4
# W7 : Try and catch exception
try:
    with open("A1.txt", "r") as f:
        for line in file:
            print(line)

except FileNotFoundError:
    print("Error: A1.txt is not found")