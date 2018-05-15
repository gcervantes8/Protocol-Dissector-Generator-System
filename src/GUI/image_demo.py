# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:33:05 2018

@author: Jerry C
"""

import Tkinter as tk

root = tk.Toplevel()
frame = tk.Frame(root)
path = '../Images/a.gif'
#im = tk.1Image.open(path)
ph = tk.PhotoImage(file = path)

#image = tk.PhotoImage(file = path)
button = tk.Button(frame, image = ph)
button.image = ph
#button.image=ph 
button.pack()
frame.pack()
root.mainloop()

while(1):
    pass