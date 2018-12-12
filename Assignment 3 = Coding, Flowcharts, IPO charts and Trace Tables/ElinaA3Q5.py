# WOW me with your Pygame Sprite knowledge
# Date Begun: 11/03/18
# Programmer: Elina Ho
# Modifications: https://www.101computing.net/creating-sprites-using-pygame/
# https://stackoverflow.com/questions/8767129/how-to-have-an-image-appear-in-python-pygame
# http://pngimagesfree.com/Butterfly/butterfly-png-flying.png for butterfly image
# http://picresize.com/edit to help resize the picture
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
# used code from class example

# importing pygame
import pygame
pygame.init()

# set up some variables for use, starting point, width, height, speed
x = 375
y = 60
vel = 3
length = 20
width = 20
GREEN = (36, 173, 55)
YELLOW = (255, 255, 0)

# set screen size
size = (700,500)
screen = pygame.display.set_mode(size)

# label the window
pygame.display.set_caption("ElinaA3Q5 - Moving the Sprite")

# set font
font = pygame.font.SysFont(None, 36)

# make false
run = False


while not run:

    for event in pygame.event.get():
        # checks if something happened
        if event.type == pygame.QUIT:
            # run is true means quit program
            run = True

    screen.fill((0, 200, 255))
    pygame.draw.polygon(screen, GREEN, ((0, 500), (700, 500), (700, 700), (0, 700)), 100)
    pygame.draw.circle(screen, YELLOW, (75, 60), 40)

    sprite = pygame.image.load("butterfly.png")
    screen.blit(sprite, (x, y))

    # displays simple instructions and warning to user that sprite may fall off screen
    text = font.render("Move me around! Don't make me fall off the screen!! :D", True, (0, 0, 0), screen)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 150
    screen.blit(text, textRect)

    pygame.display.update()


    # making the sprite move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-= vel

    if keys[pygame.K_RIGHT]:
        x+=vel

    if keys[pygame.K_UP]:
        y-= vel

    if keys[pygame.K_DOWN]:
        y+= vel

    #Screen Fill
    screen.fill((255, 255, 255))

#Quits Game
pygame.quit()
