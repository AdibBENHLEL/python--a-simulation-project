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
        for i in range(14):
            self.ranks[i]=str(i+1)
                
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
   
class Game_class():
    def __init__(self,name):
        self.name=name
        
    def play(self):
        match self.name :
            case "sahara":
                s=sahara()
                s.play()
            case "tunisien_twins" :
                t=tunisien_twins()
                t.play()
            case "medina_biggie":
                m=medina_biggie()
                m.play()
            case "desert_hearts":
                d=desert_hearts()
                d.play()
            case "Mygame":
                M=Mygame()
                M.play()
            case _:
                print("erreur")
                
    
class sahara:
    def __init__(self):
        self.d = deck()
        self.d.create_deck()
        self.d.shuffle()
        self.c = self.d.drow()

    def play(self):
        s = 0
        if self.c.rank == 'Ace':
            s = 10
        return s
        
"""class tunisien_twins():
    def __init__(self):
        self.d = deck()
        self.d.create_deck()
        self.d.shuffle()
        self.c = self.d.drow()
        self.c1 = self.d.drow()
    def play(self):
        s=0
        if (self.c.rank==self.c1.rank and self.c.suit==self.c1.suit and self.c.couleur==self.c1.couleur):
            s=50
        return s
            
            
class medina_biggie():
    def __init__(self):
        self.d = deck()
        self.d.create_deck()
        self.d.Tranf()
        self.d.shuffle()
        self.c = self.d.drow()
        self.c1 = self.d.drow()

    def play(self):
        s = 0
        if int(self.c.rank) < int(self.c1.rank):
            s = 2
        return s
        
class desert_hearts():
    def __init__(self):
        
        self.d = deck()
        self.d.create_deck()
        self.d.Tranf()
        self.d.shuffle()
        self.c = self.d.drow()
        self.c1 = self.d.drow()
        self.c2 = self.d.drow()
    def play(self):
        s=0
        for i in [self.c,self.c1,self.c2]:
            if (i.suit=='Hearts'):
                s+=1
        return s
        
class Oasis_Runny():
    def __init__(self):
        self.d=deck()
        self.d.Tranf()
        self.d.creat_deck()
    def play(self):
        T=[]
        for i in (0,4):
            self.d.shuffle()
            T[i]=self.d.drow()
        s=0
        for j in T:
            if (int(T[j+1].rank)-int(T[j].rank)==1):
                j=j+1
            else :
                if j>=3  :
                    return 5
                else:
                    return 0
class Mygame():
    def __init__(self):
        self.d=deck()
        self.d.creat_deck()
        self.c1=self.d.drow()
        self.c2=self.d.drow()
    def play(self):
        s=0
        if (self.c.rank=='Queen' and self.c1.rank=='Queen' and self.c.couleur!=self.c1.couleur):
            s=20
        return s"""
c=sahara()
print(c.play())