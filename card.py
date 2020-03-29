class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
    def __repr__(self):
        return self.number + " of " + self.suit
    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print(suit + " is not a valid suit!")
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            self._number = number
        else:
            print(number + " is not a valid number!")

test = 0
if (test):
    my_card = Card ("hearts", "6")
    print(my_card)
    c4s = Card ("spades", "4")
    c4s.suit = "SPADES"
    print(c4s)
    c11d = Card ("diamondss", "11")
    c11d.number = "11"
    print(c11d)
