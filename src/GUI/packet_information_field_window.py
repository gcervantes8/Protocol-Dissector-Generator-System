#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas

"""

import Tkinter as tk

class PacketInformationFieldWindow(tk.Frame):
    def _new_entry(self, frame, c, r):
        tk.Entry(frame).grid(column = c, row = r+1)
        tk.Entry(frame).grid(column = c+1, row = r+1)
        self.column = 0
        self.row +=1
        self.add_button.grid(column = 3,row = self.row)
        self.place(height=80 + ((self.row - 1) * 19))
    def init_window(self):

        frame = tk.Frame(self)
        frame.pack(side = tk.BOTTOM)
        tk.Label(frame, text = 'Value').grid(column = 0,row = 0)
        tk.Label(frame, text = 'Description').grid(column = 1, row = 0)
        entry1 = tk.Entry(frame)
        entry1.grid(column = 0, row = 1)
        entry2 = tk.Entry(frame)
        entry2.grid(column = 1, row = 1)
        self.add_button = tk.Button(frame, text="+", command = lambda: self._new_entry(frame,self.column,self.row))
        self.add_button.grid(column = 3, row = 1)



    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.column = 0
        self.row = 1
        self.add_button = None
        self.init_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = PacketInformationFieldWindow(root)
    app.pack()
    app.mainloop()