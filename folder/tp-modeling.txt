import random
# random.seed(619)


class Card():
    suit = ["diamond", "heart", "spade", "clover"]
    color = ["black", "red"]
    rank = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rank + " of " + self.suit)


class Deck():
    def __init__(self):
        self.deck = []
        for i in Card.rank:
            for j in Card.suit:
                card = Card(i, j)
                self.deck.append(card)

    def shuffle(self):
        shuffled_deck = []
        nbrs_used = []
        while len(shuffled_deck) < 52:
            nbr = random.randint(0, 51)
            if nbr not in nbrs_used:
                shuffled_deck.append(self.deck[nbr])
                nbrs_used.append(nbr)
        self.deck = shuffled_deck

    def draw(self):
        return self.deck.pop()


class Sahara_Ace:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        self.card = self.deck.draw()
        if self.card.rank == "1":
            return 10
        else:
            return 0


class Tunisian_Twins:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        self.card1 = self.deck.draw()
        self.card2 = self.deck.draw()
        if self.card1.rank == self.card2.rank or self.card1.suit == self.card2.suit:
            return 50
        else:
            return 0


class Medina_Biggie:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        self.card1 = self.deck.draw()
        self.card2 = self.deck.draw()
        if ranks[self.card2.rank] > ranks[self.card1.rank]:
            return 2
        else:
            return 0


class Desert_Hearts:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        revenue = 0
        self.card1 = self.deck.draw()
        self.card2 = self.deck.draw()
        self.card3 = self.deck.draw()
        drawn_cards = [self.card1, self.card2, self.card3]
        for i in drawn_cards:
            if i.suit == "heart":
                revenue += 1
        return revenue


class Oasis_Runny:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        self.card1 = self.deck.draw()
        self.card2 = self.deck.draw()
        self.card3 = self.deck.draw()
        self.card4 = self.deck.draw()
        self.card5 = self.deck.draw()
        drawn_cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
        sorted_cards = sort_cards(drawn_cards)
        for i in range(0, 3):
            if subset(sorted_cards[i:i + 3]):
                return 5
        return 0


def subset(list):
    if ranks[list[0].rank] == ranks[list[1].rank] - 1 and ranks[list[1].rank] == ranks[list[2].rank] - 1:
        return True
    return False


def sort_cards(cards):
    sorted_list = []
    for i in range(5):
        min = cards[0]
        for j in cards:
            rank1 = ranks[min.rank]
            rank2 = ranks[j.rank]
            if rank2 < rank1 and j not in sorted_list:
                min = j
        sorted_list.append(min)
        cards.remove(min)
    return sorted_list


def monte_carlo(game_class):
    wins = 0
    money_won = 0
    for i in range(100000):
        game = game_class()
        winnings = game.play()
        if winnings != 0:
            wins += 1
            money_won += winnings
    win_percentage = wins / 100000
    print("winning percentage=" + str(win_percentage))


ranks = {
    "1": 1,
    "K": 13,
    "Q": 12,
    "J": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}
monte_carlo(Sahara_Ace)
monte_carlo(Tunisian_Twins)
monte_carlo(Medina_Biggie)
monte_carlo(Desert_Hearts)
monte_carlo(Oasis_Runny)
