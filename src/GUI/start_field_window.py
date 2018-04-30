# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:29:57 2018

@author: Gerardo Cervantes
         Oliver Martinez
         Isaac Hoffman
         Daniel Ornelas
         Christopher Soto
"""

#TODO: add transparent words in Dependency Pattern label

import Tkinter as tk


class Start_Field_Window(tk.Frame):
    
    #Function create frame with label on left, and entry on the right
    #Returns the frame with label and entry, and returns the entry
    def create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)
        
        entry = tk.Entry(main_frame)
        entry.pack(side="right")
        
        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")
        
        return main_frame, entry
    
    def __init__(self, master = None):
        self.root = master
#        self.root.title("Start Field [Protocol Name]")
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        main_window = tk.Frame(self)
        main_window.pack(side="top")
        
        name_frame, self.protocol_name_entry = self.create_frame_with_entry(main_window, "Protocol Name")
        desc_frame, self.protocol_desc_desc_entry = self.create_frame_with_entry(main_window, "Protocol Description")
        depend_name_frame, self.dependent_protocol_name_entry = self.create_frame_with_entry(main_window, "Dependent Protocol Name")
        depend_pattern_frame, self.dependency_pattern_entry = self.create_frame_with_entry(main_window, "Dependency Pattern")
        
        buttons_frame = tk.Frame(main_window)

        name_frame.grid(row = 0, column = 0)
        desc_frame.grid(row = 1, column = 0)
        depend_name_frame.grid(row = 2, column = 0)
        depend_pattern_frame.grid(row = 3, column = 0)
        buttons_frame.grid(row = 4, column = 0)
    
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Start_Field_Window(master=root)
    app.mainloop()