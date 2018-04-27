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
        ph = tk.PhotoImage(file = path)

        tk.Label.__init__(self, master, image = ph)
        self.image = ph
#        self.pack()
#        self._create_widgets()
#        
#        
#
#    def _create_widgets(self):
#        
#        main_window = tk.Frame(self)
#        main_window.pack(side="top")
        
if __name__ == "__main__":
#    root = tk.Tk()
    root = tk.Toplevel()
    
    app = Expression_frame(master=root)
    app.mainloop()