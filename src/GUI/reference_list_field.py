# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:05:42 2018

@author: revil0mg
"""

import Tkinter as tk

class Reference_List_Window(tk.Frame):
    def _new_entry(self, frame, c, r):
        tk.Entry(frame).grid(column = c, row = r+1)
        tk.Entry(frame).grid(column = c+1, row = r+1)
        self.column = 0
        self.row +=1
        self.add_button.grid(column=3,row=self.row)
        
        #Increase height of window
        self.place(height = 80 + ((self.row-1) * 19))
        
    def init_window(self,parent):

        frame = tk.Frame(parent)
        frame.pack(side = tk.BOTTOM)
        tk.Label(frame,text='Reference List Name').grid(column = 0,row = 0)
        entryRLN = tk.Entry(frame)
        entryRLN.grid(column = 1 , row = 0)
        tk.Label(frame,text = 'Value').grid(column = 0,row = 1)
        tk.Label(frame,text ='Text Description').grid(column = 1, row = 1)
        entry1 = tk.Entry(frame)
        entry1.grid(column = 0 , row = 2)
        entry2 = tk.Entry(frame)
        entry2.grid(column = 1 , row = 2)
        self.add_button = tk.Button(frame, text="+",command = lambda: self._new_entry(frame,self.column,self.row))
        self.add_button.grid(column = 3, row = 2)



    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side = tk.BOTTOM)
        self.root = parent
        self.column = 0
        self.row = 2
        self.add_button = None
        self.init_window(self)

if __name__ == "__main__":
    root = tk.Tk()
    Reference_List_Window(root)

    root.mainloop()