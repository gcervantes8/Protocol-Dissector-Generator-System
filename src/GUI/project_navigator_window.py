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

#TODO: change workspace_label to current workspace
#TODO: Add projects based on working directory

import Tkinter as tk


class ProjectNavigatorWindow(tk.Frame):
    def _create_widgets(self):

        # desc = tk.Label(self.root, text="Workspace X", pady=10)
        # desc.pack()

        frame1 = tk.Frame(self.root)
        frame1.pack(side=tk.LEFT)

        project_button_1 = tk.Button(frame1, command = self.continue_button_clicked, text="Project A", padx=10)
        project_button_2 = tk.Button(frame1, command = self.continue_button_clicked, text="Project B", padx=10)
        project_button_3 = tk.Button(frame1, command = self.continue_button_clicked, text="Project C", padx=10)

        project_button_1.grid(row=0, column=0, padx=10)
        project_button_2.grid(row=1, column=0, padx=10)
        project_button_3.grid(row=2, column=0, padx=10)

    def continue_button_clicked(self):
        #Insert Opening project functionality
        print('Continue button click')


    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Project Navigator")

        # block to control where window opens
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w/2
        h = h/2
        self.root.geometry("150x150+%d+%d" % (w-75, h-200))

        self._create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectNavigatorWindow(parent=root)
    app.mainloop()