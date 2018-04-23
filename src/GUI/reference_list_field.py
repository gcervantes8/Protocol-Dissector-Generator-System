# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:05:42 2018

@author: revil0mg
"""

import Tkinter as tk
import ttk
from moving_frame import MovingFrame

class Reference_List_Window(MovingFrame):
    def _new_entry(self, frame, c, r):
        tk.Entry(frame).grid(column = c, row = r+1)
        tk.Entry(frame).grid(column = c+1, row = r+1)
        self.column = 0
        self.row +=1
        self.add_button.grid(column=3,row=self.row)
        
    def init_window(self,parent):

        frame = tk.Frame(parent)
        frame.pack()
        tk.Label(frame,text='Reference List Name').grid(column=0,row=0)
        entryRLN = ttk.Entry(frame)
        entryRLN.grid(column = 1 , row = 0)
        tk.Label(frame,text='Value').grid(column=0,row=1)
        tk.Label(frame,text='Text Description').grid(column=1, row=1)
        entry1 = ttk.Entry(frame)
        entry1.grid(column = 0 , row = 2)
        entry2 = ttk.Entry(frame)
        entry2.grid(column = 1 , row = 2)
        self.add_button = tk.Button(frame, text="+",command = lambda: self._new_entry(frame,self.column,self.row))
        self.add_button.grid(column = 3, row = 2)



    def __init__(self, parent):

        self.root = parent
        mv = MovingFrame(self.root,"Reference List [Name]",200,200,300,300)
        self.column = 0
        self.row = 2
        self.add_button = None
        self.init_window(mv.f)

if __name__ == "__main__":
    root = tk.Tk()
    Reference_List_Window(root)

    root.mainloop()