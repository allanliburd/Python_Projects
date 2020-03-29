from card import Card
from deck import Deck
import logging

class Hand:
    def __init__(self, name):
        self._name = "Player " + name
        self._cards = []
    
    def __repr__(self):
        return (self._name + " has " + str(len(self._cards)) + " cards")
        
    def pick(self, deck):
        self._cards.append(deck.give())

test = 1
if (test):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    player_names = ["Allan", "Bernard", "Charlotte", "Dolores", "Eddie", "Frank", "George", "Hector"]
    my_deck = Deck()
    my_deck.shuffle()
    hands = []
    for player in player_names:
        tempHand = Hand(player)
        tempHand._cards = my_deck.deal()
        hands.append(tempHand)
#     player_1 = Hand("Allan")
#     player_1._cards = (my_deck.deal())
#     player_2 = Hand("Bernard")
#     player_2._cards = (my_deck.deal())
    hands[0].pick(my_deck)
    my_deck.check(hands[0]._cards[2])
    for i in range(0,len(hands)):
        logger.debug( str(hands[i]) )
