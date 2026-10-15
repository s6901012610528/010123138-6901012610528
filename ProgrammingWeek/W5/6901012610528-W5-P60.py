# code run in pickcode.io
# W5 : Start from empty list
from processing import*
n = 108
x = [ ]
y = [ ]
s = [ ]

def draw_circle(x, y ,r):
    ellipse(x, y, r, r)

def setup():
    size(1000,1000)
    i = 0
    while ( i < n ):
        x.append( random(100,900) )
        y.append( random(100,500) )
        s.append( random(1,5) )
        i = i + 1
    
def draw():
    background(255)
    i = 0
    while ( i < n ):
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + s[i]
        i = i + 1
        
run()