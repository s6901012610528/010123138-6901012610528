// Code run in processing 3.5.7
int A = 1;
int B = 1;
int C = 0;

void setup() {
  size(500, 800);
  frameRate(60);
}

void draw() {
  background(245);
  fill(0);
  noStroke();
  textSize(16);
  text("Trigonometry Function : y = Af[B(x+C)]", 40, 40);
  text("If  A = " + A + ",  B = " + B + "  and  C = " + C, 40, 65);

  fill(240, 170, 50);
  text("y = A sin[B(x+C)]", 40, 105);
  drawSin(50, 130, 400, 180);

  text("y = A cos[B(x+C)]", 40, 340);
  drawCos(50, 370, 400, 180);

  text("y = A tan[B(x+C)]", 40, 575);
  drawTan(50, 605, 400, 180);
}

void drawAxes(float x, float y, float w, float h) {
  float centerX = x + w / 2;
  float centerY = y + h / 2;
  stroke(0);
  strokeWeight(2);
  line(x + 20, centerY, x + w - 20, centerY);
  line(centerX, y + 10, centerX, y + h - 10);
}

void drawSin(float x, float y, float w, float h) {
  float centerX = x + w / 2;
  float centerY = y + h / 2;
  drawAxes(x, y, w, h);

  stroke(200, 40, 40);
  strokeWeight(3);
  noFill();

  beginShape();
  float px = x + 30;
  while (px <= x + w - 30) {
    float valueX = map(px, x + 30, x + w - 30, -2 * PI, 2 * PI);
    float valueY = A * sin(B * (valueX + C));
    float py = centerY - valueY * 50;
    vertex(px, py);
    px = px + 1;
  }
  endShape();

  float t = frameCount % (int)(w - 60) + x + 30;
  float valueX = map(t, x + 30, x + w - 30, -2 * PI, 2 * PI);
  float valueY = A * sin(B * (valueX + C));
  float py = centerY - valueY * 50;

  fill(240, 170, 50);
  noStroke();
  ellipse(t, py, 12, 12);
}

void drawCos(float x, float y, float w, float h) {
  float centerX = x + w / 2;
  float centerY = y + h / 2;
  drawAxes(x, y, w, h);

  stroke(200, 40, 40);
  strokeWeight(3);
  noFill();

  beginShape();
  float px = x + 30;
  while (px <= x + w - 30) {
    float valueX = map(px, x + 30, x + w - 30, -2 * PI, 2 * PI);
    float valueY = A * cos(B * (valueX + C));
    float py = centerY - valueY * 50;
    vertex(px, py);
    px = px + 1;
  }
  endShape();

  float t = frameCount % (int)(w - 60) + x + 30;
  float valueX = map(t, x + 30, x + w - 30, -2 * PI, 2 * PI);
  float valueY = A * cos(B * (valueX + C));
  float py = centerY - valueY * 50;

  fill(240, 170, 50);
  noStroke();
  ellipse(t, py, 12, 12);
}

void drawTan(float x, float y, float w, float h) {
  float centerX = x + w / 2;
  float centerY = y + h / 2;
  drawAxes(x, y, w, h);

  stroke(100);
  strokeWeight(1);

  int k = -10;
  while (k <= 10) {
    if (B != 0) {
      float asymX = (PI / 2 + k * PI) / B - C;
      if (asymX >= -2 * PI && asymX <= 2 * PI) {
        float px = map(asymX, -2 * PI, 2 * PI, x + 30, x + w - 30);
        float py = y + 20;
        while (py < y + h - 20) {
          line(px, py, px, py + 8);
          py = py + 16;
        }
      }
    }
    k = k + 1;
  }

  stroke(200, 40, 40);
  strokeWeight(3);
  noFill();

  beginShape();
  float px = x + 30;
  float oldPy = 0;
  while (px <= x + w - 30) {
    float valueX = map(px, x + 30, x + w - 30, -2 * PI, 2 * PI);
    float valueY = A * tan(B * (valueX + C));
    float py = centerY - valueY * 30;

    if (py > y + 10 && py < y + h - 10) {
      if (oldPy == 0 || abs(py - oldPy) < 100) {
        vertex(px, py);
      } else {
        endShape();
        beginShape();
        vertex(px, py);
      }
      oldPy = py;
    } else {
      endShape();
      beginShape();
      oldPy = 0;
    }
    px = px + 1;
  }
  endShape();

  float t = frameCount % (int)(w - 60) + x + 30;
  float valueX = map(t, x + 30, x + w - 30, -2 * PI, 2 * PI);
  float valueY = A * tan(B * (valueX + C));
  float py = centerY - valueY * 30;

  if (py > y + 10 && py < y + h - 10) {
    fill(240, 170, 50);
    noStroke();
    ellipse(t, py, 12, 12);
  }
}
