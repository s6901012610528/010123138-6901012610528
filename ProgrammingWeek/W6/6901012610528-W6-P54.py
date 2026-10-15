# code run in pickcode.io
# W6 : Display String (graphic-mode)
from processing import*

def setup():
    size(500,500)
    
def draw():
    background(255)
    fill(0) # text color
    textSize(100) # text size :)
    text("ABC", mouseX, mouseY)
    
run()