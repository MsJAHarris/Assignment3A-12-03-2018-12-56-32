# Problem Description:
# WOW me with your Pygame Sprite knowledge – you may begin with the sprite given in class, but do not
# need to. Have fun with this one!
# Date Begun:Nov 21

# Programmer:Carl W

# Modifications:
import pygame
import time
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
speed = pygame.time.Clock()

# Creating some variables for coordinates etc.
x1 = 500
y1= 500
x2 = 0
y2 = 0
# Loading in image
CanSprite = pygame.image.load('spritecan.png')
run = True
soda = 1
counter = 0
while run:
    screen.fill((255, 255, 255))
    # Creating a message
    if soda is 1:
        font = pygame.font.SysFont('Arial', 40)
        text = font.render("Wow look it's a can of Sprite", True, (0, 0, 0))
        screen.blit(text, [500, 100])
        screen.blit(CanSprite, (x1 - 125, y1 - 125))
    # Counter is being changed by key presses below
    if counter is 5:
        soda = 2
    # When counter is 5, soda will be 2 and there will be two cans of Sprite
    if soda is 2:
        text = font.render("Wow look there are two cans of Sprite", True, (0, 0, 0))
        screen.blit(text, [0, 100])
        screen.blit(CanSprite, (x1 - 125, y1 - 125))
        screen.blit(CanSprite, (x1 - 125, y1 + 125))
    # Catching events and keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            elif event.key == K_LEFT:
                x2 = -10
                counter = counter + 1
            elif event.key == K_RIGHT:
                x2 = 10
                counter = counter + 1
            elif event.key == K_UP:
                y2 = -10
            elif event.key == K_DOWN:
                y2 = 10
        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                y2 = 0
            elif event.key == K_LEFT or event.key == K_RIGHT:
                x2 = 0
    # Moving the sprite by changing its coordinates
    x1 = x1 + x2
    y1 = y1 + y2
    pygame.display.update()


