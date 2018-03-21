# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:42:36 2018

@author: Jerry C
"""

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
from drag_manager import Drag_and_drop


class Application(tk.Frame):
    
    def __init__(self, master=None):
        
        self.root = master
        master.geometry("500x250")
        master.title("Drop and drop demo")
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()
    
    #Adds all the widgets.
    def _create_widgets(self):
        
        canvas = tk.Canvas(self)
        canvas.pack(expand = True, fill = "both")
        
        buttonA = tk.Label(canvas, text = "Button A")
        buttonB = tk.Label(canvas, text = "Button B")
        
        buttonC = tk.Label(canvas, text = "Button C")
        buttonD = tk.Label(canvas, text = "Button D")
        
        buttonA_x = 50
        buttonA_y = 50
        
        buttonB_x = 0
        buttonB_y = 0
        buttonA.place(x = buttonA_x, y = buttonA_y, height = 10, width = 60)
        
        buttonB.place(x = buttonB_x, y = buttonB_x, height = 10, width = 60)
        
        buttonC.place(x = 100, y = 100, height = 10, width = 60)
        buttonD.place(x = 200, y = 200, height = 10, width = 60)
        
        
        dnd_buttonA = Drag_and_drop()
        dnd_buttonA.add_dragable(buttonA, buttonA_x, buttonA_y)
        dnd_buttonB = Drag_and_drop()
        dnd_buttonB.add_dragable(buttonB, buttonB_x, buttonB_y)
#        

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
