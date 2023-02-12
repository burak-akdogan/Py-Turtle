import turtle
colors = ['red', 'purple', 'blue', 'green', 'black', 'yellow','orange']
t = turtle.Pen()
turtle.bgcolor('grey')
for x in range(360):
    t.pencolor(colors[x%7])
    t.width(x//50 + 2)
    t.forward(x)
    t.left(40)