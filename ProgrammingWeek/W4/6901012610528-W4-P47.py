# code run in pickcode.io
# W4 : Fixed number
from processing import*
import random

def setup():
    size(500, 500)
    background(255) 
    n = random.randint(10, 50) 
    draw_rain_drops(n)

def draw_circle(x, y, r):
    ellipse(x, y, r, r)

def draw_rain_drops(n):
    i = 0
    while (i < n): 
        x = random.randint(100, 400)
        y = random.randint(150, 350)
        r = random.randint(3, 30)
        draw_circle(x, y, r)
        i = i + 1

run()