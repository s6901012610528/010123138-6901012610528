# code run in Thonny Python 3.14.4
# W2 : To Try
def show_info():
    print("This program will calculate area")
    print("given width and length")
    print("created by THanawat")
    print()
    
def get_width():
    width = float(input("width : "))
    return width
    
def get_length():
    length = float(input("length : "))
    return length

def cal_area(W,L):
    area = W*L
    return area

def show_area(area):
    print(f"Area is {area:.2f} Square Meter")
    
def show_area_in_SqWa(area):
    area_SQW = area/4
    print(f"Area is {area_SQW:.2f} Square Wah")

show_info()
width = get_width()
length = get_length()
area = cal_area(width,length)
show_area(area)
show_area_in_SqWa(area)