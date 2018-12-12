# Defining a function to evaluate a card and load its image by looking at the different combinations and providing
import pygame
def evalCard(card):
    if card.getValue() is 'Ace':
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/ad.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/ah.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/ac.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/as.png')
            return cardimage
    if card.getValue() is 2:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/2d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/2h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/2c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/2s.png')
            return cardimage
    if card.getValue() is 3:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/3d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/3h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/3c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/3s.png')
            return cardimage
    if card.getValue() is 4:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/4d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/4h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/4c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/4s.png')
            return cardimage
    if card.getValue() is 5:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/5d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/5h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/5c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/5s.png')
            return cardimage
    if card.getValue() is 6:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/6d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/6h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/6c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/6s.png')
            return cardimage
    if card.getValue() is 7:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/7d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/7h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/7c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/7s.png')
            return cardimage
    if card.getValue() is 8:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/8d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/8h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/8c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/8s.png')
            return cardimage
    if card.getValue() is 9:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/9d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/9h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/9c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/9s.png')
            return cardimage
    if card.getValue() is 10:
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/10d.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/10h.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/10c.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/10s.png')
            return cardimage
    if card.getValue() is 'Jack':
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/jd.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/jh.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/jc.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/js.png')
            return cardimage
    if card.getValue() is 'Queen':
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/qd.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/qh.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/qc.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/qs.png')
            return cardimage
    if card.getValue() is 'King':
        if card.getSuit() is "Diamonds":
            cardimage = pygame.image.load('resources/cards/kd.png')
            return cardimage
        if card.getSuit() is "Hearts":
            cardimage = pygame.image.load('resources/cards/kh.png')
            return cardimage
        if card.getSuit() is 'Clubs':
            cardimage = pygame.image.load('resources/cards/kc.png')
            return cardimage
        if card.getSuit() is 'Spades':
            cardimage = pygame.image.load('resources/cards/ks.png')
            return cardimage
    run = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
    quit()