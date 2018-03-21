#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas

"""
from Tkinter import *
import Tkinter as tk
from ttk import *

class DissectorScriptWindow(tk.Frame):
    def browse_project(self):
        print('Browsing')
    def dropdown_change(dissector_format,*args):
        print(dissector_format.get())

    def init_window(self,pos):
        root = pos
        root.wm_title('Dissector Script')

        frame = tk.Frame(root)
        frame.pack()
        tk.Label(frame,text='Generate a custom dissector script from a selected project').grid(column=0,row=0)
        #Project Browse
        tk.Label(frame,text='Project').grid(column = 0, row = 1)
        project = tk.Entry(frame)
        project.grid(column = 1 , row =1)
        project.insert(0,"Project Name")
        tk.Button(frame, text="Browse",command = self.browse_project).grid(column = 2, row = 1)

        available_formats = {'LUA'}
        dissector_format = StringVar(frame)
        dissector_format.set('LUA')

        tk.Label(frame,text='Dissector Format').grid(column = 0, row = 2)
        format = tk.OptionMenu(frame,dissector_format,*available_formats)
        format.grid(column = 1 , row =2)
        dissector_format.trace('w',self.dropdown_change(dissector_format))

        tk.Label(frame,text='Save Location').grid(column = 0, row = 3)
        save_location = tk.Entry(frame)
        save_location.grid(column = 1 , row =3)
        save_location.insert(0,"Local File System Path")
        tk.Button(frame, text="Browse",command = self.browse_project).grid(column = 2, row = 3)

        tk.Button(frame,text = 'Generate').grid(column = 2 , row = 4)
        tk.Button(frame,text = 'Cancel').grid(column = 3 , row = 4)

        root.mainloop()



