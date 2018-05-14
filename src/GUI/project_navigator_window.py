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
import os
from moving_frame import MovingFrame
import sys
sys.path.insert(0, '../Model')
from ProjectManager import ProjectManager

class ProjectNavigatorWindow(MovingFrame):
    def _create_widgets(self,parent):

        # desc = tk.Label(self.root, text="Workspace X", pady=10)
        # desc.pack()

        frame1 = tk.Frame(parent)
        frame1.pack(side=tk.LEFT)
        a = ProjectManager.current.guiInfo(None, None, None, None, None, 2)

        self.ProjectButtons = []
        for i in range(len(a)):
            self.ProjectButtons.append(tk.Button(frame1, command = self.continue_button_clicked, text=a[i], padx=10))
            self.ProjectButtons[i].grid(row=i+1, column=0, padx=10)

    def continue_button_clicked(self):
        #Insert Opening project functionality
        print('Continue button click')


    def __init__(self, parent):
        self.root = parent
        self.mv = MovingFrame(self.root, "Project Navigator", 0, 100, 150, 200)
        # block to control where window opens
        # w = self.root.winfo_screenwidth()
        # h = self.root.winfo_screenheight()
        # w = w/2
        # h = h/2
        # self.root.geometry("150x150+%d+%d" % (w-75, h-200))

        self._create_widgets(self.mv.f)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectNavigatorWindow(parent=root)
    app.mainloop()
