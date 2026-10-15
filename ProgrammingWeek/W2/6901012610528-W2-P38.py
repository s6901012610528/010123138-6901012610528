# code run in pickcode.io
# W2 : Special functions in Processing
from processing import *

def draw_balloon(x, y):
    ellipse(x,y,100,100)
    line(x, y + 50, x, y + 200)

def setup(): # will be called 1 time
    size(500,500)

def draw(): # will be called repeatedly
    draw_balloon(200,200)

run()