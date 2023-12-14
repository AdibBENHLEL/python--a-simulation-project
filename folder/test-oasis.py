import random
class card():
    def __init__(self,rank,suit,couleur):
        self.rank=rank
        self.suit=suit
        self.couleur=couleur


class deck():

    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deckk=[]

    def Tranf(self):
        for i in range(13):
            self.ranks[i]=str(i+2)

    def create_deck(self):
        for i in self.suits:
            for j in self.ranks:
                if i in ["Hearts", "Diamonds"]:
                    co = "red"
                else:
                    co = "black"
                self.deckk.append(card(j, i, co))
        return self.deckk


    def shuffle(self):
        deck_shuffled=[]
        nbr=[]
        while True:
            nb= random.randint(0, 51)
            if not(nb in nbr):
                deck_shuffled.append(self.deckk[nb])
                nbr.append(nb)
            if(len(nbr)==52):
                self.deckk=deck_shuffled
                break
    def drow(self):
        nb= random.randint(0, 51)
        return (self.deckk[nb])


class Oasis_Runny():
    def __init__(self):
        self.d = deck()
        self.d.Tranf()
        self.d.create_deck()
        self.d.shuffle()
    def play(self):
        T=[]
        d1=self.d.drow()
        T.append(int(d1.rank))
        d2=self.d.drow()
        T.append(int(d2.rank))
        d3=self.d.drow()
        T.append(int(d3.rank))
        d4=self.d.drow()
        T.append(int(d4.rank))
        d5=self.d.drow()
        T.append(int(d5.rank))
        j=1
        v=T[0]
        test=0
        while j<5 :
            if (T[j]==v+1):
                test+=1
            else :
                if test==2 :
                    print("sahi verife",test+1)
                    return 5
                test=0
                
            v=T[j]
            j+=1
        print("out avec",test+1)  
        if test>=2 :
            return 5
        return 0

c=Oasis_Runny()

print(c.play())
