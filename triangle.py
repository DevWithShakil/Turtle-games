import turtle
from turtle import *

# Turle for Triangle

speed(0)
bgcolor("skyblue")

penup()
goto(-150, -150)
fillcolor('white')
begin_fill()
pendown()

for i in range(3):
    forward(300)
    left(120)

end_fill()

hideturtle()

turtle.done()