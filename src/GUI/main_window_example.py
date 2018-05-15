# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:43:31 2018

@author: Some Stackoverflow guy
@resource: https://stackoverflow.com/questions/4055267/python-tkinter-mouse-drag-a-window-without-borders-eg-overridedirect1
"""

import Tkinter as tk
import tkFileDialog 

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)

        self.label = tk.Label(self, text="Click on the grip to move")
        self.grip = tk.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        self.label.pack(side="right", fill="both", expand=True)

        self.grip.bind("<ButtonPress-1>", self.StartMove)
        self.grip.bind("<ButtonRelease-1>", self.StopMove)
        self.grip.bind("<B1-Motion>", self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))


if __name__ == "__main__":
    app = App()
    app.mainloop()