# code run in Thonny Python 3.14.4
# W4 : Password
import getpass
count = 0

while(count < 5):
    user_password = getpass.getpass("Enter your password : ")
    if user_password == "secret123":
        print("Access granted :)")
        count = 5
    else:
        print("Access denied!")
    count = count + 1