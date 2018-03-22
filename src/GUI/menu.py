#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018
@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""
from Tkinter  import *
import Tkinter as tk
from export_project_window import ExportProject
from import_project_window import ImportProject
from dissector_script_window import DissectorScriptWindow

class MenuWindow(tk.Frame):
    
    def set_main_window(self, root):
        self.root = root

    def buttonClick(self):
        print("Button clicked")

    def export_click(self):
        if self.root != None:
            popup = tk.Toplevel(self.root)
            export_proj = ExportProject(popup)
        else:
            print("No root set in menu.py")

    def import_click(self):
        if self.root != None:

            popup = tk.Toplevel(self.root)
            import_proj = ImportProject(popup)

        else:
            print("No root set in menu.py")

    def dissector_script_click(self):
        if self.root != None:

            popup = tk.Toplevel(self.root)
            dissector_script = DissectorScriptWindow(popup)

        else:
            print("No root set in menu.py")
            
    def init_window(self):

        create_btn = tk.Button(self, text='Create Project', command=self.buttonClick)
        create_btn.grid(column=0, row=0)
        save_btn = tk.Button(self, text='Save Project', command=self.buttonClick)
        save_btn.grid(column=1, row=0)
        close_btn = tk.Button(self, text='Close Project', command=self.buttonClick)
        close_btn.grid(column=2, row=0)
        switch_ws_btn = tk.Button(self, text='Switch Workspace', command=self.buttonClick)
        switch_ws_btn.grid(column=3, row=0)
        import_btn = tk.Button(self, text='Import Project', command=self.import_click)
        import_btn.grid(column=4, row=0)
        export_btn = tk.Button(self, text='Export Project', command=self.export_click)
        export_btn.grid(column=5, row=0)
        gen_dis_script_btn = tk.Button(self, text='Generate Dissector Script',
                                       command=self.dissector_script_click)
        gen_dis_script_btn.grid(column=6, row=0)
        org_views_btn = tk.Button(self, text='Organize Views', command=self.buttonClick)
        org_views_btn.grid(column=7, row=0)
        open_pcap_btn = tk.Button(self, text='Open PCAP', command=self.buttonClick)
        open_pcap_btn.grid(column=8, row=0)

    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.init_window()
