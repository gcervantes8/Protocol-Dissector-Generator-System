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
import tkFileDialog
import os


class ImportProject(tk.Frame):
    def _create_widgets(self):

        def change_project():
            projectname = tkFileDialog.askopenfilename(defaultextension=".xml",
                                                       filetypes=(("XML file", "*.xml"),
                                                                  ("All Files", "*.*")))
            project_entry.delete(0, tk.END)
            project_entry.insert(0, projectname)

        def export_project():
            self.root.destroy()

        def cancel():
            self.root.destroy()

        desc = tk.Label(self.root, text="Import a project into the current workspace.", pady=10)
        desc.pack()

        frame1 = tk.Frame(self.root)
        frame1.pack(side=tk.LEFT)

        project_label = tk.Label(frame1, text="Import Project")
        project_entry = tk.Entry(frame1, width=40)
        project_browse_button = tk.Button(frame1, command=change_project, text="Browse", padx=10)
        import_button = tk.Button(frame1, command=export_project, text="Import", padx=10)
        cancel_button = tk.Button(frame1, command=cancel, text="Cancel", padx=10)

        project_label.grid(row=0, column=0, sticky=tk.E)
        project_entry.grid(row=0, column=1)
        project_browse_button.grid(row=0, column=2, padx=10)
        import_button.grid(row=2, column=1, sticky=tk.E)
        cancel_button.grid(row=2, column=2, pady=10)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Import Project")

        # block to control where window opens
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w/2
        h = h/2
        self.root.geometry("410x110+%d+%d" % (w-150, h-100))

        self._create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImportProject(parent=root)
    app.mainloop()
