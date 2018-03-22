#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas

"""

import Tkinter as tk
class PacketStreamAreaWindow(tk.Frame):
    pcap = [['1', '11.2', '192.1.1', '192.1.2', 'HTTP', "HELLO"], ['2', '11.4', '192.1.1', '192.1.2', 'TCP', "WORLD"]]
    def _display_packets(self, PCAP,position):
        col = 0
        row = 1
        for packet in PCAP:
            for val in packet:
                tk.Label(position, text=val).grid(column=col, row=row)
                col += 1
            row += 1
            col = 0

    def init_window(self):
       # self.wm_title('Packet Stream Area View')
        tk.Label(self,text='No .').grid(column=0,row=0)
        tk.Label(self,text='Time').grid(column=1, row=0)
        tk.Label(self,text='Source').grid(column=2, row=0)
        tk.Label(self,text='Destination').grid(column=3, row=0)
        tk.Label(self,text='Protocol').grid(column=4, row=0)
        tk.Label(self,text='Info').grid(column=5, row=0)
        self._display_packets(self.pcap,self)

    def hide_window(self):
        self.pack_forget()

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.root = parent
        self.init_window()

        
if __name__ == "__main__":
    root = tk.Tk()
    app = PacketStreamAreaWindow(root)
    app.pack()
    app.mainloop()
