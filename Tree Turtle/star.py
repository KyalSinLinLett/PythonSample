import turtle
from turtle import *

windows = turtle.Screen()
windows.bgcolor('black')

color('light blue')

while True:
    left(190)
    forward(100)
    right(75)
    # backward(80)
    speed(200)
    if abs(pos()) < 1:
        break

setpos(150,150)

while True:
	right(75)
	forward(100)
	left(190) 
    # backward(80)
	speed(200)
	if abs(pos()) < 15:
		break

# end_fill()
done()