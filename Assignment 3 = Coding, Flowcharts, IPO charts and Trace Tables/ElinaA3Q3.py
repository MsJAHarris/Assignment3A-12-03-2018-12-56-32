# Create Yahtzee game
# Date Begun: 11/11/18
# Programmer: Elina Ho
# Modifications: joined path, and make it interactive

# Import Libraries
import pygame
import random
import os  # how to join the path

# setup global settings
pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)

# Global Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
RED = (255, 0, 0)

BACKGROUND = (0, 0, 0)

# Set resource path
dicepath = os.path.join("resources", "dices")

# label the window
pygame.display.set_caption("ElinaA3Q3 - Yatzee Game")

# sets font
font = pygame.font.SysFont(None, 24)


class Dice:
    # array of dictionary - includes pts and picture associated
    dices = [
        {"pt": 1, "image": pygame.image.load(os.path.join(dicepath, 'die_face_1.png'))},
        {"pt": 2, "image": pygame.image.load(os.path.join(dicepath, 'die_face_2.png'))},
        {"pt": 3, "image": pygame.image.load(os.path.join(dicepath, 'die_face_3.png'))},
        {"pt": 4, "image": pygame.image.load(os.path.join(dicepath, 'die_face_4.png'))},
        {"pt": 5, "image": pygame.image.load(os.path.join(dicepath, 'die_face_5.png'))},
        {"pt": 6, "image": pygame.image.load(os.path.join(dicepath, 'die_face_6.png'))}
    ]

    # function to deal cards
    def rollAll(self, myList):
        myList.clear()
        for i in range(5):
            myList.append(random.choice(self.dices))

    def reRoll(self, myList, selectedList):
        for i in selectedList:
            myList[i] = (random.choice(self.dices))

    def show(self, myList, ypos, selectedList):
        n = 0
        for i in range(len(myList)):
            dice = myList[i]
            image = dice["image"].convert()

            # show a rectangle around the dice that is selected
            if i in selectedList:
                pygame.draw.rect(image, RED, image.get_rect(), 30)

            image = pygame.transform.scale(image, (100, 100))
            imagerect = image.get_rect()
            imagerect.centerx = 100 + n
            imagerect.centery = ypos
            screen.blit(image, imagerect)
            n += 100

        pygame.display.update()

        showCategories(scoreList)


########## General functions
def textScreen(writtentext):
    text = font.render(writtentext, True, WHITE, BACKGROUND)
    textRect = text.get_rect()
    textRect.centerx = 400
    textRect.centery = 400
    screen.blit(text, textRect)

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.fill(BLACK)
                    run = False


def showText(text):
    t = font.render(text, True, WHITE, BACKGROUND)
    tRect = t.get_rect()
    tRect.centerx = 400
    tRect.centery = 700
    screen.blit(t, tRect)

    pygame.display.flip()


categories = [
    "Aces",
    "Twos",
    "Threes",
    "Fours",
    "Fives",
    "Sixes"
]


def showCategories(scoreList):
    total = 0
    for i in range(6):
        if scoreList[i] == -1:
            text = "{}: {}".format(i + 1, categories[i])
        else:
            text = "{}: {} - {}".format(i + 1, categories[i], scoreList[i])
            total += scoreList[i]

        cat = font.render(text, True, WHITE, BACKGROUND)
        catRect = cat.get_rect()
        catRect.centerx = 200
        catRect.centery = 300 + (i * 50)
        screen.blit(cat, catRect)

    t = font.render("Total: {}".format(total), True, WHITE, BACKGROUND)
    tRect = t.get_rect()
    tRect.centerx = 200
    tRect.centery = 600
    screen.blit(t, tRect)

    pygame.display.update()


def upperScore(myList, category):
    total = 0
    for dice in myList:
        if dice["pt"] == category:
            total += category

    return total

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


#################### Main program starts here
run = True

textScreen("Welcome to 'Yahtzee'! Press enter to begin!")
textScreen("Instructions")
textScreen("Press a,b,c,d,e to select a dice to re-roll")
textScreen("Press enter to re-roll the selected dice")
textScreen("You can only re-roll a maximum of 3 times")
textScreen("You can't select the same category twice")
textScreen("When all 6 categories are selected, then the game ends")
textScreen("Good luck!")

# initialize with 2 cards
myList = []

isStop = False

myTotal = 0
compTotal = 0

scoreList = [-1, -1, -1, -1, -1, -1]
selectedList = set()

d = Dice()

d.rollAll(myList)
d.show(myList, 200, selectedList)
# showCategories(scoreList)

numTries = 1

while True:
    run = False
    ruleSelected = False

    for event in pygame.event.get():
        # checks if something happened
        if event.type == pygame.QUIT:
            # run is true means quit program
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                selectedList.add(0)
                d.show(myList, 200, selectedList)
            elif event.key == pygame.K_b:
                selectedList.add(1)
                d.show(myList, 200, selectedList)
            elif event.key == pygame.K_c:
                selectedList.add(2)
                d.show(myList, 200, selectedList)
            elif event.key == pygame.K_d:
                selectedList.add(3)
                d.show(myList, 200, selectedList)
            elif event.key == pygame.K_e:
                selectedList.add(4)
                d.show(myList, 200, selectedList)
            elif event.key == pygame.K_1:
                if scoreList[0] == -1:
                    scoreList[0] = upperScore(myList, 1)
                    run = True
                    ruleSelected = True
                else:
                    showText("Category 6 has already been selected.")

                break
            elif event.key == pygame.K_2:
                if scoreList[1] == -1:
                    scoreList[1] = upperScore(myList, 2)
                    run = True
                    ruleSelected = True
                else:
                    showText("Category 6 has already been selected.")

                break
            elif event.key == pygame.K_3:
                if scoreList[2] == -1:
                    scoreList[2] = upperScore(myList, 3)
                    run = True
                    ruleSelected = True
                else:
                    showText("Category 6 has already been selected.")

                break
            elif event.key == pygame.K_4:
                if scoreList[3] == -1:
                    scoreList[3] = upperScore(myList, 4)
                    run = True
                    ruleSelected = True
                else:
                    showText("Category 6 has already been selected.")

                break
            elif event.key == pygame.K_5:
                if scoreList[4] == -1:
                    scoreList[4] = upperScore(myList, 5)
                    run = True
                    ruleSelected = True
                else:
                    showText("Category 6 has already been selected.")

                break
            elif event.key == pygame.K_6:
                if scoreList[5] == -1:
                    scoreList[5] = upperScore(myList, 6)
                    run = True
                    ruleSelected = True
                else:
                    showText("Category 6 has already been selected.")

                break
            elif event.key == pygame.K_RETURN:
                if numTries > 3:
                    showText("You only have a maximum 3 rolls before selecting a category")
                elif len(selectedList) == 0:
                    showText("You need to select one or more dices to roll again")
                else:
                    run = True

                break
        else:
            continue

    if run:
        if ruleSelected == False:
            d.reRoll(myList, selectedList)
            selectedList.clear()
            d.show(myList, 200, selectedList)
            numTries += 1

        if ruleSelected == True:
            d.show(myList, 200, set())
            textScreen("Press Enter to Continue")

            # New roll
            d.rollAll(myList)
            d.show(myList, 200, set())

            # Reset numTries for new roll
            numTries = 1

        if -1 not in scoreList:
            showText("Game End")
            textScreen("Press Enter to Continue")

            break

# Quits Game
pygame.quit()
quit()