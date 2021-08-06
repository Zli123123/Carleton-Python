import turtle
t = turtle.Turtle() # init graphics
t.color("red")  
t.width(2)
t.speed(1)
t.circle(50)
t.penup()
t.goto(0, 50)
t.pendown()
for i in range(6):
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.backward(50)
    t.left(120)
    t.backward(50)
    t.right(60)

