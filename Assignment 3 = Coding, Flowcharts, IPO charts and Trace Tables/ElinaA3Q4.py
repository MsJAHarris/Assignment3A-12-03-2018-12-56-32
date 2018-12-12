# Create interactive BlackJack game
# Date Begun: 11/14/18
# Programmer: Elina Ho
# Modifications: imported images, finished logic, made it interactive
# Websites used: https://stackoverflow.com/questions/11390596/how-to-display-image-in-pygame
# https://stackoverflow.com/questions/35642629/using-classes-in-pygame

# Import Libraries
import pygame
import random
import os # how to join the path

# setup global settings
pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)

# Global Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)

BACKGROUND = (0, 0, 0)

# Set Icon
cardpath = os.path.join("resources", "cards")
icon = pygame.image.load(os.path.join("resources", "icon.png"))
pygame.display.set_icon(icon)

# label the window
pygame.display.set_caption("ElinaA3Q4 - Card Game")

# sets font
font = pygame.font.SysFont(None, 24)

class Card:

    # array of dictionary - includes suit, rank, number of points, and picture associated
    cards = [
        {"suit": "diamond", "rank": "A", "pt": 11, "image": pygame.image.load(os.path.join(cardpath, 'ad.png'))},
        {"suit": "diamond", "rank": "2", "pt": 2, "image": pygame.image.load(os.path.join(cardpath, '2d.png'))},
        {"suit": "diamond", "rank": "3", "pt": 3, "image": pygame.image.load(os.path.join(cardpath, '3d.png'))},
        {"suit": "diamond", "rank": "4", "pt": 4, "image": pygame.image.load(os.path.join(cardpath, '4d.png'))},
        {"suit": "diamond", "rank": "5", "pt": 5, "image": pygame.image.load(os.path.join(cardpath, '5d.png'))},
        {"suit": "diamond", "rank": "6", "pt": 6, "image": pygame.image.load(os.path.join(cardpath, '6d.png'))},
        {"suit": "diamond", "rank": "7", "pt": 7, "image": pygame.image.load(os.path.join(cardpath, '7d.png'))},
        {"suit": "diamond", "rank": "8", "pt": 8, "image": pygame.image.load(os.path.join(cardpath, '8d.png'))},
        {"suit": "diamond", "rank": "9", "pt": 9, "image": pygame.image.load(os.path.join(cardpath, '9d.png'))},
        {"suit": "diamond", "rank": "10", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, '10d.png'))},
        {"suit": "diamond", "rank": "J", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'jd.png'))},
        {"suit": "diamond", "rank": "Q", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'qd.png'))},
        {"suit": "diamond", "rank": "K", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'kd.png'))},
        {"suit": "club", "rank": "A", "pt": 11, "image": pygame.image.load(os.path.join(cardpath, 'ac.png'))},
        {"suit": "club", "rank": "2", "pt": 2, "image": pygame.image.load(os.path.join(cardpath, '2c.png'))},
        {"suit": "club", "rank": "3", "pt": 3, "image": pygame.image.load(os.path.join(cardpath, '3c.png'))},
        {"suit": "club", "rank": "4", "pt": 4, "image": pygame.image.load(os.path.join(cardpath, '4c.png'))},
        {"suit": "club", "rank": "5", "pt": 5, "image": pygame.image.load(os.path.join(cardpath, '5c.png'))},
        {"suit": "club", "rank": "6", "pt": 6, "image": pygame.image.load(os.path.join(cardpath, '6c.png'))},
        {"suit": "club", "rank": "7", "pt": 7, "image": pygame.image.load(os.path.join(cardpath, '7c.png'))},
        {"suit": "club", "rank": "8", "pt": 8, "image": pygame.image.load(os.path.join(cardpath, '8c.png'))},
        {"suit": "club", "rank": "9", "pt": 9, "image": pygame.image.load(os.path.join(cardpath, '9c.png'))},
        {"suit": "club", "rank": "10", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, '10c.png'))},
        {"suit": "club", "rank": "J", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'jc.png'))},
        {"suit": "club", "rank": "Q", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'qc.png'))},
        {"suit": "club", "rank": "K", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'kc.png'))},
        {"suit": "spade", "rank": "A", "pt": 11, "image": pygame.image.load(os.path.join(cardpath, 'as.png'))},
        {"suit": "spade", "rank": "2", "pt": 2, "image": pygame.image.load(os.path.join(cardpath, '2s.png'))},
        {"suit": "spade", "rank": "3", "pt": 3, "image": pygame.image.load(os.path.join(cardpath, '3s.png'))},
        {"suit": "spade", "rank": "4", "pt": 4, "image": pygame.image.load(os.path.join(cardpath, '4s.png'))},
        {"suit": "spade", "rank": "5", "pt": 5, "image": pygame.image.load(os.path.join(cardpath, '5s.png'))},
        {"suit": "spade", "rank": "6", "pt": 6, "image": pygame.image.load(os.path.join(cardpath, '6s.png'))},
        {"suit": "spade", "rank": "7", "pt": 7, "image": pygame.image.load(os.path.join(cardpath, '7s.png'))},
        {"suit": "spade", "rank": "8", "pt": 8, "image": pygame.image.load(os.path.join(cardpath, '8s.png'))},
        {"suit": "spade", "rank": "9", "pt": 9, "image": pygame.image.load(os.path.join(cardpath, '9s.png'))},
        {"suit": "spade", "rank": "10", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, '10s.png'))},
        {"suit": "spade", "rank": "J", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'js.png'))},
        {"suit": "spade", "rank": "Q", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'qs.png'))},
        {"suit": "spade", "rank": "K", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'ks.png'))},
        {"suit": "heart", "rank": "A", "pt": 11, "image": pygame.image.load(os.path.join(cardpath, 'ah.png'))},
        {"suit": "heart", "rank": "2", "pt": 2, "image": pygame.image.load(os.path.join(cardpath, '2h.png'))},
        {"suit": "heart", "rank": "3", "pt": 3, "image": pygame.image.load(os.path.join(cardpath, '3h.png'))},
        {"suit": "heart", "rank": "4", "pt": 4, "image": pygame.image.load(os.path.join(cardpath, '4h.png'))},
        {"suit": "heart", "rank": "5", "pt": 5, "image": pygame.image.load(os.path.join(cardpath, '5h.png'))},
        {"suit": "heart", "rank": "6", "pt": 6, "image": pygame.image.load(os.path.join(cardpath, '6h.png'))},
        {"suit": "heart", "rank": "7", "pt": 7, "image": pygame.image.load(os.path.join(cardpath, '7h.png'))},
        {"suit": "heart", "rank": "8", "pt": 8, "image": pygame.image.load(os.path.join(cardpath, '8h.png'))},
        {"suit": "heart", "rank": "9", "pt": 9, "image": pygame.image.load(os.path.join(cardpath, '9h.png'))},
        {"suit": "heart", "rank": "10", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, '10h.png'))},
        {"suit": "heart", "rank": "J", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'jh.png'))},
        {"suit": "heart", "rank": "Q", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'qh.png'))},
        {"suit": "heart", "rank": "K", "pt": 10, "image": pygame.image.load(os.path.join(cardpath, 'kh.png'))}
    ]

    # function to deal cards
    def deal(self, num, toList, xList):
        for i in range(num):
            while True:
                card = random.choice(self.cards)  # chooses a random card
                if card not in toList and card not in xList:
                    toList.append(card)  # if not in the list add it to the list
                    break

    # shows the picture
    def show(self, cList, ypos):
        n = 0
        for card in cList:
            image = card["image"].convert()  # get image
            imagerect = image.get_rect()
            imagerect.centerx = 100 + n  # sets the position of card
            imagerect.centery = ypos
            screen.blit(image, imagerect)  # blits it to the screen
            n += 100

        # displays points
        totaltext = font.render("{} points!".format(self.sum(cList)), True, WHITE, BACKGROUND)
        totaltextrect = totaltext.get_rect()
        totaltextrect.centerx = 700
        totaltextrect.centery = ypos
        screen.blit(totaltext, totaltextrect)

        pygame.display.update()  # updates the screen

    # shows the back of the card (for the computer)
    def showBack(self, cList, ypos):
        n = 0
        for x in range(len(cList)):
            image = pygame.image.load(os.path.join(cardpath,"cardback.png")).convert()
            imagerect = image.get_rect()
            imagerect.centerx = 100 + n
            imagerect.centery = ypos
            screen.blit(image, imagerect)
            n += 100

        pygame.display.update()

    # function to show the results to see if you win or computer wins
    def showResult(self, myList, compList, isDraw):
        myTotal = self.sum(myList)
        compTotal = self.sum(compList)

        ypos = 625
        if myTotal > 21:
            text = "Sorry, you lose. Computer wins!"
        elif isDraw == True and myTotal < 21:
            text = "Do you want another card? y/n"
            ypos = 600
        elif compTotal > 21:
            text = "Congratulations, you win!"
        elif myTotal > compTotal:
            text = "Congratulations, you win!"
        elif isDraw == False and compTotal > myTotal:
            text = "Sorry, you lose. Computer wins!"

        totaltext = font.render(text, True, WHITE, BACKGROUND)
        totaltextrect = totaltext.get_rect()
        totaltextrect.centerx = 400
        totaltextrect.centery = ypos
        screen.blit(totaltext, totaltextrect)

        pygame.display.update()

    # checks to see if there is and Ace (ace can be 1 or 11)
    # if there is an ace, it changed it to 1 to see if player can still win
    def sum(self, cards):
        points = 0
        for x in cards:
            points += x["pt"]
            if points > 21:
                if x["rank"] == "A":
                    points = points - 10

        return points

# shows the beginning screen
def firstscreen(text):
    welcome = font.render(text, True, WHITE, BACKGROUND)
    welcomeRect = welcome.get_rect()
    welcomeRect.centerx = 400
    welcomeRect.centery = 400
    screen.blit(welcome, welcomeRect)

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.fill(BLACK)
                    run = False

#################### Main program starts here
run = True

firstscreen("Press enter to begin!")
firstscreen("Welcome to 'Game of 21'!")
firstscreen("Instructions... Try to get 21 points")
firstscreen("21 points - you win. Above 21 - you lose. Below 21 - press 'y' to get another card, press 'n' to stay")

# initializing variables
myList = []
compList = []

isDraw = True  # player keeps drawing
compDraw = False  # once player is done drawing, computer starts drawing
isStop = False  # game is done

myTotal = 0
compTotal = 0

c = Card()

c.deal(2, myList, compList)
c.deal(2, compList, myList)

c.show(myList, 200)
c.showBack(compList, 400)
c.showResult(myList, compList, isDraw)

while True:
    run = False
    for event in pygame.event.get():
        # checks if something happened
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                run = True
                break
            elif event.key == pygame.K_n:
                run = True
                isDraw = False
                compDraw = True
                break
        elif isStop:
            continue
        else:
            continue

    if run:
        if isDraw == True and len(myList) < 5:
            c.deal(1, myList, compList)

        c.show(myList, 200)
        if compDraw:
            c.show(compList, 400)
        else:
            c.showBack(compList, 400)

        # Computer turn to draw
        while compDraw:
            compTotal = c.sum(compList)
            if compTotal > 21:
                # c.showResult(myTotal, compTotal)
                break
            elif compTotal < 21:
                if len(compList) < 5:
                    c.deal(1, compList, myList)
                    c.show(compList, 400)
                else:
                    break
            else:
                # c.showResult(myTotal, compTotal)
                break

        c.showResult(myList, compList, isDraw)

        if myTotal >= 21 or compTotal >= 21 or not isDraw:
            isStop = True

        pygame.display.flip()

# Quits Game
pygame.quit()
quit()