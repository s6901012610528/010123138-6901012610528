# code run in pickcode.io
# W3 : Draw on the same side as the mouse
from processing import *

def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
    diffy = abs( y1-y2 )
    result = sqrt( diffx*diffx + diffy*diffy )
    return result

def draw_balloon(x, y, r):
    ellipse(x,y, r*2, r*2)
    line(x, y+50, x, y+200)

def setup():
    size(500,500)

x = 200
def draw():
    global x
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    line(x,200, x + d, 200)

    if(mouseX > x):
        line(x,200, x + d, 200)
    else:
        line(x,200, x - d, 200)

run()