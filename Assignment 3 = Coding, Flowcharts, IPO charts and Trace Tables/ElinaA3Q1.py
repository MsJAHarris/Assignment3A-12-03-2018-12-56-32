# Create program with Koch Curve
# Elina Ho
# Date Begun: 11/06/18
# Modifications: called MyKoch function

# Programmer:
import turtle

t = turtle.Pen()

def MyKoch(Turtle, length, degree):
	if degree == 0:
		# tell the turtle to draw for length steps in here
		Turtle.forward(length)

	else:
		length1 = length/3
		degree1 = degree-1
		MyKoch(Turtle, length1, degree1)
		Turtle.left(60)
		# tell the turtle to turn left 60 degrees
		MyKoch(Turtle, length1, degree1)
		Turtle.right(120)
		# tell the turtle to turn right 120 degrees
		MyKoch(Turtle, length1, degree1)
		Turtle.left(60)
		# tell the turtle to turn left 60 degrees
		MyKoch(Turtle, length1, degree1)

MyKoch(t, 200, 3) # calling the Koch function with specified degree and lenght
t.right(120) # turning right to form 1st leg of triangle
MyKoch(t, 200, 3) # calling the Koch function with specified degree and lenght
t.right(120) # turning right to form 2nd leg of triangle
MyKoch(t, 200, 3) # calling the Koch function with specified degree and lenght
t.right(120) # turning right to form final leg of triangle

turtle.done() # keeps finished product on the screen, so you can admire it :D

#(Idea copied from Prof. John Zelle, Python Programming and introduction to computer science 2nd
# edition {Python 2}.)
