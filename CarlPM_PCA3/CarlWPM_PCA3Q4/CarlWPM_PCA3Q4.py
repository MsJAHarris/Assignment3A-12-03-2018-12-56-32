# Problem Description:
# Please create a flowchart, IPO chart and trace table for a particular error you had while creating
# your work.  Please let me know which version you were on so that I may see the code and match up
# the trace table to that (now fixed) code.
#
# Your task:
# Create ONE of TWO games using the Card class you and your classmates created.
# a)	Easy choice (highest level possible is a Level 3).  In this option you will create a basic
# matching game.  Consider that Hearts and Diamonds match (red) and Spades and Clubs match (Black).
# You must use at least a 5 x 5 set of cards and  the entire deck.is at your disposal.  You will need
# complete instructions for your user.
#
# b)	More difficult option, (full marks possible). You will create the game of 21 or Blackjack,
# also using the Card class created in class. You will need complete instructions for your user.
# Date Begun:Nov 16

# Programmer:Carl W

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The program does appear to freeze up after launching, however it will still update after inputs through the console.
# I am unsure what the issue is, but it should still work most of the time if played quickly before window crashes.
# You will have to close it through pycharm if you want to avoid using task manager
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Modifications:
import pygame
import time
import os
import sys
import random
pygame.init()
# Print instructions
print("Welcome to Blackjack, your goal is to get a hand worth 21 or end with a higher valued hand than the dealer without exceeding 21.")
print("If you exceed 21 you lose. Hit to draw another card, or stand to pass your turn. Note that your aces could be worth 1 or 11.")
# Not using class given
# Creating class
class Card:
    def __init__(self, value, suit):
        # Creating the potential values and the suits to go with them
        self.values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', ]
        self.suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        self.value = value
        self.suit = suit
    # Creating functions to check value or suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit


# Creating Diamond cards
dA = Card('Ace','Diamonds')
d2 = Card(2, 'Diamonds')
d3 = Card(3, 'Diamonds')
d4 = Card(4, 'Diamonds')
d5 = Card(5, 'Diamonds')
d6 = Card(6, 'Diamonds')
d7 = Card(7, 'Diamonds')
d8 = Card(8, 'Diamonds')
d9 = Card(9, 'Diamonds')
d10 = Card(10, 'Diamonds')
dJ = Card('Jack', 'Diamonds')
dQ = Card('Queen', 'Diamonds')
dK = Card('King', 'Diamonds')
# Creating Heart cards
hA = Card('Ace','Hearts')
h2 = Card(2, 'Hearts')
h3 = Card(3, 'Hearts')
h4 = Card(4, 'Hearts')
h5 = Card(5, 'Hearts')
h6 = Card(6, 'Hearts')
h7 = Card(7, 'Hearts')
h8 = Card(8, 'Hearts')
h9 = Card(9, 'Hearts')
h10 = Card(10, 'Hearts')
hJ = Card('Jack', 'Hearts')
hQ = Card('Queen', 'Hearts')
hK = Card('King', 'Hearts')
# Creating Clubs cards
cA = Card('Ace','Clubs')
c2 = Card(2, 'Clubs')
c3 = Card(3, 'Clubs')
c4 = Card(4, 'Clubs')
c5 = Card(5, 'Clubs')
c6 = Card(6, 'Clubs')
c7 = Card(7, 'Clubs')
c8 = Card(8, 'Clubs')
c9 = Card(9, 'Clubs')
c10 = Card(10, 'Clubs')
cJ = Card('Jack', 'Clubs')
cQ = Card('Queen', 'Clubs')
cK = Card('King', 'Clubs')
# Creating Spades cards
sA = Card('Ace','Spades',)
s2 = Card(2, 'Spades')
s3 = Card(3, 'Spades')
s4 = Card(4, 'Spades')
s5 = Card(5, 'Spades')
s6 = Card(6, 'Spades')
s7 = Card(7, 'Spades')
s8 = Card(8, 'Spades')
s9 = Card(9, 'Spades')
s10 = Card(10, 'Spades')
sJ = Card('Jack', 'Spades')
sQ = Card('Queen', 'Spades')
sK = Card('King', 'Spades')

# The deck containing all the cards
deck = [dA, d2, d3, d4, d5, d6, d7, d8, d9, d10, dJ, dQ, dK, hA, h2, h3, h4, h5, h6, h7, h8, h9, h10, hJ, hQ, hK, cA,\
        c2, c3, c4, c5, c6, c7, c8, c9, c10, cJ, cQ, cK,sA, s2, s3, s4, s5, s6, s7, s8, s9, s10, sJ, sQ, sK]
# Determining the first card being drawn to start
first_card = random.choice(deck)
# Removing the card from the deck
deck.remove(first_card)

run = True
# White constant
WHITE = (255,255,255)
# Creating a play screen
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,200,0))
pygame.draw.rect(screen, (0,0,0), [260,675,100,60])
pygame.draw.rect(screen, (0,0,0), [260,200,100,60])
# Turn counter
turn = 0

while run:
    # Importing the function I created that was put on a separate file to make things easier to read
    from A3Q4Functions import evalCard
    # Determining the players first card using the function and then drawing it on screen
    if turn is 0:
        cardimage1 = evalCard(first_card)
        screen.blit(cardimage1,(500, 650))
        pygame.display.update()
        valAdd = 0
        # Adding the value of the card
        valAdd = first_card.getValue()
        # If the card is Jack, Queen, or King it will add 10 to the dealt values
        # Also tracking if the user already has an ace because the user can only ever have one ace that is valued at 11
        user_ace = False
        if first_card.getValue() is 'Jack':
            valAdd = 10
        if first_card.getValue() is 'Queen':
            valAdd = 10
        if first_card.getValue() is 'King':
            valAdd = 10
        if first_card.getValue() is 'Ace' and user_ace is True:
            valAdd = 1
        if first_card.getValue() is 'Ace' and user_ace is False:
            valAdd = 11
            user_ace = True
        # Tracking the players dealt values
        player_total = valAdd
        # Giving the second card for the beginning
        second_card = random.choice(deck)
        # Removing the card from the deck
        deck.remove(second_card)
        cardimage2 = evalCard(second_card)
        screen.blit(cardimage2, (530,650))
        valAdd = second_card.getValue()
        # If the card is Jack, Queen, or King it will add 10 to the dealt values
        if second_card.getValue() is 'Jack':
            valAdd = 10
        if second_card.getValue() is 'Queen':
            valAdd = 10
        if second_card.getValue() is 'King':
            valAdd = 10
        if second_card.getValue() is 'Ace' and user_ace is True:
            valAdd = 1
        if second_card.getValue() is 'Ace' and user_ace is False:
            valAdd = 11
            user_ace = True
        # Tracking the players dealt values
        player_total = player_total + valAdd
        # Showing the total on screen
        font = pygame.font.SysFont('Arial', 40)
        text = font.render(str(player_total), True, WHITE)
        screen.blit(text, [290,680])
        pygame.display.update()
        # Asking if user would like to gain another card or not

        # Now we draw the dealers cards by doing basically the same thing but changing where the cards are drawn
        dealer_card1 = random.choice(deck)
        deck.remove(dealer_card1)
        dealerimage1 = evalCard(dealer_card1)
        screen.blit(dealerimage1, (500, 200))
        dvalAdd = 0
        dvalAdd = dealer_card1.getValue()
        pygame.display.update()
        dvalAdd = dealer_card1.getValue()
        # If the card is Jack, Queen, or King it will add 10 to the dealt values
        if dealer_card1.getValue() is 'Jack':
            dvalAdd = 10
        if dealer_card1.getValue() is 'Queen':
            dvalAdd = 10
        if dealer_card1.getValue() is 'King':
            dvalAdd = 10
        if dealer_card1.getValue() is 'Ace' and user_ace is True:
            dvalAdd = 1
        if dealer_card1.getValue() is 'Ace' and user_ace is False:
            dvalAdd = 11
            user_ace = True
        # Tracking the dealer's combination
        dealer_total = dvalAdd
        # Dealer's second card

        dealer_card2 = random.choice(deck)
        deck.remove(dealer_card2)
        dealerimage2 = evalCard(dealer_card2)
        screen.blit(dealerimage2, (530, 200))
        pygame.display.update()
        dvalAdd = dealer_card2.getValue()# If the card is Jack, Queen, or King it will add 10 to the dealt values
        if dealer_card2.getValue() is 'Jack':
            dvalAdd = 10
        if dealer_card2.getValue() is 'Queen':
            dvalAdd = 10
        if dealer_card2.getValue() is 'King':
            dvalAdd = 10
        if dealer_card2.getValue() is 'Ace' and user_ace is True:
            dvalAdd = 1
        if dealer_card2.getValue() is 'Ace' and user_ace is False:
            dvalAdd = 11
            user_ace = True

        dealer_total = int(dealer_total) + int(dvalAdd)
        text2 = font.render(str(dealer_total), True, WHITE)
        screen.blit(text2, [290, 200])
        pygame.display.update()
        # Creating a while loop for multiple/consecutive decisions
        initial_setup = True
        # Future variable to shift cards over
        z = 530
        # Creating a variable to end the game
        game_over = False
        while initial_setup and game_over is False:
            # One special situation
            if player_total is 21 and dealer_total is 21:
                print('Nobody wins!')
            # If the user gets to 21 they instantly win
            if player_total is 21:
                print('You won!!')
                game_over = True
            # If the user gets over 21 they automatically lose
            if player_total > 21:
                print('The dealer wins!')
                game_over = True
            # If the dealer goes over 21 the player wins
            if dealer_total > 21:
                print('You won!')
                game_over = True
            # If the dealer has 21 and the user doesn't, the dealer wins
            if dealer_total is 21 and player_total is not 21:
                print('The dealer wins!')
                game_over = True
            decision = input('Would you like to HIT or STAND? h/s:')

            # If the player chooses not to draw any more cards
            if decision is 's':
                if dealer_total > player_total:
                    print('The dealer wins!')
                    game_over = True
                if player_total >= dealer_total:
                    # If the dealer is behind he will try to draw another card
                    new_dealer_card = random.choice(deck)
                    addx = new_dealer_card.getValue()
                    if new_dealer_card.getValue() is 'Jack':
                        addx = 10
                    if new_dealer_card.getValue() is 'Queen':
                        addx = 10
                    if new_dealer_card.getValue() is 'King':
                        addx = 10
                    if new_dealer_card.getValue() is 'Ace' and user_ace is True:
                        addx = 1
                    if new_dealer_card.getValue() is 'Ace' and user_ace is False:
                        addx = 11
                    deck.remove(new_dealer_card)
                    dealer_new_image = evalCard(new_dealer_card)
                    screen.blit(dealer_new_image, (z + 30, 200))
                    dealer_total = dealer_total + addx
                    # Displaying value of  dealer hand
                    text = font.render(str(dealer_total), True, WHITE)
                    pygame.draw.rect(screen, (0, 0, 0), [260, 200, 100, 60])
                    screen.blit(text, [290, 200])
                    pygame.display.update()
                    # If the dealer ends up with a higher hand that does not exceed 21, the dealer wins
                    if dealer_total > player_total and dealer_total <= 21:
                        print('The dealer wins!')
                        game_over = True
                    if dealer_total > 21:
                        print('You won!')
                        game_over = True
            # If the user decides to draw another card
            if decision is 'h':
                hit_card = random.choice(deck)
                add = hit_card.getValue()
                if hit_card.getValue() is 'Jack':
                    add = 10
                if hit_card.getValue() is 'Queen':
                    add = 10
                if hit_card.getValue() is 'King':
                    add = 10
                if hit_card.getValue() is 'Ace' and user_ace is True:
                    add = 1
                if hit_card.getValue() is 'Ace' and user_ace is False:
                    add = 11
                    user_ace = True
                # Removing card from the deck
                deck.remove(hit_card)
                new_image = evalCard(hit_card)
                screen.blit(new_image, (z + 30,650))
                player_total = player_total + add
                # Displaying value of hand
                text = font.render(str(player_total), True, WHITE)
                pygame.draw.rect(screen, (0, 0, 0), [260, 675, 100, 60])
                screen.blit(text, [290, 680])
                pygame.display.update()

        # Preventing the screen from closing
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
pygame.quit()