#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas

"""
from Tkinter import *
import Tkinter as tk

class MenuWindow(tk.Frame):
    def buttonClick(event=None):
        print("Button clicked")

    def init_window(self,pos):
        root = pos
        create_btn = tk.Button(root, text='Create Project',command=self.buttonClick)
        create_btn.grid(column=0, row=0)
        save_btn = tk.Button(root, text='Save Project',command=self.buttonClick)
        save_btn.grid(column=1, row=0)
        close_btn = tk.Button(root, text='Close Project',command=self.buttonClick)
        close_btn.grid(column=2, row=0)
        switch_ws_btn = tk.Button(root, text='Switch Workspace',command=self.buttonClick)
        switch_ws_btn.grid(column=3, row=0)
        import_btn = tk.Button(root, text='Import Project',command=self.buttonClick)
        import_btn.grid(column=4, row=0)
        export_btn = tk.Button(root, text='Export Project',command=self.buttonClick)
        export_btn.grid(column=5, row=0)
        gen_dis_script_btn = tk.Button(root, text='Generate Dissector Script',command=self.buttonClick)
        gen_dis_script_btn.grid(column=6, row=0)
        org_views_btn = tk.Button(root, text='Organize Views',command=self.buttonClick)
        org_views_btn.grid(column=7, row=0)
        open_pcap_btn = tk.Button(root, text='Open PCAP',command=self.buttonClick)
        open_pcap_btn.grid(column=8, row=0)

        root.mainloop()


