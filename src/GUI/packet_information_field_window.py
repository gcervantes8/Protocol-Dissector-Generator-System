#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas

"""

import Tkinter as tk
import ttk

class PacketInformationFieldWindow(tk.Frame):
    def _new_entry(self, frame, c, r):
        tk.Entry(frame, text = " ").grid(column = c, row = r+1)
        tk.Entry(frame, text = " ").grid(column = c+1, row = r+1)
        self.column = 0
        self.row +=1
    def init_window(self):

        #root.wm_title('Packet Information')

        frame = tk.Frame(self)
        frame.pack()
        tk.Label(frame,text='Value').grid(column=0,row=0)
        tk.Label(frame,text='Description').grid(column=1, row=0)
        entry1 = ttk.Entry(frame)
        entry1.grid(column = 0 , row = 1)
        entry2 = ttk.Entry(frame)
        entry2.grid(column = 1 , row = 1)
        tk.Button(frame, text="+",command = lambda: self._new_entry(frame,self.column,self.row)).grid(column = 3, row = 2)



    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.root = parent
        self.column = 0
        self.row = 1
        self.init_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = PacketInformationFieldWindow(root)
    app.pack()
    app.mainloop()