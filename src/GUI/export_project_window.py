#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  20  2018

@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

from Tkinter import *
import tkFileDialog
import os


class ExportProject():
    def __init__(self, master=None):
        self.root = master
        root.title("Export Project")

        # block to control where window opens
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w = w/2
        h = h/2
        root.geometry("400x150+%d+%d" % (w-150, h-100))

        self._create_widgets()

    def _create_widgets(self):

        def change_project():
            projectname = tkFileDialog.askopenfilename()
            project_entry.delete(0, END)
            project_entry.insert(0, projectname)

        def change_path():
            dirname = tkFileDialog.askdirectory(parent=root, initialdir=os.getcwd())
            export_entry.delete(0, END)
            export_entry.insert(0, dirname)

        def export_project():
            exit(0)

        def cancel():
            exit(0)

        desc = Label(root, text = "Export project to the local file system.", pady=10)
        desc.pack()

        frame1 = Frame(root)
        frame1.pack(side = LEFT)

        project_label = Label(frame1, text="Project")
        project_entry = Entry(frame1, width=40)
        export_label = Label(frame1, text="To export file", pady=10)
        export_entry = Entry(frame1, width=40)
        project_browse_button = Button(frame1, command=change_project, text="Browse", padx=10)
        export_browse_button = Button(frame1, command=change_path, text="Browse", padx=10)
        export_button = Button(frame1, command=export_project, text="Export", padx=10)
        cancel_button = Button(frame1, command=cancel, text="Cancel", padx=10)

        project_label.pack()
        project_entry.pack()
        export_label.pack()
        export_entry.pack()
        project_browse_button.pack()
        export_browse_button.pack()
        export_button.pack()
        cancel_button.pack()

        project_label.grid(row=0, column=0, sticky=E)
        project_entry.grid(row=0, column=1)
        export_label.grid(row=1, column=0)
        export_entry.grid(row=1, column=1)
        project_browse_button.grid(row=0, column=2, padx=10)
        export_browse_button.grid(row=1, column=2, padx=10)
        export_button.grid(row=2, column=1, sticky=E)
        cancel_button.grid(row=2, column=2)

if __name__ == "__main__":
    root = Tk()
    app = ExportProject(master=root)
    root.mainloop()