# code run in pickcode.io
# W4 : Fix number
from processing import*
def setup(): 
    size(500,500) 
 

z = 100
def draw_ladder(x,y,s): 
    global z
    line(x,y,x,y+s)
    line(x+z,y,x+z,y+s) 
    while(y < 350): 
        y = y + 50 
        line(x,y,x+z,y) 
        line(x,y,x,y+s)
        line(x+z,y,x+z,y+s) 
 
def draw(): 
    draw_ladder(100,100,50)

run()