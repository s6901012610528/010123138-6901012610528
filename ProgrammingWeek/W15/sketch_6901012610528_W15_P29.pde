// code run in processing 4.5.7
// W15 : Animation

void draw_balloon(int x, int y){
  ellipse(x, y, 100, 100);
  line(x, y+50, x, y+200);
}

void setup(){
  size(500,500);
}

void draw(){
  background(255);
  int x = (int)random(100,400);
  draw_balloon(x, 200);
  x = x + 10;
  if (x > 500){
    x = 100;
  }
}
