# code run in pickcode.io
# W3 : random()
from processing import *

def draw_circle(x, y, r):
    ellipse(x,y, r*2, r*2)

def setup():
    size(500,500)

def draw():
    x = random(100,400) # random value of x
    y = random(150,350) # random value of y
    draw_circle(x,y,30)

run()