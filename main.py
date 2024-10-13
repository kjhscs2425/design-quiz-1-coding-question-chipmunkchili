from turtle import *

#this next part is not necessary, but it helps center the shape better
up()
goto(-100,250)
down()

def draw_shape(size, sides):
    for i in range(sides):
        forward(size)
        right(360/sides)

draw_shape(100,12)

exitonclick()