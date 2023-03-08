import turtle
t=turtle.Turtle()
t.penup()
#B
t.goto(-30,50)
t.pendown()
t.pensize(10)
t.pencolor("red")
t.right(90)
t.forward(200)

t.penup()
t.goto(-30,50)
t.pendown()
t.right(-90)
t.circle(-50,180)

t.penup()
t.goto(-30,-50)
t.pendown()
t.right(180)
t.circle(-50,180)

#U
t.penup()
t.setpos(40,40)
t.pendown()
t.color("blue")
t.right(-90)
t.forward(150)
t.circle(50,180)
t.forward(150)

#R
t.penup()

