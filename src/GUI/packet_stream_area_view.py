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
def _display_packets(PCAP):
    col = 0
    row = 1
    for packet in PCAP:
        for val in packet:
            tk.Label(root, text=val).grid(column=col, row=row)
            col += 1
        row += 1
        col = 0



pcap = [['1','11.2','192.1.1','192.1.2','HTTP',"HELLO"], ['2','11.4','192.1.1','192.1.2','TCP',"WORLD"]]
root = tk.Tk()
root.wm_title('Packet Stream Area View')
tk.Label(root,text='No .').grid(column=0,row=0)
tk.Label(root,text='Time').grid(column=1, row=0)
tk.Label(root,text='Source').grid(column=2, row=0)
tk.Label(root,text='Destination').grid(column=3, row=0)
tk.Label(root,text='Protocol').grid(column=4, row=0)
tk.Label(root,text='Info').grid(column=5, row=0)
_display_packets(pcap)
root.mainloop()



