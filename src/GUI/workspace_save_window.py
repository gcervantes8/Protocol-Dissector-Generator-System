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
import os
from tkFileDialog import askdirectory
import sys
sys.path.insert(0, '../Model')
from src.Model.ProjectManager import ProjectManager

class Workspace_save_window(tk.Frame):

    # Function create frame with label on left, and entry on the right
    # Returns the frame with label and entry, and returns the entry
    def _create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)

        entry = tk.Entry(main_frame)
        entry.pack(side="right")

        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")

        return main_frame, entry

    def __init__(self,main_win, parent):
        tk.Frame.__init__(self)
        self.main_win = main_win
        self.root = parent
        self.root.title("Workspace Launcher")
        self._create_widgets()


    # Adds all the widgets.
    def _create_widgets(self):
        self.folder_path = ''
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(3, weight=1)

        # Create Widgets
        self.label_title = tk.Label(self.root,
                                     text="Select a directory as workspace: PDGS uses the workspace\ndirectory to store projects.")
        self.contentframe = tk.Frame(self.root, relief="sunken")

        self.path_entry = tk.Entry(self.contentframe)
        self.browse_btn = tk.Button(self.contentframe, text="Browse", command=self._browse_button)

        self.btn_do = tk.Button(self.root, text='Launch', command=self._create_button_clicked)
        self.btn_cancel = tk.Button(self.root, text='Cancel',command=self._cancel_button_clicked)

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.contentframe.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.path_entry.grid(row=0, column=0, sticky='ew')
        self.contentframe.columnconfigure(0, weight=1)
        self.browse_btn.grid(row=0, column=1, sticky='e')

        self.btn_do.grid(row=2, column=0, sticky='e')
        self.btn_cancel.grid(row=2, column=1, sticky='e')

        # Padding
        for child in self.root.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    # Function to be called when create button is clicked
    def _create_button_clicked(self):
        print('Launch button clicked')
        manager1 = ProjectManager()
        manager1.guiInfo(os.path.dirname(self.filename),self.filename,None,None,None,None)
        manager1.guiInfo(None,None,None,None,None,2)
        ProjectManager.current = manager1
        self.main_win.init_window()
        self.root.destroy()

    def _browse_button(self):

        self.filename = askdirectory()
        print(self.filename)
        self.path_entry.insert(0,self.filename)



                # Function to be called when cancel button is clicked
    def _cancel_button_clicked(self):
        print('Cancel button clicked')
        self.root.destroy()

