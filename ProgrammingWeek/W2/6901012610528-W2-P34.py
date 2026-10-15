# code run in pickcode.io
# W2 : Call it twice
from processing import *

def draw_balloon(x, y):
    ellipse(x,y,100,100)
    line(x, y + 50, x, y + 200)

def setup():
    size(500,500)
    draw_balloon(200, 200)
    draw_balloon(400, 200)

run()