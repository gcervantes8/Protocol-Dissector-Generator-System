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
from expression_frame import Expression_frame
from dissector_moving_frame import MovingFrame
#from connector import *
from connector_v2 import Connector

import xml.etree.cElementTree as ET
import xml.dom.minidom


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
            dnd = Palette_drag_and_drop() #Should be in for loop, so each has their own dnd instance
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
        
        canvas = tk.Canvas(self, width=1050, height=550)
        self.canvas = canvas
#        canvas.pack(expand=1, fill=tk.BOTH)
        canvas.grid(row = 0, column = 0)
#        palette = Palette_frame(self)
        palette = self.create_palette(self)
        palette_width = 190
        self.palette_height = 350
        palette.place(x = 0, y = 0, width = palette_width, height = self.palette_height)
        clear_button = tk.Button(canvas, text = "Clear", command = self.clear_canvas)
        clear_button.place(x = 0, y = self.palette_height + 10, height = 20, width = 70)
        
    def clear_canvas(self):
        self.canvas.delete("all")
        for child in self.canvas.winfo_children():
            child.destroy() 
        clear_button = tk.Button(self.canvas, text = "Clear", command = self.clear_canvas)
        clear_button.place(x = 0, y = self.palette_height + 10, height = 20, width = 70)
        
    def handle_func(self, x, y, widget):
        self.add_button(self.canvas, widget['text'])
        
    def add_button(self, canvas, object_type):
        x, y = 200, 175
        add_move_frame = True
        if object_type == 'Start Field':
            frame = Start_Field_Window(canvas)
            h, w = 110, 300
        elif object_type == 'Field(1 Byte)':
            frame = Field_window(canvas)
            h, w = 240, 300
        elif object_type == 'Field(2 Byte)':
            frame = Field_window(canvas)
            h, w = 240, 300
        elif object_type == 'Field(4 Byte)':
            frame = Field_window(canvas)
            h, w = 240, 300
        elif object_type == 'Field(8 Byte)':
            frame = Field_window(canvas)
            h, w = 240, 300
        elif object_type == 'Field(16 Byte)':
            frame = Field_window(canvas)
            h, w = 240, 300
        elif object_type == 'Field(Var Byte)':
            frame = Field_window(canvas)
            h, w = 240, 300
        elif object_type == 'End Field':
            frame = End_field(canvas)
            h, w = 40, 180
        elif object_type == 'Reference List':
            frame = Reference_List_Window(canvas)
            h, w = 100, 300
        elif object_type == 'Packet Info.':
            frame = PacketInformationFieldWindow(canvas)
            h, w = 90, 400
        elif object_type == 'Expression':
            frame = Expression_frame(canvas)
            h, w = 100, 200
        elif object_type in ['<', '>', '<=', '>=', '==', '~=', 'And', 'Or', 'Not', 'Operand']:
            frame = tk.Label(canvas, text = object_type)
            h, w = 12, 60
            
        elif object_type == 'Connector':
            Connector(canvas)
            add_move_frame = False
            
        if add_move_frame:            
            frame.place(x = x, y = y, height = h, width = w)
            mv = MovingFrame(canvas, frame, object_type, x, y)


if __name__ == "__main__":
    root = tk.Tk()
    app = Dissector_builder_area(master = root)
    app.mainloop()