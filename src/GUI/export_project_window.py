#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  20  2018

@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

from Tkinter import *

class Export_project():
    def __init__(self, master=None):
        self.root = master
        root.title("Export Project")
        root.geometry("500x250")
        self._create_widgets()

    def _create_widgets(self):
        desc = Label(root, text = "Export project to the local file system.")
        desc.config(font=("consolas", 12))
        desc.pack()

        frame1 = Frame(root)
        frame1.grid_propagate(0)
        frame1.grid_rowconfigure(0, weight = 1)
        frame1.grid_columnconfigure(0, weight = 1)
        frame1.pack(side = LEFT)

        p_label = Label(frame1, text = "Project")
        p_label.grid(row = 0)
        p_label.config(font=("consolas", 12))
        p_label.pack()

        to_export_label = Label(frame1, text = "To export file", pady = 20)
        to_export_label.grid(row = 1)
        to_export_label.config(font=("consolas", 12))
        to_export_label.pack()

if __name__ == "__main__":
    root = Tk()
    app = Export_project(master=root)
    root.mainloop()