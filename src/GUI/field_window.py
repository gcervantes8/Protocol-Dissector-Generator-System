     #! python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:29:57 2018

@author: Gerardo Cervantes
"""

import Tkinter as tk


class Field_window(tk.Frame):
    
    
    #Function create frame with label on left, and entry on the right
    #Returns the frame with label and entry, and returns the entry
    def _create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)
        
        entry = tk.Entry(main_frame)
        entry.pack(side="right")
        
        tk.Label(main_frame, text = label_str).pack(side="left")
        
        return main_frame, entry
    
    #Function create frame with label on left, and dropdown menu on the right
    #Returns the frame with label and dropdown menu, and returns the dropdown menu
    def _create_frame_with_menu(self, parent_frame, label_str, OPTIONS):
        main_frame = tk.Frame(parent_frame)
        
        variable = tk.StringVar(main_frame)
        variable.set(OPTIONS[0]) # default value

        option_menu = tk.OptionMenu(main_frame, variable, *OPTIONS)
        option_menu.pack(side="right")      
        
        tk.Label(main_frame, text = label_str).pack(side="left")
        return main_frame, option_menu
    
    #Function create frame with label on left, and checkbox on the right
    #Returns the frame with label and checkbox, and returns the checkbox
    def _create_frame_with_checkbox(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)
        
        checkbutton = tk.Checkbutton(main_frame, variable=tk.IntVar())
        checkbutton.pack(side="right")
        tk.Label(main_frame, text = label_str).pack(side="left")
        
        return main_frame, checkbutton
    
    def __init__(self, master=None):
        
        self.root = master
#        self.root.title("Field [Abbrevation]")
        tk.Frame.__init__(self, master)
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        
        main_window = tk.Frame(self)
        main_window.pack(side="top")
        
        #Placeholder for options that the dropdown menus will have
        OPTIONS = ["Option 1","Option 2","Option 3"]
        
        #Create many frames what will be added to main_window
        name_frame, self.name_entry = self._create_frame_with_entry(main_window, "Name")
        abv_frame, self.abv_entry = self._create_frame_with_entry(main_window, "Abbreviation")
        desc_frame, self.desc_entry = self._create_frame_with_entry(main_window, "Description")
        ref_frame, self.ref_mb = self._create_frame_with_menu(main_window, "Reference List", OPTIONS)
        data_frame, self.data_mb = self._create_frame_with_menu(main_window, "Data Type", OPTIONS)
        base_frame, self.base_mb = self._create_frame_with_menu(main_window, "Base", OPTIONS)
        mask_frame, self.mask_entry = self._create_frame_with_entry(main_window, "Mask")
        value_frame, self.value_entry = self._create_frame_with_entry(main_window, "Value Constraint")
        req_frame, self.req_cb = self._create_frame_with_checkbox(main_window, "Required")
        
        #Specify location
        name_frame.grid(row = 1, column = 0)
        abv_frame.grid(row = 2, column = 0)
        desc_frame.grid(row = 3, column = 0)
        ref_frame.grid(row = 4, column = 0)
        data_frame.grid(row = 5, column = 0)
        base_frame.grid(row = 6, column = 0)
        mask_frame.grid(row = 7, column = 0)
        value_frame.grid(row = 8, column = 0)
        req_frame.grid(row = 9, column = 0)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Field_window(master=root)
    app.mainloop()