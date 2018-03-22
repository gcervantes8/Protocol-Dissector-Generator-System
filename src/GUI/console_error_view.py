#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  21  2018

@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

import Tkinter as tk


class ConsoleErrorView(tk.Frame):
    def __init__(self, parent=None):
        self.root = parent
        root.title("Console Errors")
        tk.Frame.__init__(self)

        # block to control where window opens
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w = w/2
        h = h/2
        root.geometry("600x100+%d+%d" % (w-100, h-100))

        self._create_widgets()

    def _create_widgets(self):
        frame1 = tk.Frame(root)
        frame1.pack(side=tk.LEFT)

        desc = tk.Text(frame1, pady=10)
        desc.pack()

        desc.grid(row=0, column=0, sticky=tk.NW)

        desc.insert(tk.INSERT, "No error messages to display.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsoleErrorView(parent=root)
    root.mainloop()