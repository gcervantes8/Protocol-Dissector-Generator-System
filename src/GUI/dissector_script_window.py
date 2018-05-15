#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas
	    Christopher Soto

"""
from Tkinter import *
import Tkinter as tk
from ttk import *
from tkFileDialog import *

class DissectorScriptWindow(tk.Frame):
    def _create_widgets(self):

        self.proj_label = tk.Label(self.root,text='Project')
	self.proj_label.grid(column = 0, row = 1)
        self.project = tk.Entry(self.root)
        self.project.grid(column = 1 , row =1)
        self.browse_project = tk.Button(self.root, command=self.browse_project, text="Browse")
        self.browse_project.grid(column = 2, row = 1)

        available_formats = {'LUA'}

        self.dissector_format.set('LUA')

        tk.Label(self.root,text='Dissector Format').grid(column = 0, row = 2)
        format = tk.OptionMenu(self.root,self.dissector_format,*available_formats)
        format.grid(column = 1 , row =2)
        self.dissector_format.trace('w',self.dropdown_change())

        tk.Label(self.root,text='Save Location').grid(column = 0, row = 3)
        self.save_location = tk.Entry(self.root)
        self.save_location.grid(column = 1 , row =3)
        self.browse_save_location = tk.Button(self.root, command=self.browse_location, text="Browse")
        self.browse_save_location.grid(column = 2, row = 3)

        self.generate_button = tk.Button(self.root,text = 'Generate', command=self.generate_click)
        self.generate_button.grid(column = 2 , row = 4)
        self.cancel_button = tk.Button(self.root, command=self.click_cancel, text = 'Cancel')
        self.cancel_button.grid(column = 3 , row = 4)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
	self.root.title("Generate Protocol")
        self.dissector_format = StringVar(self)
	w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w/2
        h = h/2
        self.root.geometry("430x120+%d+%d" % (w-150, h-100))
        self._create_widgets()
    
    def browse_project(self):
        self.projectname = askopenfilename(defaultextension=".xml", filetypes=(("XML file", "*.xml"),("All Files", "*.*")))
	self.project.insert(0,self.projectname)

    def browse_location(self):
        self.filename = askdirectory()
        print(self.filename)
        self.save_location.insert(0,self.filename)

    def dropdown_change(self,*args):
        print(self.dissector_format.get())
 
    def generate_click(self):
        print('Generate Script Clicked')
    
    def click_cancel(self):
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DissectorScriptWindow(parent=root)
    app.mainloop()



