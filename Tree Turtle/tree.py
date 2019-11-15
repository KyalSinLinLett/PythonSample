import random
import turtle

def tree(size, myTurtle):
	myTurtle.pensize(size / 10)

	if size < random.randint(1,2) * 20:
		myTurtle.color('green')
	else:
		myTurtle.color('brown')

	if size > 5:
		myTurtle.forward(size)
		myTurtle.left(25)
		tree(size - random.randint(10, 20), myTurtle)
		myTurtle.right(50)
		tree(size - random.randint(10, 20), myTurtle)
		myTurtle.left(25)
		myTurtle.penup()
		myTurtle.backward(size)
		myTurtle.pendown()

window = turtle.Screen()
window.bgcolor('black')

myTurtle = turtle.Turtle()
myTurtle.color('brown', 'blue')
myTurtle.left(90)
myTurtle.speed(1000)
myTurtle.penup()
myTurtle.setpos(-200, -250)
myTurtle.pendown()

myTurtle2 = turtle.Turtle()
myTurtle2.color('brown', 'blue')
myTurtle2.left(90)
myTurtle2.speed(1000)
myTurtle2.penup()
myTurtle2.setpos(200, -250)
myTurtle2.pendown()

tree(120, myTurtle)
tree(120, myTurtle2)
window.exitonclick()