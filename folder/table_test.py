# Python program to create a table

from tkinter import *


class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=20, fg='blue',
							font=('Arial',16,'bold'))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Raj','Mumbai',19),
	(2,'Aaryan','Pune',18),
	(3,'Vaishnavi','Mumbai',20),
	(4,'Rachna','Mumbai',21),
	(5,'Shubham','Delhi',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()



"""
frameM = tk.Frame(root, bg="#00BFFF")
frameM.pack(side="left")
label = tk.Label(frameM, text="Result", bg="#0000FF", fg="#FFFF00", font="Helvetica 80 bold")

root = tk.Tk()

framet = tk.Frame(root, bg="#00BFFF")
framet.pack(side="bottom", fill="x")

table = tk.Table(framet)
table.pack()
"""



"""
fig1, ax1 = plt.subplots()

table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ax1.table(table, loc='center', cellalign='center')

plt.draw()


frame3= tk.Tk()
canvas1 = FigureCanvasTkAgg(fig,frame3)


canvas1.pack()

fig1, ax1 = plt.subplots()
table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
table.set_cell(3,3 , value="New value", align="center")
ax1.table(table, loc='center', cellalign='center')
plt.draw()
root = tk.Tk()
canvas = FigureCanvasTkAgg(fig1, master=root)
canvas.pack()



fig2, ax2 = plt.subplots()
table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ax2.set_title("Game Performance Report Table ",ha="center",color="#0000FF", fontdict={"family": "Helvetica", "size": 20, "weight": "bold"})
ax2.table(table, loc='center', cellalign='center')

"""
