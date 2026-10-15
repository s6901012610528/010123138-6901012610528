# code run in pickcode.io
# W4 : Until specified condition
from processing import*
def setup():
    size(500, 500)
    background(255)
    draw_rain_drops_until_r_below(5)

def draw_circle(x, y, r):
    ellipse(x, y, r, r)

def draw_rain_drops_until_r_below(value):
    if (value <= 3):
        value = 4
        
    r_flag = True  
    while r_flag:
        x = int(random(100, 400))
        y = int(random(150, 350))
        r = int(random(3, 30))
        
        draw_circle(x, y, r)

        if (r < value):
            r_flag = False

run()