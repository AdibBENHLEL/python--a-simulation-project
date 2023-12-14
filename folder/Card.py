import random
class card():
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    def shuffle(self):
        suit= random.randint(0, 3)
        rank= random.randint(0, 12)
        if (suit <2):
            return self.suits[suit]+"   "+self.ranks[rank]+"    "+"red"
        else:
            return self.suits[suit]+"   "+self.ranks[rank]+"    "+"black"
c=card()
print(c.shuffle())
