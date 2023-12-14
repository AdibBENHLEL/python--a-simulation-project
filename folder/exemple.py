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
        nb=14
        for i in range (len(self.ranks),len(self.ranks)-4,-1):
            self.ranks[i]=str(nb)
            nb-=1
                
    def creat_deck(self):
       for i in self.suits:
           for j in self.ranks:
               if i in ["Hearts", "Diamonds"]:
                  co="red"
               else:
                  co="black"
                c=card(j,i,co)
                self.deckk.append(c)

    def shuffle(self)
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
   
class Game_class()
    def __init__(self,name):
        self.name=name
        
    def play(self):
        match name :
            case "sahara":
                s=sahra()
                s.play()
            case "tunisien_twins" :
                t=tunisien_twins()
                t.play()
            case "medina_biggie":
                m=medina_biggie()
                m.play()
            case "desert_hearts":
                d=sahra()
                d.play()
            case "Mygame":
                M=sahra()
                M.play()
            case _:
                print("erreur")
                
    
class sahara()
    def __init__(self):
        self.d=deck()
        self.d.creat_deck()
        self.d.shuffle()
        self.c=self.d.drow()
     def play(self):
         s=0
         if (self.c.rank=='Ace'):
           s=10
         return s
        
class tunisien_twins()
    def __init__(self):
        self.d=deck()
        self.d.creat_deck()
        self.d.shuffle()
        self.c=.d.drow()
        self.c1=.d.drow()
    def play(self):
        s=0
        if (self.c.rank==self.c1.rank and self.c.suit==self.c1.suit and self.c.couleur==c1.couleur):
            s=50
        return s
            
            
class medina_biggie():
    def __init__(self):
        self.d=deck()
        self.d.Tranf()
        self.d.creat_deck()
        self.d.shuffle()
        self.c=d.drow()
        self.c1=d.drow()
   def play(self):
       s=0
       if (int(self.c.rank)<int(self.c1.rank)):
            s=2
        return s
        
class desert_hearts():
    def __init__(self):
        
        self.d=deck()
        self.d.Tranf()
        self.d.creat_deck()
        self.d.shuffle()
        self.c=d.drow()
        self.d.shuffle()
        self.c1=d.drow()
        self.d.shuffle()
        self.c2=d.drow()
        
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
            if (int(T[j+1].rank)-int(T[j].rank)=1):
                j++
            else :
                if j>=3  :
                    return (s=5)
                else
                    return s
class Mygame():
    def __init__(self):
        self.d=deck()
        self.d.creat_deck()
        self.c1=d.drow()
        self.c2=d.drow()
    def play(self):
        s=0
        if (self.c.rank=='Queen' and self.c1.rank=='Queen' and self.c.couleur!=self.c1.couleur)
            s=20
        return s
    