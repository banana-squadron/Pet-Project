from Hand import Hand
from Deck import Deck
import msvcrt
deck = Deck()
hand = Hand(deck)
while hand.pointsInHand <= 21:
    print("Currently cards in hand are ...")
    for x in hand.cardsInHand:
        print(x.both)
    input = msvcrt.getch()
    print("Input is ", input)
    if input.upper() == b'H':
        print("triggered")
def inputSwitch(argument):
    switcher = {
    1: "b'H'",
    2: "b'"
    }
