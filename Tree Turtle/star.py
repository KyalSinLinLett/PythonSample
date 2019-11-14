from turtle import *

windows = turtle.Screen()
windows.bgcolor('black')

color('light blue')

position = pos()

print(position)

while True:
    left(145)
    forward(100)
    right(90)

    if abs(pos()) < 2:
        break
# end_fill()
done()