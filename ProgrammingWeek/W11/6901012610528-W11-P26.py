# code run in pickcode.io
# W11 : Create a class
from processing import*

class Balloon: # specify class name
    def __init__(self, x, y, r): # specify constructor
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        line(self.x, self.y, self.x, self.y + 100)
        ellipse(self.x, self.y, self.r, self.r)

    def move(self):
        if(self.y > width / 2):
            self.y = self.y - 2
        else:
            self.y = self.y - 4

b = Balloon(400, 600, 50)
def setup():
    size(1000, 1000)
    print(b)

def draw():
    background(255)
    b.show()
    b.move()
    
run()
