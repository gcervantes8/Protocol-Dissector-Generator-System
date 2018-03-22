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
from packet_information_field_window import PacketInformationFieldWindow


class Dissector_builder_area(tk.Frame):
    
    def __init__(self, master=None):
        
        self.root = master
        
        master.title("Dissector Builder Area")
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
        
        canvas = tk.Canvas(self, width=850, height=550)
        self.canvas = canvas
#        canvas.pack(expand=1, fill=tk.BOTH)
        canvas.grid(row=0,column=0)
#        palette = Palette_frame(self)
        palette = self.create_palette(self)
        palette_width = 200
        palette.place(x = 0, y = 0, width = palette_width, height = 800)
        

#        
    def handle_func(self, x, y, widget):
        self.add_button(self.canvas, widget['text'])
        
    def add_button(self, canvas, object_type):
        print(object_type)
        dnd = Drag_and_drop()
        x, y = 200, 175
        if object_type == 'Start Field':
            start_field = Start_Field_Window(canvas)
#            x, y = 175, 175
            start_field.place(x = x, y = y, height = 170, width = 300)
            dnd.add_dragable(start_field, x, y)
        if object_type == 'Field(1 Byte)':
            field = Field_window(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(2 Byte)':
            field = Field_window(canvas)
            
            field.place(x = x, y = y, height = 230, width = 300)
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(4 Byte)':
            field = Field_window(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(8 Byte)':
            field = Field_window(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(16 Byte)':
            field = Field_window(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd.add_dragable(field, x, y)
        if object_type == 'Field(Var Byte)':
            field = Field_window(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd.add_dragable(field, x, y)
        if object_type == 'End Field':
            field = End_field(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 100, width = 200)
            dnd.add_dragable(field, x, y)
            
        if object_type == 'Reference List':
            field = Reference_List_Window(canvas)
#            x, y = 175, 175
            field.place(x = x, y = y, height = 230, width = 300)
            dnd.add_dragable(field, x, y)
            
        if object_type == 'Packet Info.':
            
            field = PacketInformationFieldWindow(canvas)
#            x, y = 175, 175
            
            field.place(x = x, y = y, height = 330, width = 400)
            canvas.tag_raise(field)
            dnd.add_dragable(field, x, y)
        
        if object_type in ['Expression', 'Connector' , '<', '>', '<=', '>=', '==', '~=', 'And', 'Or', 'Not', 'Operand']:
#            x, y = 175, 175
            button = tk.Label(canvas, text = object_type)
            button.place(x = 175, y = 175, height = 12, width = 60)
            dnd.add_dragable(button, x, y)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = Dissector_builder_area(master = root)
    app.mainloop()
