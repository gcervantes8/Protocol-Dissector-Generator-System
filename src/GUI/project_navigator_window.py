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


        self.frame1 = tk.Frame(parent)
        self.frame1.pack(side=tk.LEFT)
        a = ProjectManager.current.guiInfo(None, None, None, None, None, 2)

        self.button_amount = 0
        self.ProjectButtons = []
        for i in range(len(a)):
            self.add_button(a[i])

    def add_button(self, button_name):
        button = tk.Button(self.frame1, command = self.continue_button_clicked, text = button_name, padx = 10)
        self.ProjectButtons.append(button)
        self.ProjectButtons[self.button_amount].grid(row=self.button_amount+1, column=0, padx=10)
        self.button_amount += 1
        return button
    def continue_button_clicked(self):
        #Insert Opening project functionality
        print('Continue button click')


    def __init__(self, parent):
        self.root = parent
        self.mv = MovingFrame(self.root, "Project Navigator", 0, 100, 150, 200)

        self._create_widgets(self.mv.f)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectNavigatorWindow(parent=root)
    app.mainloop()
