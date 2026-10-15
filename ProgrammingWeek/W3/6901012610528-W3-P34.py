# code run in pickcode.io
# W3 : Use it in our function
from processing import *

def draw_circle(x, y, r):
    ellipse(x,y, r*2, r*2)

def draw_balloon(x, y):
    draw_circle(x,y, 50) # easier to understand?
    line(x, y+50, x, y+200)

def setup():
    size(500,500)
    draw_balloon(200,200)

run()
