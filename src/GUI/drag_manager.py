# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:35:49 2018

@author: Jerry C
"""

class Drag_and_drop():
    
    
    def add_dragable(self, widget, original_x, original_y):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")
        self.widget = widget
        self.x = original_x
        self.y = original_y
        
    def on_start(self, event):
        
        # you could use this method to create a floating window
        # that represents what is being dragged.
        x, y = event.widget.winfo_pointerxy()
        print(x, y)
        print("Drag started")
        
        print(event.x, event.y)
        self.init_touch_x, self.init_touch_y = event.x, event.y
        

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        drag_widget = self.widget

        if (drag_widget != None):
            pass
            
        else:
            print("Widget attempted to drag is of type None")
        pass

    def on_drop(self, event):
        
        print("Dropped")
        drag_widget = self.widget
        
        print('Prev x and y: ')
        print(self.x, self.y)
        print('Change in x and y')
        print(event.x, event.y)
        print('Initial touch pos')
        print(self.init_touch_x, self.init_touch_y)
        
        new_x = self.x + event.x - self.init_touch_x
        new_y = self.y + event.y - self.init_touch_y
        
        print('New x and y')
        print(new_x, new_y)
        
        
        drag_widget.place(x = new_x, y = new_y)
        self.x = new_x
        self.y = new_y
        
        target = event.widget.winfo_containing(new_x, new_y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass