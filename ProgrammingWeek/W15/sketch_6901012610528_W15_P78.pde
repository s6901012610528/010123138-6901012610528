// code run in processing 4.5.7
// W15 : Create Class
class Balloon {
  int x;
  int y;
  int r;
  Balloon(int x, int y, int r){
    this.x = x;
    this.y = y;
    this.r = r;
  }
  void show(){
    line(this.x, this.y, this.x, this.y + 100);
    ellipse(this.x, this.y, this.r, this.r);
  }
  void move(){
        if(this.y > width / 2){
            this.y = this.y - 2;
        }
        else{
            this.y = this.y - 4;
        }
  }
}
Balloon t;
void setup(){
  size(500,500);
  t = new Balloon(200, 200, 70);
}

void draw(){
  background(255);
  t.show();
  t.move();
}
