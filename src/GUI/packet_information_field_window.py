#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

import Tkinter as tk

def _new_entry(c,r):
    tk.Entry(root, text=" ").grid(column=c, row=r+1)
    tk.Entry(root, text=" ").grid(column=c+1, row=r+1)


root = tk.Tk()
root.wm_title('Packet Information')
tk.Label(root,text='Value').grid(column=0,row=0)
tk.Label(root,text='Description').grid(column=1, row=0)

tk.Entry(root, text = " ").grid(column = 0 , row = 1)
tk.Entry(root, text = " ").grid(column = 1 , row = 1)
tk.Button(root, text="+",command = lambda: _new_entry(0,1)).grid(column = 3, row = 2)
root.mainloop()



