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

def buttonClick(event=None):
    print("Button clicked")

root = tk.Tk()

create_btn = tk.Button(root, text='Create Project',command=buttonClick).grid(column=0, row=0)
save_btn = tk.Button(root, text='Save Project',command=buttonClick).grid(column=1, row=0)
close_btn = tk.Button(root, text='Close Project',command=buttonClick).grid(column=2, row=0)
switch_ws_btn = tk.Button(root, text='Switch Workspace',command=buttonClick).grid(column=3, row=0)
import_btn = tk.Button(root, text='Import Project',command=buttonClick).grid(column=4, row=0)
export_btn = tk.Button(root, text='Export Project',command=buttonClick).grid(column=5, row=0)
gen_dis_script_btn = tk.Button(root, text='Generate Dissector Script',command=buttonClick).grid(column=6, row=0)
org_views_btn = tk.Button(root, text='Organize Views',command=buttonClick).grid(column=7, row=0)
open_pcap_btn = tk.Button(root, text='Open PCAP',command=buttonClick).grid(column=8, row=0)

root.mainloop()



