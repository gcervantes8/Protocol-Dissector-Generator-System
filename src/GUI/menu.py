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

import Tkinter as tk
from Tkinter import Toplevel
from create_project_window import CreateProjectWindow
from export_project_window import ExportProject
from import_project_window import ImportProject
from dissector_script_window import DissectorScriptWindow
from dissector_selector_popup import DissectorSelector


from organize_views import OrganizeViews
from open_pcap_window import OpenPcapWindow


class MenuWindow(tk.Frame):
    def set_main_window(self, root):
        self.root = root

    def buttonClick(self):
        print("Button clicked")

    def create_click(self):
        if self.root != None:
            popup = tk.Toplevel(self.root)
            create_proj = CreateProjectWindow(popup)

        else:
            print("No root set in menu.py")

    def save_click(self):
        if self.root != None:
            popup = tk.Toplevel(self.root)
            save_proj = CreateProjectWindow(popup)

        else:
            print("No root set in menu.py")

    def export_click(self):
        if self.root != None:
            popup = tk.Toplevel(self.root)
            export_proj = ExportProject(popup)
            export_proj.set_main_window(self.main_window)
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

    def organize_views_click(self):
        if self.root != None:

            popup = tk.Toplevel(self.root)
            org_views = OrganizeViews(popup)

        else:
            print("No root set in menu.py")
    def switch_ws_click(self):
        if self.root != None:
           print("SWITCH")

        else:
            print("No root set in menu.py")

    def pcap_click(self):
        if self.root != None:
            popup = tk.Toplevel(self.root)
            open_pcap = OpenPcapWindow(popup)

        else:
            print("No root set in menu.py")
    def dissect_click(self):
        popup = tk.Toplevel(self.root)
        popup = DissectorSelector(popup)
        popup.set_main_window(self.main_window)
    def init_window(self):

        create_btn = tk.Button(self, text='Create Project', command=self.create_click)
        create_btn.grid(column=0, row=0)
        save_btn = tk.Button(self, text='Save Project', command=self.buttonClick)
        save_btn.grid(column=1, row=0)
        close_btn = tk.Button(self, text='Close Project', command=self.buttonClick)
        close_btn.grid(column=2, row=0)
        switch_ws_btn = tk.Button(self, text='Switch Workspace', command=self.switch_ws_click)
        switch_ws_btn.grid(column=3, row=0)
        import_btn = tk.Button(self, text='Import Project', command=self.import_click)
        import_btn.grid(column=4, row=0)
        export_btn = tk.Button(self, text='Export Project', command=self.export_click)
        export_btn.grid(column=5, row=0)
        gen_dis_script_btn = tk.Button(self, text='Generate Dissector Script',
                                       command=self.dissector_script_click)
        gen_dis_script_btn.grid(column=6, row=0)
        org_views_btn = tk.Button(self, text='Organize Views', command=self.organize_views_click)
        org_views_btn.grid(column=7, row=0)
        open_pcap_btn = tk.Button(self, text='Open PCAP', command=self.pcap_click)
        open_pcap_btn.grid(column=8, row=0)
        dissect_btn = tk.Button(self,text = 'Apply Dissector',command=self.dissect_click)
        dissect_btn.grid(column=9,row=0)

    def __init__(self, parent, main_window):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.init_window()
        self.main_window = main_window
