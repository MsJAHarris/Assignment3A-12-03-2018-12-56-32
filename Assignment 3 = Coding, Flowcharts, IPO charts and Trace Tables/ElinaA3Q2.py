# Create interactive hangman game
# Date Begun: 11/09/18
# Programmer: Elina Ho
# Modifications: created basic pygame window, added graphics, and added typing features
# Websites used: https://sivasantosh.wordpress.com/2012/07/18/displaying-text-in-pygame/ - how to display the text
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

import pygame
import random
from pygame.locals import *

# sets colour to be called later
BACKGROUND = (171, 102, 227)
BLACK = (0, 0, 0)

pygame.init()

# set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# label the window
pygame.display.set_caption("ElinaA3Q2 - Hangman")

# make true
run = True

# path to get the words
path = 'hangmanwords.txt'


def generate_the_word(inFile):
    with open(path) as f:
        contents_of_file = f.read()  # reads the lines
    lines = contents_of_file.splitlines()  # reads each line individually
    line_number = random.randrange(0, len(lines))  # random line from the text file
    return lines[line_number]  # gives a word


word = (generate_the_word(path))  # generates word
wordLen = len(word)

# sets guesses as empty string
guesses = ""
# sets number of turns
turns = 10

# sets font
font = pygame.font.SysFont(None, 36)

keyPressed = False

firstRun = True  # if it's the first time it runs through the loop, you can still see the welcome screen

# while run
while run:
    keyPressed = False  # nothing is pressed

    for event in pygame.event.get():
        # checks if something happened
        if event.type == pygame.QUIT:
            # run is false means quit program
            run = False
        if event.type == KEYDOWN:
            # if something is pressed
            keyPressed = True
            if event.unicode.isalpha():
                guess = event.unicode
                guesses += guess  # accumulate guess into guesses

    if (not keyPressed) and (not firstRun):
        continue  # break from loop and go back to beginning of loop

    firstRun = False  # reset so that the playing screen can continue to display in each iteration

    screen.fill(BACKGROUND)  # fills the background with this colour

    sprite = pygame.image.load("hangman.png")  # draws hangman
    screen.blit(sprite, (235, 220))

    pygame.display.update()

    # displays welcome message
    helloName = font.render("Welcome! Are you ready to have some fun?", True, BLACK, BACKGROUND)
    helloNameRect = helloName.get_rect()
    helloNameRect.centerx = 350
    helloNameRect.centery = 100
    welcome = font.render("It's time to play hangman! Guess a letter...", True, BLACK, BACKGROUND)
    welcomeRect = welcome.get_rect()
    welcomeRect.centerx = 350
    welcomeRect.centery = 140

    screen.blit(welcome, welcomeRect)
    screen.blit(helloName, helloNameRect)

    if turns > 0:
        missingChar = 0

        rightGuess = False

        drawResult = "" # accumulate right or wrong guesses to display

        for char in word:
            if char in guesses:
                drawResult += char + ""

                if guess == char:  # set equal to see if current guess is part of char
                    rightGuess = True
            elif char == " ":
                drawResult += char + " "
            else:
                drawResult += "_ "

                # edit counters
                missingChar += 1

        # draws the text
        text = font.render(drawResult, True, BLACK, BACKGROUND)
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 150
        screen.blit(text, textRect)

        if keyPressed and not rightGuess:
            turns -= 1

        # display number of turns
        turnsText = font.render("Tries left: " + str(turns), True, BLACK, BACKGROUND)
        turnsRect = turnsText.get_rect()
        turnsRect.centerx = 350
        turnsRect.centery = 180

        screen.blit(turnsText, turnsRect)

    else:
        print("Sorry, you lose")
        print("The word was: " + word)
        break

    pygame.display.flip()

    if missingChar == 0:
        print("Congratulations, you win")
        break

    # Screen Fill
    screen.fill((255, 255, 255))

# Quits Game
pygame.quit()