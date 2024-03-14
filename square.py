import turtle
from turtle import *

speed(1)
bgcolor("black")

# Outlined Square
penup()
goto(-300, 100)
pendown()
pensize(5)
color("magenta")

for i in range(4):
    forward(150)
    left(90)

# Multi-coloured square (Stroke only)

penup()
goto(-130, 100)
pendown()

for i in ['yellow', 'red', 'green', 'blue']:
    color(i)
    forward(150)
    left(90)

# Square with Fill and Stroke
penup()
goto(40, 100)
color('blue', 'magenta')
pendown()
begin_fill()

for i in range(4):
    forward(150)
    left(90)
end_fill()


hideturtle()

exitonclick()