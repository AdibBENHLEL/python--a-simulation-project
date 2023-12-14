import random
from  tkinter import ttk 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

class tunisien_twins():
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
        self.d.Tranf()
        self.d.create_deck()
        self.d.shuffle()
        self.c = self.d.drow()
        self.c1 = self.d.drow()
    def play(self):
        s = 0
        if (int(self.c.rank) < int(self.c1.rank)):
            s = 2
        return s

class desert_hearts():
    def __init__(self):

        self.d = deck()
        self.d.Tranf()
        self.d.create_deck()
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
                    #print("sahi verife il existe 3 conseutive ",test+1)
                    return 5
                test=0
                
            v=T[j]
            j+=1
        #print("out avec",test+1)  
        if test>=2 :
            return 5
        return 0
    
class Adib_Game():
    def __init__(self):
        self.d = deck()
        self.d.create_deck()
        self.d.shuffle()
        self.c = self.d.drow()
        self.c1 = self.d.drow()
    def play(self):
        s=0
        if (self.c.rank=='Queen' and self.c1.rank=='Queen' and self.c.couleur!=self.c1.couleur):
            s=20
        return s

def go(x):
    e={}
    s1,s2,s3,s4,s5,s6=0,0,0,0,0,0
    # x simulation number
    for i in range(x):
        c=sahara()
        s1=s1+c.play()

        c=tunisien_twins()
        s2=s2+c.play()

        c=medina_biggie()
        s3=s3+c.play()

        c=desert_hearts()
        s4=s4+c.play()

        c=Oasis_Runny()
        s5=s5+c.play()

        c=Adib_Game()
        s6=s6+c.play()
    # dictionnaire pour les résulta des jeux
    e["sahara"]=float(s1/x)
    e["tunisien_twins"]=float(s2/x)
    e["medina_biggie"]=float(s3/x)
    e["desert_hearts"]=float(s4/x)
    e["oasis_Runny"]=float(s5/x)
    e["Adib_Game"]=float(s6/x)
    return e

def diag_tab():
    ax1.clear()
    mes.config(text="")
    res.config(text="")
    res1.config(text="")

    #properties and layout of the diagram
    
    ax1.set_title("Game Performance Report ",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 20, "weight": "bold"})
    ax1.set_xlabel("Games",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 15, "weight": "bold"})
    ax1.set_ylabel("Wins",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 15, "weight": "bold"})
    
    
    simget= sim.get()
    getseed=seed.get()
    if simget and getseed :
        try:
            #appeler la fonction go
            a=go(int(simget))
            #fixer the seed number
            random.seed(int(getseed))
        except ValueError:# not number
            mes.config(text="Attention ** conversion error ** please enter valide number ")
    else:
        mes.config(text=" Attention **  empty string input ")

    plt.xticks(range(len(a)), a.keys(), rotation=20)
    
    global y
    y = a.values()
    ax1.bar(a.keys(), y)
    canvas1.draw()
    
    #remplir le tableau
    data=[]
    item_separation=("***","***","***")
    test=0
    nam=""
    for i,j in a.items():
        data.append((i,j,int(j*int(simget))))
        if j>=test :
            test=j
            name=i
    for item in data:
        treeview.insert('', 'end', values=item)
    treeview.insert('', 'end', values=item_separation)
    ch="summarizing the results:the new card game :"+name
    ch1="is the most attractive for players with pourcentage of winning per play :"+str(test)
    res.config(text=ch)
    res1.config(text=ch1)
    
#dictionnaire
a={}
#the main window
root = tk.Tk()
root.title("Tunisian Delight all right reserved ADIB_BH")
root.state('zoomed')

plt.rcParams["axes.prop_cycle"] = plt.cycler(
color=["#00BFFF", "#87CEEB", "#87CEFA", "#6495ED", "#4682B4"])


# definir the diagrame Frame utilusant matplotlib
fig1, ax1= plt.subplots()
y= a.values()
ax1.bar(a.keys(), y)
ax1.set_title("Game Performance Report ",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 20, "weight": "bold"})
ax1.set_xlabel("Games",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 15, "weight": "bold"})
ax1.set_ylabel("Wins",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 15, "weight": "bold"})




# definir the Testing Frame
side_frame = tk.Frame(root, bg="#00BFFF")
side_frame.pack(side="right", fill="y")

image = tk.PhotoImage(file="O57tTgmpqO78CwSDhvS2.png")
labpho = tk.Label(side_frame, image=image)
labpho.pack(side="top", fill="both", expand=True)


label = tk.Label(side_frame, text="Testing", bg="#0000FF", fg="#FFFF00", font="Helvetica 60 bold")
label.pack(pady=20, padx=20)

label1 = tk.Label(side_frame, text="Please enter the simulation number:", bg="#0000FF", fg="#FFFF00", font="Helvetica 20 bold")
label1.pack(pady=15, padx=20)

sim = tk.Entry(side_frame)
sim.config(font={"family": "Helvetica", "size": 70, "weight": "bold"})
sim.pack(pady=20, padx=20)

label2 = tk.Label(side_frame, text="Please enter the seed number:", bg="#0000FF", fg="#FFFF00", font="Helvetica 30 bold ")
label2.pack(pady=20, padx=20)


seed = tk.Entry(side_frame)
seed.config(font={"family": "Helvetica", "size": 70, "weight": "bold"})
seed.pack(pady=20, padx=20)

button = tk.Button(side_frame, text="submit",command=diag_tab,bg="#FFFF00", fg="#000000", font="Helvetica 40 bold ")
button.pack(pady=20, padx=20)

mes= tk.Label(side_frame,text=" ",bg="#00BFFF", fg="#FF0000", font="Helvetica 20 bold ")
mes.pack(pady=20, padx=20)

res= tk.Label(side_frame, text="",bg="#00BFFF",fg="#000000", font="Helvetica 15 bold ")
res.pack(pady=10, padx=20)
res1= tk.Label(side_frame, text="",bg="#00BFFF",fg="#000000", font="Helvetica 15 bold ")
res1.pack(pady=10, padx=20)

label3 = tk.Label(side_frame, text="CREATED BY BEN HLEL ADIB ", bg="#0000FF", fg="#FFFF00", font="Helvetica 20 bold ")
label3.pack(pady=20, padx=20)


charts_frame = tk.Frame(root)
charts_frame.pack()

lab = tk.Label(charts_frame, text="Tunisian Delight ", bg="#0000FF", fg="#FFFF00", font="Helvetica 45 bold ")
lab.pack(pady=25, padx=20) 


tab_frame = tk.Frame(charts_frame, bg="#00BFFF")
tab_frame.pack(side="bottom",fill="x")

labt = tk.Label(tab_frame, text="Table of simulation results", bg="#0000FF", fg="#FFFF00", font="Helvetica 30 bold ")
labt.pack(pady=25, padx=20)

treeview = tk.ttk.Treeview(tab_frame,columns=('game', '% of winner','winner in tunisian dinars'),show="headings")
treeview.pack(side="bottom",fill="x")
treeview.heading('game', text='game')
treeview.heading('% of winner', text='% of winner')
treeview.heading('winner in tunisian dinars', text='winner in tunisian dinars')

upper_frame = tk.Frame(charts_frame,bg="#00BFFF")
upper_frame.pack(fill="x")

labe= tk.Label(upper_frame, text="simulation results diagram", bg="#0000FF", fg="#FFFF00", font="Helvetica 30 bold ")
labe.pack(pady=25, padx=20)


canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

root.mainloop()



