# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:29:57 2018

@author: Gerardo Cervantes
"""

import tkinter as tk


class Application(tk.Frame):
    
    #Function create frame with label on left, and entry on the right
    #Returns the frame with label and entry, and returns the entry
    def create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)
        
        entry = tk.Entry(main_frame)
        entry.pack(side="right")
        
        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")
        
        return main_frame, entry
    
    def __init__(self, master=None):
        
        self.root = master
        self.root.title("New Project")
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        main_window = tk.Frame(self)
        main_window.pack(side="top")
        
        
        name_frame, self.name_entry = self.create_frame_with_entry(main_window, "Project")
        desc_frame, self.desc_entry = self.create_frame_with_entry(main_window, "Description")
        
        buttons_frame = tk.Frame(main_window)
        project_label = tk.Label(main_window, text= "Create a new project")
        
        project_label.grid(row = 0, column = 0)
        name_frame.grid(row = 1, column = 0)
        desc_frame.grid(row = 2, column = 0)
        buttons_frame.grid(row = 3, column = 0)
    
        create_button = tk.Button(buttons_frame, text = "Create", command = self.create_button_clicked)
        cancel_button = tk.Button(buttons_frame, text = "Cancel", command = self.cancel_button_clicked)
        
        create_button.pack(side="left")
        cancel_button.pack(side="right")
        
    def create_button_clicked(self):
        
        print('Create button click')
        project_name = self.name_entry.get()
        project_desc = self.desc_entry.get()
        
        print("Project name: " + project_name)
        print("Project description: " + project_desc)
        
    def cancel_button_clicked(self):
        
        print('Cancel button click')
        self.root.destroy()

root = tk.Tk()
app = Application(master=root)
app.mainloop()