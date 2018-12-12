# Problem Description:
# # Please create a flowchart, IPO chart and trace table for a particular error you had while creating
# # your work.  Please let me know which version you were on at the time of the error, so that I may see
# # the code and match up the trace table to that (now fixed) code.
# #
# # Your task: Create a basic Yatzee game (top of score card only) using the msdie class created in class.
# # Note: Rename this file appropriately (if that does not happen automatically)
# # Date Begun: November 5, 2018
#
# # Programmer: Carl
#
# # Modifications:

# Importing
from random import *


# Class core from GitHub
class msdie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)
        return self.value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


# Where modifications really begin~~~~~~~~~~~
# Rolling each dice
die1 = msdie(6)
die1.roll()

die2 = msdie(6)
die2.roll()

die3 = msdie(6)
die3.roll()

die4 = msdie(6)
die4.roll()

die5 = msdie(6)
die5.roll()

# Two random "rerolls"
diex1 = msdie(6)
diex1.roll()

diex2 = msdie(6)
diex2.roll()

diex3 = msdie(6)
diex3.roll()
# The player has 3 extra rolls
rolls = 3


# Defining function to show dice values
def currentDice():
    print("dice 1 value is:", val1)
    print("dice 2 value is:", val2)
    print("dice 3 value is:", val3)
    print("dice 4 value is:", val4)
    print("dice 5 value is:", val5)


# Introduction
print("Welcome to Yahtzee, you have 3 extra rolls and you may reroll one die at a time. Here is your initial roll.")

# Tracking dice values in variables
val1 = die1.getValue()
val2 = die2.getValue()
val3 = die3.getValue()
val4 = die4.getValue()
val5 = die5.getValue()
# print(diex1.getValue())
# 3 "reroll" values
valx1 = diex1.getValue()
valx2 = diex2.getValue()
valx3 = diex3.getValue()
# Initial dice
currentDice()

# Turn counter
turn = 1
# Testing
# print("reroll 1 is", diex1.getValue())
# print("reroll 2 is", diex2.getValue())
# While the user has turns left
while turn is not 4:
    # Asking if the user would like keep or reroll a die
    rollAgain = input("Would you like to reroll a die? y/n:")
    # If they choose to keep their dice
    if rollAgain is "n":
        # Set in the program to a state as if all turns are over
        turn = 4
    # If the user would like to reroll a die AND the turn is 1
    if rollAgain is "y" and turn is 1:
        # Asking user WHICH die they would like to reroll
        reroll = input("Which die would you like to reroll? 1/2/3/4/5:")
    # If user wants to reroll die 1...
    if rollAgain is "y" and reroll is "1" and turn is 1:
        # Set die 1 value to the first "reroll"
        val1 = valx1
        # Display dice after reroll
        currentDice()
        # Add 1 to turns
        turn = turn + 1
        # Resetting variables with x
        rollAgain = "x"
        reroll = "x"
    # If user wants to reroll die 2...
    if rollAgain is "y" and reroll is "2" and turn is 1:
        # Set die  value to the first "reroll"
        val2 = valx1
        # Display all the dice
        currentDice()
        # Add 1 to the turn counter
        turn = turn + 1
        # Variable reset
        rollAgain = "x"
        reroll = "x"
    # etc
    if rollAgain is "y" and reroll is "3" and turn is 1:
        val3 = valx1
        currentDice()
        turn = turn + 1
        rollAgain = "x"
        reroll = "x"
    if rollAgain is "y" and reroll is "4" and turn is 1:
        val4 = valx1
        currentDice()
        turn = turn + 1
        rollAgain = "x"
        reroll = "x"
    if rollAgain is "y" and reroll is "5" and turn is 1:
        val5 = valx1
        currentDice()
        turn = turn + 1
        rollAgain = "x"
        reroll = "x"
    # TURN 2
    if turn is 2:
        rollAgain = input("Would you like to reroll a die? y/n:")
        if rollAgain is "n":
            turn = 4
        if rollAgain is "y":
            reroll = input("Which dice would you like to reroll? 1/2/3/4/5:")
        # Checking turn variable
        # the following section of ifs is very similar to the last
        if rollAgain is "y" and turn is 2:
            if reroll is "1":
                # Change the specified die to the second "reroll"
                val1 = valx2
                currentDice()
                turn = turn + 1
                rollAgain = "x"
                reroll = "x"
            if reroll is "2":
                val2 = valx2
                currentDice()
                turn = turn + 1
                rollAgain = "x"
                reroll = "x"
            if reroll is "3":
                val3 = valx2
                currentDice()
                turn = turn + 1
            if reroll is "4":
                val4 = valx2
                currentDice()
                turn = turn + 1
                rollAgain = "x"
                reroll = "x"
            if reroll is "5":
                val5 = valx2
                currentDice()
                turn = turn + 1
                rollAgain = "x"
                reroll = "x"
    # TURN 3 (last turn)
    if turn is 3:
        rollAgain = input("Would you like to reroll a die? y/n:")
        if rollAgain is "y":
            reroll = input("Which dice would you like to reroll? 1/2/3/4/5:")
    # Checking turn variable
    # the following section of ifs is very similar to the last
    if rollAgain is "y" and turn is 3:
        if rollAgain is "n":
            turn = 4
        if reroll is "1" and turn is 3:
            # Change the specified die to the third "reroll"
            val1 = valx3
            currentDice()
            turn = turn + 1
            rollAgain = "x"
            reroll = "x"
        if reroll is "2" and turn is 3:
            val2 = valx3
            currentDice()
            turn = turn + 1
            rollAgain = "x"
            reroll = "x"
        if reroll is "3" and turn is 3:
            val3 = valx3
            currentDice()
            turn = turn + 1
        if reroll is "4" and turn is 3:
            val4 = valx3
            currentDice()
            turn = turn + 1
            rollAgain = "x"
            reroll = "x"
        if reroll is "5" and turn is 3:
            val5 = valx3
            currentDice()
            turn = turn + 1
            rollAgain = "x"
            reroll = "x"
# Once the player finishes all turns
from collections import Counter

# Help finding mode in a list from https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list
if turn is 4:
    values = [val1, val2, val3, val4, val5]
    mode = Counter(values)
    print("Your dice values are:", values)
    # Finds the most frequent value from the list of rolled values
    # If the length of the mode list is 2 that means there was a four of a kind combination because there are only 2
    # different numbers in the group of 5. If the mode list is 3 that means there was a three of a kind combination or two
    # pairs. If the mode brought up one value only then there was a Yahtzee! because all 5 values were the same.
    # Use the test lines below if my explanation sucked.
    # Test
    # print(mode.most_common())
    # print(len(mode.most_common()))
    # Anything other than a Yahtzee!...
    if len(mode.most_common()) is not 1:
        # Non-Yahtzee scores always get added up
        score = val1 + val2 + val3 + val4 + val5
        if len(mode.most_common()) is 2:
            # Setting message for the end
            combo = "4 of a kind!"
        if len(mode.most_common()) is 3:
            combo = "3 of a kind or 2 pairs!"
        if len(mode.most_common()) is 4:
            combo = "pair!"
        if len(mode.most_common()) is 5:
            combo = "chance combo!"
    if len(mode.most_common()) is 1:
        combo = "Yahtzee!"
        score = 50
    print("Nice", combo, "You got", score, "points!")

# Defining the drawing of dice from the class we worked on in class
# Made small adjustments with parameters

import turtle

turtle.setup(1600, 900)
turtle.speed(15)

def side1(x, y):
    t = turtle
    t.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for p in range(4):
        t.forward(100)
        t.right(90)
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.pendown()
    t.dot(10, "Black")
    turtle.penup()
    t.setpos(x, y)
    t.left(90)
    t.setpos(0, 0)


def side2(x, y):
    turtle.hideturtle()

    # begin the filling process, making the color white
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    # draw the four sides
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

    # fill the square made
    turtle.end_fill()
    # lift the pen up
    turtle.penup()

    # go to the given x,y coordinates
    turtle.goto(x + 33, y - 33)
    turtle.pendown()

    # put the pendown
    turtle.pendown()
    turtle.dot(10, "black")
    turtle.penup()
    turtle.goto(x + 66, y - 66)
    turtle.pendown()
    # make a 10 pixel wide black dot
    turtle.dot(10, "black")
    turtle.penup()
    turtle.setpos(0, 0)


def side3(x, y):
    # Set the starting position for the drawing of the square
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(x, y)
    turtle.pendown()
    # Drawing the four sides of the square shaped size
    for u in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
    turtle.setpos(x + 25, y - 25)
    turtle.dot(10)
    turtle.setpos(x + 50, y - 50)
    turtle.dot(10)
    turtle.setpos(x + 75, y - 75)
    turtle.dot(10)
    turtle.penup()
    turtle.setpos(0, 0)


def side4(x, y):
    t = turtle
    turtle.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for k in range(4):
        t.forward(100)
        t.right(90)
    t.penup()
    t.setpos(x + 33, y - 33)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 33, y - 66)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 66, y - 33)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 66, y - 66)
    t.pendown()
    t.dot(10)
    turtle.penup()
    turtle.setpos(0, 0)


def side5(x, y):
    t = turtle
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.hideturtle()
    for z in range(4):  # loop so it draws 4 sides
        t.forward(100)  # side
        t.right(90)  # corner
    turtle.penup()
    turtle.setpos(x + 25, y - 25)
    turtle.pendown()
    t.dot(10)
    turtle.penup()
    turtle.setpos(x + 25, y - 75)
    turtle.pendown()
    t.dot(10)
    turtle.penup()
    turtle.setpos(x + 50, y - 50)
    turtle.pendown()
    t.dot(10)
    turtle.penup()
    turtle.setpos(x + 75, y - 25)
    turtle.pendown()
    t.dot(10)
    turtle.penup()
    turtle.setpos(x + 75, y - 75)
    turtle.pendown()
    t.dot(10)
    t.penup()
    turtle.setpos(0, 0)


def side6(x, y):
    t = turtle
    t.penup()  # not drawing when moving
    t.setpos(x, y)  # setting up the start position
    t.pendown()  # drawing when moving
    t.hideturtle()
    for f in range(4):
        t.forward(100)
        t.right(90)
    t.penup()
    t.setpos(x + 25, y - 25)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 25, y - 50)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 25, y - 75)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 75, y - 25)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 75, y - 50)
    t.pendown()
    t.dot(10)
    t.penup()
    t.setpos(x + 75, y - 75)
    t.pendown()
    t.dot(10)
    turtle.penup()
    turtle.setpos(0, 0)


# Drawing the first dice the user ended with
if val1 is 1:
    side1(-300, -200)
if val1 is 2:
    side2(-300, -200)
if val1 is 3:
    side3(-300, -200)
if val1 is 4:
    side4(-300, -200)
if val1 is 5:
    side5(-300, -200)
if val1 is 6:
    side6(-300, -200)

# Drawing the second die the user ended with
if val2 is 1:
    side1(-300, 0)
if val2 is 2:
    side2(-300, 0)
if val2 is 3:
    side3(-300, 0)
if val2 is 4:
    side4(-300, 0)
if val2 is 5:
    side5(-300, 0)
if val2 is 6:
    side6(-300, 0)

# Showing die 3
if val3 is 1:
    side1(-300, 200)
if val3 is 2:
    side2(-300, 200)
if val3 is 3:
    side3(-300, 200)
if val3 is 4:
    side4(-300, 200)
if val3 is 5:
    side5(-300, 200)
if val3 is 6:
    side6(-300, 200)

# Showing die 4
if val4 is 1:
    side1(-600, 200)
if val4 is 2:
    side2(-600, 200)
if val4 is 3:
    side3(-600, 200)
if val4 is 4:
    side4(-600, 200)
if val4 is 5:
    side5(-600, 200)
if val4 is 6:
    side6(-600, 200)

# Showing die 5
if val5 is 1:
    side1(-600, -200)
if val5 is 2:
    side2(-600, -200)
if val5 is 3:
    side3(-600, -200)
if val5 is 4:
    side4(-600, -200)
if val5 is 5:
    side5(-600, -200)
if val5 is 6:
    side6(-600, -200)

# Drawing message

turtle.write((('Nice', combo, 'You got', score, 'points!')), True, align = "left", font=("Arial", 32, "normal"))
turtle.exitonclick()
