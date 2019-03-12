"""Asks how many players, creates 1 hand for dealer and 1 hand for each player"""
from Deck import Deck
from Hand import Hand
playernumber = input("How many Players?: ")
handcount = int(playernumber) + 1
print(handcount)

d = Deck()
hand = Hand(d)
for x in hand.cardsInHand:
    print(x.both)
print("Score:")
print(hand.pointsInHand)
print("Hit 'H'  :  Stay 'S'")
x = input("Hit  'H'  :  Stay 'S'")
if x.upper() == "H":
    print("Hit")
    for x in hand.cardsInHand:
        print(x.both)
    print("Score:")
    print(hand.pointsInHand)
    x = input("you hit")
