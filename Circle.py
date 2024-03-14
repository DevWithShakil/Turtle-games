import turtle
from turtle import *

speed(1)
penup()
goto(0, -100)
bgcolor("green")
color("red")
pensize(5)
pendown()

begin_fill()
circle(120)
end_fill()

hideturtle()
exitonclick()