import turtle
b=turtle.Screen()
ok = turtle.Turtle()

b.bgcolor("orange")
ok.pencolor("red")

def drawSquer(length):
    for i in range (4):
     ok.forward(length)
     ok.right(90)
def drawTriangle(length):
    
    for a in range (3):
     ok.forward(120)
     ok.left(120)

drawSquer(250)
drawTriangle(250)

ok.penup()
ok.backward(400)
ok.pendown()

for a in range(5):
    drawSquer(50)
    ok.forward(50)
    ok.penup()
    ok.forward(40)
    ok.pendown()

# ok.penup()

# ok.forward(200)
# ok.right(90)
# ok.forward(100)
# ok.left(90)
# ok.pendown()
