# Daniel Shiffman
# http:#codingtra.in
# http:#patreon.com/codingtrain

# Double Pendulum
# https:#youtu.be/uWzPe_S-RVE

r1 = 200
r2 = 200
m1 = 40
m2 = 40
a1 = PI/2
a2 = PI/2
a1_v = 0
a2_v = 0
g = 1

px2 = -1
py2 = -1
li = []
#cx, cy

canvas = PGraphics()

def setup():
  global cx, cy
  size(900, 600)
  fullScreen()
  cx = width/2
  cy = 200
  canvas = createGraphics(width, height)
  canvas.beginDraw()
  canvas.background(255)
  canvas.endDraw()

counter = 0
def draw():
  global a1, a2, r1, r2, m1, m2, g, a1_v, a2_v, px2, py2, cx, cy, li, counter
  background(0)
  imageMode(CORNER)
  image(canvas, 0, 0, width, height)

  num1 = -g * (2 * m1 + m2) * sin(a1)
  num2 = -m2 * g * sin(a1-2*a2)
  num3 = -2*sin(a1-a2)*m2
  num4 = a2_v*a2_v*r2+a1_v*a1_v*r1*cos(a1-a2)
  den = r1 * (2*m1+m2-m2*cos(2*a1-2*a2))
  a1_a = (num1 + num2 + num3*num4) / den

  num1 = 2 * sin(a1-a2)
  num2 = (a1_v*a1_v*r1*(m1+m2))
  num3 = g * (m1 + m2) * cos(a1)
  num4 = a2_v*a2_v*r2*m2*cos(a1-a2)
  den = r2 * (2*m1+m2-m2*cos(2*a1-2*a2))
  a2_a = (num1*(num2+num3+num4)) / den

  translate(cx, cy)
  stroke(0)
  strokeWeight(5)

  x1 = r1 * sin(a1)
  y1 = r1 * cos(a1)

  x2 = x1 + r2 * sin(a2)
  y2 = y1 + r2 * cos(a2)

  fill(25,25,255)
  stroke(25,25,255)
  line(0, 0, x1, y1)
  ellipse(x1, y1, m1, m1)

  line(x1, y1, x2, y2)
  ellipse(x2, y2, m2, m2)

  a1_v += a1_a
  a2_v += a2_a
  a1 += a1_v
  a2 += a2_v

  # a1_v *= 0.99
  # a2_v *= 0.99

  canvas.beginDraw()
  #canvas.background(0, 1)
  canvas.translate(cx, cy)
  canvas.stroke(0)
  if (frameCount > 1):
    canvas.line(px2, py2, x2, y2)
  
  canvas.endDraw()
  
  col = (25,25,255)
  #col = (random(0,255), random(0,255), random(0,255))
  
  li.append((px2,py2,col))
  
  if counter == 1:
      li.remove(li[0])
      counter += 1
  
  for i in range(len(li)):
    if i < len(li)-1:
        strokeWeight(1)
        stroke(li[i][2][0], li[i][2][1], li[i][2][2])
        fill(li[i][2][0], li[i][2][1], li[i][2][2])
        line(li[i][0], li[i][1], li[i+1][0], li[i+1][1])
  px2 = x2
  py2 = y2
  if counter == 0: 
    counter += 1
  #saveFrame('images/Anim############.png')
