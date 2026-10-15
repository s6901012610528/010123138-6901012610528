# code run in pickcode.io
# W5 : Parallel Arrays
from processing import*
x = [ 1, 4, 2, 9, 3 ]
y = [ 5, 3, 1, 7, 2 ]

def draw_circle(x, y ,r):
    ellipse(x, y, r, r)

def setup():
    size(500,500)
    
def draw():
    background(255)
    i = 0
    while (i < len(x)):
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + 2
        x[i] = x[i] + 2 # need it?
        i = i + 1
        
run()