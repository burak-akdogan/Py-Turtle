
import turtle
import random
 
t = turtle.Turtle()
s = turtle.Screen()
 
t.speed(100)
 
s.bgcolor("black") 
t.color("yellow")
 
t.hideturtle()
def stars():
    for i in range(5):
        t.fd(10)
        t.right(144)
 
 
for i in range(100):
   
    x = random.randint(-640, 640)
    y = random.randint(-330, 330)
     

    stars()
    t.up()
    t.goto(x, y)
    t.down()
 
t.up()
 
#Moon
t.goto(10, 170)
t.down()
 

t.color("white")
t.begin_fill()
t.circle(90)
t.end_fill()
 
 

s.exitonclick()