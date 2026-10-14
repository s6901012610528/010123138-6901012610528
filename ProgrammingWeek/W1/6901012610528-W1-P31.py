# code run in pickcode.io
# W1 : Use Variables
from processing import *

def setup():
    size(500,500)
    x = 200 # upper left x
    y = 100 # upper left y
    line(x, y, x, y+200)
    line(x+100, y, x+100, y+200)

    middle = y + 100
    line(x, middle, x+100, middle)

run()