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
    def dropdown_change(self,*args):
        print(self.dissector_format.get())

    def init_window(self):

        #root.wm_title('Dissector Script')


        tk.Label(self.root,text='Generate a custom dissector script from a selected project').grid(column=0,row=0)
        #Project Browse
        tk.Label(self.root,text='Project').grid(column = 0, row = 1)
        project = tk.Entry(self.root)
        project.grid(column = 1 , row =1)
        project.insert(0,"Project Name")
        tk.Button(self.root, text="Browse",command = self.browse_project).grid(column = 2, row = 1)

        available_formats = {'LUA'}

        self.dissector_format.set('LUA')

        tk.Label(self.root,text='Dissector Format').grid(column = 0, row = 2)
        format = tk.OptionMenu(self.root,self.dissector_format,*available_formats)
        format.grid(column = 1 , row =2)
        self.dissector_format.trace('w',self.dropdown_change())

        tk.Label(self.root,text='Save Location').grid(column = 0, row = 3)
        save_location = tk.Entry(self.root)
        save_location.grid(column = 1 , row =3)
        save_location.insert(0,"Local File System Path")
        tk.Button(self.root, text="Browse",command = self.browse_project).grid(column = 2, row = 3)

        tk.Button(self.root,text = 'Generate').grid(column = 2 , row = 4)
        tk.Button(self.root,text = 'Cancel').grid(column = 3 , row = 4)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.dissector_format = StringVar(self)
        self.init_window()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DissectorScriptWindow(parent=root)
    app.pack()
    app.mainloop()



