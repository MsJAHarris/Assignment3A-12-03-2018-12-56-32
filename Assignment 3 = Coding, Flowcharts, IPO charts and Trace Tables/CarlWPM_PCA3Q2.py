# Problem Description:
# Weeks ago you were given a version 1 and then a version 2 of hangman.  You are to complete this task,
# use versioning and commit regularly as you add each piece, nothing hardcoded. Your words will be input
# from either a txt file or a csv file, your choice.  Your word list should come from the hardware
# components readings from Week 9.
# Note: Rename this file appropriately (if that does not happen automatically)
# Please create a flowchart, IPO chart and trace table for a particular guess.
# Date Begun: November 5, 2018

# Programmer: Carl

# Modified
# Importing
import random
import turtle

t = turtle
import turtle

# Defining a function to pick a random word from a text file

def random_word(file):
    # Opening the list of words
    words = open(file).read().splitlines()
    # Return the word that was picked
    return random.choice(words)


# Picking a random word from the text file
open("words.txt")
answer = random_word("words.txt")
# Testing answer
# print(answer)

# Getting length of word for future messages
n = len(answer)
# Creating a variable to track the users lives equal to the length of the word divided by 2 (rounded up)
lives = round(n/2,1)
guesses = ""

# Introduction while telling the user how long the word is
print("Welcome to hangman you have", lives,"lives. The word is", n, "characters long. Please guess a character")


# While loop (while the user has lives)
while lives > 0:
    fails = 0

    # If the letter is in the word...
    for char in answer:
        if char in guesses:
            print(char, )
        else:
            print("_", )
            fails = fails + 1
    if fails is 0:
        print("You win.")
        t.hideturtle()
        t.setup(500, 500)
        t.pensize(5)
        t.speed(2)

        # Writing win message
        t.write("YOU WIN", True, align="center", font=("Arial", 32, "normal"))

        # Drawing stand
        t.penup()
        t.setpos(-100, -200)
        t.pendown()
        t.left(90)
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)

        # Drawing head
        t.penup()
        t.right(90)
        t.pendown()
        t.circle(10)
        t.penup()

        # Drawing neck
        t.left(90)
        t.forward(20)
        t.pendown()
        t.forward(15)

        # Drawing arms
        t.penup()
        t.setpos(-35, -85)
        t.pendown()
        t.left(90)
        t.forward(70)

        # Drawing rest of core body
        t.backward(35)
        t.right(90)
        t.forward(50)

        # Drawing legs
        t.setpos(-20, -170)
        t.setpos(0, -135)
        t.setpos(20, -170)
        t.exitonclick()
        break
    # Asking the user to guess a letter
    guess = input("Guess a character:")

    # set the players guess to guesses
    guesses = guesses + guess

    # if the guess is not found in the secret word
    if guess not in answer:
        # Takes away a life
        lives = lives - 1

        # Printing "incorrect" response
        print("That letter is not in the word")
        print("You have", lives, "lives/life left.")
        # When the user has no more lives print fail message and  lose screen
        if lives <= 0:
            print("You lost. The word was", answer, ". Please try again.")

            # Drawing the full hangman
            # Setting up
            t.hideturtle()
            t.setup(500,500)
            t.pensize(5)
            t.speed(2)

            # Writing lose message
            t.write("YOU LOSE", True, align = "center", font=("Arial", 32, "normal"))

            # Drawing stand
            t.penup()
            t.setpos(-100, -200)
            t.pendown()
            t.left(90)
            t.forward(200)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(50)

            # Drawing head
            t.penup()
            t.right(90)
            t.pendown()
            t.circle(10)
            t.penup()

            # Drawing neck
            t.left(90)
            t.forward(20)
            t.pendown()
            t.forward(15)

            # Drawing arms
            t.penup()
            t.setpos(-35, -85)
            t.pendown()
            t.left(90)
            t.forward(70)

            # Drawing rest of core body
            t.backward(35)
            t.right(90)
            t.forward(50)

            # Drawing legs
            t.setpos(-20, -170)
            t.setpos(0, -135)
            t.setpos(20, -170)
            t.exitonclick()
