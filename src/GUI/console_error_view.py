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
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.root = parent
       # root.title("Console Errors")

        # block to control where window opens
        # w = self.root.winfo_screenwidth()
        # h = self.root.winfo_screenheight()
        # w = w/2
        # h = h/2
        # self.root.geometry("600x100+%d+%d" % (w-100, h-100))

        self._create_widgets()

    def _create_widgets(self):
        frame1 = tk.Frame(self.root)
        frame1.pack()

        desc = tk.Text(frame1)
        desc.pack()

        desc.grid(row=0, column=0)

        desc.insert(tk.INSERT, "No error messages to display.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsoleErrorView(parent=root)
    root.mainloop()