import turtle
from turtle import *

fillcolor("blue")
begin_fill()

for i in range(2):
    forward(300)
    right(90)
    forward(150)
    right(90)

hideturtle()
end_fill()
exitonclick()