// code run in processing 4.5.7
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
    this.x = this.x + 2;
    if(this.x > 500){
      this.x = 0;
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
