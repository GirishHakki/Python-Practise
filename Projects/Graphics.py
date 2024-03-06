import random
import turtle
colors = ['red', 'cyan', 'pink', 'yellow', 'green', 'orange']
t = turtle.Turtle()
t.speed(50)
turtle.bgcolor("black")
lenght = 100
angle = 50
size = 3

for i in range(lenght):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")