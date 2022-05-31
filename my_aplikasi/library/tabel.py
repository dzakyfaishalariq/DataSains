import sys
import tkinter as tk
from tkinter import ttk


class Tabel:
    def __init__(self):
        self.win = tk.Tk()
        self.tabel = ttk.Treeview(
            self.win, columns=('#nama', '#alamat', '#telp'))
        self.tabel.column('#nama', width=100, minwidth=100)
        self.tabel.column('#alamat', width=200, minwidth=200)
        self.tabel.column('#telp', width=100, minwidth=100)
        self.tabel.heading('#nama', text='Nama')
        self.tabel.heading('#alamat', text='Alamat')
        self.tabel.heading('#telp', text='Telp')
        for i in range(1, 11):
            self.tabel.insert('', 'end', text=i, values=(
                'Nama ' + str(i), 'Alamat ' + str(i), 'Telp ' + str(i)))
        self.tabel.pack()
        self.win.mainloop()


Tabel()
sys.exit()
