"""Creates a hand of 2 cards, has methods like "hit" that add cards, totals card value"""
from Deck import Deck
class Hand:
    def __init__(self, deck):
        self.deck = deck
        cardsInHand = []
        pointsInHand = 0
        cardsInHand.append(deck.draw())
        cardsInHand.append(deck.draw())
        self.cardsInHand = cardsInHand
        for card in cardsInHand:
            pointsInHand += int(card.score)
        self.pointsInHand = pointsInHand
        self.bust = False
        return
    def hit(self):
        deck = self.deck
        newcard = deck.draw()
        cardsInHand = self.cardsInHand
        cardsInHand.append(newcard)
        pointsInHand = self.pointsInHand
        print("Newcard value", int(newcard.score))
        pointsInHand = int(self.pointsInHand) + int(newcard.score)
        if pointsInHand > 21:
            self.bust = True
        print("New score", pointsInHand)
        return cardsInHand
