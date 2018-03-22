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
from palette_drag_manager import Palette_drag_and_drop
from palette_frame import Palette_frame
from start_field_window import Start_Field_Window
from field_window import Field_window
from end_field_window import End_field
from reference_list_field import Reference_List_Window

class Dissector_builder_area(tk.Frame):
    
    def __init__(self, master=None):
        
        self.root = master
        master.geometry("800x600")
#        master.pack(expand=1, fill=tk.BOTH)
        
        master.title("Drop and drop demo")
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()
    
    def create_palette(self, root):
        palette_frame = tk.Frame(root)
        
        cf1 = Palette_frame(palette_frame, text = "Field", interior_padx = 6)
        cf1.pack()
        cf2 = Palette_frame(palette_frame, text = "Construct", interior_padx = 6)
        cf2.pack()
    
    
        field_items = ['Start Field', 'Field(1 Byte)', 'Field(2 Byte)', 'Field(4 Byte)',
                 'Field(8 Byte)', 'Field(16 Byte)', 'Field(Var Byte)', 'End Field',
                 'Reference List', 'Packet Info.']
        #whats inside folders
        for i, item in enumerate(field_items):
            dnd = Palette_drag_and_drop() #Should be in for loop
            button = tk.Button(cf1.interior, text = item)
            button.grid(row = i/2, column = i%2)
            dnd.add_dragable(button, 0, 0, self)
            
        construct_items = ['Expression', 'Connector' , '<', '>', '<=', '>=', '==', '~=', 'And', 'Or', 'Not', 'Operand']
        
        #whats inside folders
        for i, item in enumerate(construct_items):
            dnd = Palette_drag_and_drop() #Should be in for loop
            button = tk.Button(cf2.interior, text = item)
            button.grid(row = i/2, column = i%2)
            dnd.add_dragable(button, 0, 0, self)
        
        cf1._containerFrame.configure(width = 250)
        cf2._containerFrame.configure(width = 350)
        return palette_frame
    #Adds all the widgets.
    def _create_widgets(self):
        
        canvas = tk.Canvas(self)
        self.canvas = canvas
        canvas.pack(expand=1, fill=tk.BOTH)
#        palette = Palette_frame(self)
        palette = self.create_palette(self)
        palette_width = 200
        palette.place(x = 0, y = 0, width = palette_width, height = 300)
        
        
#        frame_A = tk.Frame(canvas, bg = 'green')
#        buttonA = tk.Label(frame_A, text = "Button A")
#        buttonB = tk.Label(canvas, text = "Button B")
#        
#        buttonC = tk.Label(canvas, text = "Button C")
#        buttonD = tk.Label(canvas, text = "Button D")
#        
#        buttonA_x = 50
#        buttonA_y = 50
#        
#        buttonB_x = 0
#        buttonB_y = 0
#        buttonA.place(x = buttonA_x, y = buttonA_y, height = 10, width = 60)
#        frame_A.place(x = 150, y = 50, height = 300, width = 300)
#        
#        buttonB.place(x = buttonB_x, y = buttonB_x, height = 10, width = 60)
#        
#        buttonC.place(x = 100, y = 100, height = 10, width = 60)
#        buttonD.place(x = 200, y = 200, height = 10, width = 60)
##        
#        
#        dnd_buttonA = Drag_and_drop()
#        dnd_buttonA.add_dragable(buttonA, buttonA_x, buttonA_y)
#        dnd_buttonB = Drag_and_drop()
#        dnd_buttonB.add_dragable(buttonB, buttonB_x, buttonB_y)
#        
    def handle_func(self, x, y, widget):
        
        if x > 200:
            print('add button to dissector builder')
            self.add_button(self.canvas, widget['text'])
            
        else:
            print('Do not add button')
        
        
#    def handle_func(A, B):
#        print('Handle function called!!')
    def add_button(self, canvas, object_type):
        print(object_type)
        if object_type == 'Start Field':
            start_field = Start_Field_Window(canvas)
            x, y = 175, 175
            start_field.place(x = x, y = y, height = 170, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(start_field, x, y)
            
#            pass
#        if object_type == 'Start Field':
#            button = tk.Label(canvas, text = "Start Field")
#            button.place(x = 175, y = 175, height = 10, width = 60)
        if object_type == 'Field(1 Byte)':
            field = Field_window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(2 Byte)':
            field = Field_window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(4 Byte)':
            field = Field_window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(8 Byte)':
            field = Field_window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(16 Byte)':
            field = Field_window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(Var Byte)':
            field = Field_window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
        if object_type == 'End Field':
            field = End_field(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 100, width = 200)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
            
        if object_type == 'Reference List':
            field = Reference_List_Window(canvas)
            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd = Drag_and_drop()
            dnd.add_dragable(field, x, y)
            
        if object_type == 'Packet Info.':
            button = tk.Label(canvas, text = 'Packet Info.')
            button.place(x = 175, y = 175, height = 10, width = 60)
        
        if object_type in ['Expression', 'Connector' , '<', '>', '<=', '>=', '==', '~=', 'And', 'Or', 'Not', 'Operand']:
            x, y = 175, 175
            button = tk.Label(canvas, text = object_type)
            button.place(x = 175, y = 175, height = 10, width = 60)
            dnd = Drag_and_drop()
            dnd.add_dragable(button, x, y)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = Dissector_builder_area(master=root)
    app.mainloop()
