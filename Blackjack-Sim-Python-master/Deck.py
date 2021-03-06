import random
class Card:
    """Makes a card with value and suit"""
    def __init__(self, cardvalue, cardsuit):
        self.value = cardvalue
        self.suit = cardsuit
        self.both = cardvalue + " of " + cardsuit
        cardscore = self.value
        isAce = False
        if self.value == "Jack":
            cardscore = 10
        if self.value == "Queen":
            cardscore = 10
        if self.value == "King":
            cardscore = 10
        if self.value == "Ace":
            cardscore = 1
            isAce = True
        self.score = cardscore
        self.isAce = isAce
        return

class Deck:
    """Makes a shuffled deck"""
    def __init__(self):
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        decklist = []
        for y in suits:
            for x in values:
                c = Card(x,y)
                decklist.append(c)
        random.shuffle(decklist)
        self.decklist = decklist
    def draw(self):
        decklist = self.decklist
        output = decklist.pop(0)
        return output
