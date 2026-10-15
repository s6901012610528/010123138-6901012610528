# code run in pickcode.io
# W4 : Change to vertical lines
from processing import*
import random

def setup():
    size(500,500)
    x1 = random.randint(100, 400)
    y1 = random.randint(150, 350)
    x2 = random.randint(100, 400)
    y2 = random.randint(150, 350)
    draw_vertical_lines(x1, y1, x2, y2)
    
def draw_vertical_lines(x1, y1, x2, y2):
    if (x1 == x2):
        line(x1, y1 - 50, x1, y1 + 50)
        return
        
    space = abs(x1 - x2) / 5  
    
    if (x1 > x2):
        x1, x2 = x2, x1

    while (x1 < x2):
        line(x1, y1 - 50, x1, y1 + 50)
        x1 = x1 + space

run()