"""1)	Recursion – The Koch curve is described in terms of “levels” or “degrees”."""

#Problem Description: The Koch curve of degree 0 is a straight line.  The first degree curve
# is formed by placing an accent (^).  The original line has been divided into 4( -^-), each of which
# is 1/3 the length of the original.  The accent or accent rises at 60 degrees, so it forms two sides
# of an equilateral triangle.  To get a second-degree curve, you put an accent in each of the line
# segments of the first-degree curve.  Successive curves are constructed by placing accents on each
# segment or the previous curve.
#Your Task:
#1.	 Create a flowchart for this problem
#2.	Create an IPO chart for this problem
#3.	Create a trace (table in any form) for this question when you have an error and hand it in.
#4.	Complete the coding and hand it in.

#Implement this algorithm with a Turtle class that contains instance variables location (a point) and
# Direction (a float?) and moveTo (somePoint), draw (length), and turn (degrees). A little advanced
# math if you are stuck (you do not need to use this):
#If you are maintaining direction as an angle in radians, the point you are going to can be computed
# from your current location direction x = length * cos(direction) and current location direction
# y = length * sin(direction)
#
#IMPORTANT NOTE:  Contrary to all other assignments, your Koch snowflake can be very basic and it will
# be marked as a level 3 if you have made an honest attempt (Application and Thinking).  You must have
# a base case and your program must end.  Use error capture.  BE very careful in your attempt to earn
# a Level 4 – you must cite your sources AND must not borrow more than 25% of your code.


#A turtle always knows where it currently sits and what direction it is facing.  To draw a Koch curve
# of a given length and degree, you might (but don’t need to) use an algorithm like:
# REMINDER - Rename this file appropriately.
# Date Begun:

# Programmer:
	MyKoch(Turtle, length, degree):
		if degree == 0:
			# tell the turtle to draw for length steps in here
		else:
			length1 = length/3
			degree1 = degree-1
			MyKoch(Turtle, length1, degree1)
			# tell the turtle to turn left 60 degrees
			MyKoch(Turtle, length1, degree1)
# tell the turtle to turn left 120 degrees
			MyKoch(Turtle, length1, degree1)
# tell the turtle to turn left 60 degrees
			MyKoch(Turtle, length1, degree1)
#(Idea copied from Prof. John Zelle, Python Programming and introduction to computer science 2nd
# edition {Python 2}.)