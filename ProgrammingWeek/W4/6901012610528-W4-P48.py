# code run in pickcode.io
# W4 : Until specified sum/volume
from processing import*
import random

def draw_circle(x, y, r):
    ellipse(x, y, r, r)

def draw_rain_drops_until(volume):
    sum_vol = 0 
    while(sum_vol < volume):
        x = random.randint(100, 400)
        y = random.randint(150, 350)
        r = random.randint(3, 30)
        draw_circle(x, y, r)
        sum_vol = sum_vol + r

def setup():
    size(500, 500)
    background(255)
    draw_rain_drops_until(500)

run()