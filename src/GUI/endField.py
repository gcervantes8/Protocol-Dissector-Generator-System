#! python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:29:57 2018
@author: Gerardo Cervantes
         Oliver Martinez
         Isaac Hoffman
         Daniel Ornelas
         Christopher Soto
"""

import Tkinter as tk

class Application(tk.Frame):

    # Function create frame with label on left, and entry on the right
    # Returns the frame with label and entry, and returns the entry

    def __init__(self, master=None):
        self.root = master
        master.title("End Field")
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()



    # Adds all the widgets.
    def _create_widgets(self):
        # Main window
        main_window = tk.Frame(self)
        main_window.pack(side="top")



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.geometry("300x50+150+150")
    app.mainloop()