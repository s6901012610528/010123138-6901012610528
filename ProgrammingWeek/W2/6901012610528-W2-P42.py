# code run in pickcode.io
# W2 : Simple conditional statement (if)
from processing import *

def draw_balloon(x, y):
    ellipse(x,y,100,100)
    line(x, y + 50, x, y + 200)

def setup(): # will be called 1 time
    size(500,500)

x = 200
def draw(): # will be called repeatedly
    global x
    draw_balloon(x, 200)
    x = x + 10
    if(x > 500):
        x = 100

run()