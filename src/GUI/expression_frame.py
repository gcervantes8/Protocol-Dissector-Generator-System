# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:37:19 2018

@author: Gerardo Cervantes
"""


import Tkinter as tk


class Expression_frame(tk.Label):
    

    def __init__(self, master=None):
        self.root = master
        path = '../Images/Expression.gif'
        image = tk.PhotoImage(file = path)

        tk.Label.__init__(self, master, image = image)
        self.image = image
        
if __name__ == "__main__":
    root = tk.Toplevel()
    app = Expression_frame(master=root)
    app.mainloop()