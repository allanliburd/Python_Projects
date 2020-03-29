from card import Card
import random

class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        #print(self._cards)
        
    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        #numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        cards = [] # create an empty list
        for suit in suits:
            for number in numbers:
                # Create a new Card object and append it to the cards list
                cards.append( Card(suit, number))
        # This can also be written as a list comprehentsion
        #seff._cards = [ Card(s, n) for s in suits for n in numbers]       
        self._cards = cards
        print("There are " + str(len(self._cards)) + " cards in the deck!")

    def shuffle(self):
        numCards = len(self._cards)
        for i in range (0, int (numCards/2)):
            temp = self._cards[i]
            nIndex = random.randint(0, numCards -1)
            self._cards[i] = self._cards[nIndex]
            self._cards[nIndex] = temp
        print("Shuffled " + str(len(self._cards)) + " cards in the deck!")
        print (self._cards)

    def check(self, card):
        if card in self._cards:
            print( str(card) + " is in the Deck")
        else:
            print( str(card) + " is NOT in the Deck")

    def give(self):
        if (len(self._cards) == 0):
            print("There are no cards left!")
        else:
            card = self._cards[0]
            del(self._cards[0])
            return card
    
    def deal(self):
        hand = []
        nCards = 5
        if (nCards > len(self._cards)):
            print ("Not enough cards to deal")
            return hand
        for i in range(0,nCards):
            hand.append(self._cards[0])
            del(self._cards[0])
        print(hand)
        print("Dealt " + str(len(hand)) + " cards from the deck!")
        print("Remaining " + str(len(self._cards)) + " cards from the deck!")
        return hand

test = 0
if (test):
    my_deck = Deck()
    my_deck.shuffle()
    print("Deal 5 cards from the deck:")
    player_1 = my_deck.deal()
    bad_card = ("diamonds", "11")
    my_deck.check(bad_card)
    print("Deal 5 cards from the deck:")
    player_2 = my_deck.deal()
