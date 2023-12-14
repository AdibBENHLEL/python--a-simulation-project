import tkinter as tk
from tkintertable import Table

class ExampleApp:
    def __init__(self):
        self.root = tk.Tk()

        # Create a frame to hold the table
        self.framet = tk.Frame(self.root)
        self.framet.pack()

        # Create a table
        self.table = Table(self.framet)
        self.table.pack()

        # Add some data to the table
        self.table.insert('', 'end', values=('column_1', 'column_2', 'column_3'))

        # Display the table
        self.root.mainloop()

if __name__ == '__main__':
    app = ExampleApp()
