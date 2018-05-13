# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:04:36 2018

@author: Gerardo Cervantes
"""

import Tkinter as tk
from connector_drag import Drag_and_drop_connector

class Connector():

    
    def __init__(self, master = None):
        self.root = master
        d1 = Drag_and_drop_connector()
        point_1 = tk.Label(master, text="X", relief = tk.RAISED)
        x1, y1 = 200, 175
        point_1.place(x = x1, y = y1, height = 12, width = 12)
        d1.add_dragable(point_1, x1, y1, self, 'p1')
        
        d2 = Drag_and_drop_connector()
        point_2 = tk.Label(master, text="X", relief = tk.RAISED)
        x2, y2 = 300, 180
        point_2.place(x = x2, y = y2, height = 12, width = 12)
        d2.add_dragable(point_2, x2, y2, self, 'p2')
        self.line = master.create_line(x1, y1, x2, y2, fill="red")
        
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        print('No err9')

    def connector_dragged(self, con_type, x, y):
        
        if 'p1' == con_type:
            self.x1, self.y1 = x, y
        elif 'p2' == con_type:
            self.x2, self.y2 = x, y
            
        canvas = self.root
        
        canvas.delete(self.line)
        self.line = canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="red")

        
if __name__ == "__main__":
    root = tk.Tk()
    app = Connector(master=root)
    app.mainloop()