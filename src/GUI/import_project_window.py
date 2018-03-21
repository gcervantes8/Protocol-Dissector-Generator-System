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
from tkFileDialog import askopenfilename

class Import_Project(tk.Frame):

    # Function create frame with label on left, and entry on the right
    # Returns the frame with label and entry, and returns the entry
    def _create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)

        entry = tk.Entry(main_frame)
        entry.pack(side="right")

        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")

        return main_frame, entry

    def __init__(self, master=None):
        self.root = master
        master.title("Import Project")
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()

    # Adds all the widgets.
    def _create_widgets(self):
        # Main window
        main_window = tk.Frame(self)
        main_window.pack(side="top")

        # Create Label with text, and add to main_window
        project_label = tk.Label(main_window, text="Import a project into the current workspace")

        # Create frame with label, entry, and button to add to main_window
        name_frame, self.name_entry = self._create_frame_with_entry(main_window, "Import project")
        buttons_frame1 = tk.Frame(main_window)
        tk.Button(buttons_frame1, text="Browse", command=self._browse_button).pack(side="right")

        # Create frame and add 2 buttons to it.
        buttons_frame2 = tk.Frame(main_window)
        tk.Button(buttons_frame2, text="Import", command=self._import_button_clicked).pack(side="left")
        tk.Button(buttons_frame2, text="Cancel", command=self._cancel_button_clicked).pack(side="right")

        # Specify location of widgets on main window
        project_label.grid(row=0, column=0)
        name_frame.grid(row=1, column=0)
        buttons_frame1.grid(row=1, column=1)
        buttons_frame2.grid(row=3, column=0)

    # Function to be called when import button is clicked
    def _import_button_clicked(self):
        print('Import button clicked')
        project_path = self.name_entry.get()

    # Function to be called when browse button is clicked
    def _browse_button(self):
        tk.Tk().withdraw()
        self.filename = askopenfilename()
        print(self.filename)

    # Function to be called when cancel button is clicked
    def _cancel_button_clicked(self):
        print('Cancel button clicked')
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Import_Project(master=root)
    app.mainloop()