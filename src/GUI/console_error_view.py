#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  21  2018

@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

from Tkinter import *


class ConsoleErrorView():
    def __init__(self, master=None):
        self.root = master
        root.title("Console Errors")

        # block to control where window opens
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w = w/2
        h = h/2
        root.geometry("600x100+%d+%d" % (w-100, h-100))

        self._create_widgets()

    def _create_widgets(self):
        frame1 = Frame(root)
        frame1.pack(side=LEFT)

        desc = Text(frame1, pady=10)
        desc.pack()

        desc.grid(row=0, column=0, sticky=NW)

        desc.insert(INSERT, "No error messages to display.")

if __name__ == "__main__":
    root = Tk()
    app = ConsoleErrorView(master=root)
    root.mainloop()