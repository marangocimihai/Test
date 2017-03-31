#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *
import sqlite3


class UI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Buttons")
#        self.style = Style()
#        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        encrypt_button = Button(self, text="Encrypt")
        decrypt_button = Button(self, text="Decrypt")
        decrypt_button.pack(side=RIGHT)
        encrypt_button.pack(side=RIGHT, padx=5, pady=5)
        self.connect_to_database()

    def connect_to_database(self):
        conn = sqlite3.connect('C:\Users\marangocimihai\Desktop\db.db')
        c = conn.cursor()
        c.execute('SELECT * FROM TEST')
        print c.fetchall()

def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = UI(root)
    app.grid(row=5, column=2)
    root.mainloop()

if __name__ == '__main__':
    main()