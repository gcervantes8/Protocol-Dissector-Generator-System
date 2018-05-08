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
from src.Model.ProjectManager import ProjectManager


class CreateProjectWindow(tk.Frame):
    
    #Function create frame with label on left, and entry on the right
    #Returns the frame with label and entry, and returns the entry
    def _create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)
        
        entry = tk.Entry(main_frame)
        entry.pack(side="right")
        
        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")
        
        return main_frame, entry
    
    #Adds all the widgets.
    def _create_widgets(self):
        
        #Main window
        main_window = tk.Frame(self.root)
        main_window.pack(side="top")
        
        #Create Label with text, and add to main_window
        project_label = tk.Label(main_window, text= "Create a new project")
        
        #Create frame with label and entry, and add to main_window
        name_frame, self.name_entry = self._create_frame_with_entry(main_window, "Project")
        desc_frame, self.desc_entry = self._create_frame_with_entry(main_window, "Description")
        
        #Create frame and add 2 buttons to it.
        buttons_frame = tk.Frame(main_window)
        tk.Button(buttons_frame, text = "Create", command = self._create_button_clicked).pack(side="left")
        tk.Button(buttons_frame, text = "Cancel", command = self._cancel_button_clicked).pack(side="right")
        
        
        #Specify location of widgets on main window
        project_label.grid(row = 0, column = 0)
        name_frame.grid(row = 1, column = 0)
        desc_frame.grid(row = 2, column = 0)
        buttons_frame.grid(row = 3, column = 0)
    
    
    #Function to be called when create button is clicked
    def _create_button_clicked(self):
        
        print('Create button clicked')
        project_name = self.name_entry.get()
        project_desc = self.desc_entry.get()
        ProjectManager.current.guiInfo(None,None,project_name,project_desc,None,None)
        
        print("Project name: " + project_name + "\n Project description: " + project_desc)
        self.root.destroy()
         
    #Function to be called when cancel button is clicked
    def _cancel_button_clicked(self):
        
        print('Cancel button clicked')
        self.root.destroy()

    def __init__(self, master):
        tk.Frame.__init__(self)
        self.root = master
        self.root.title("New Project")
        self._create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    app = CreateProjectWindow(master=root)
    app.pack()
    app.mainloop()
