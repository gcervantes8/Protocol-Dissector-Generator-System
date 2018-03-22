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

from menu import MenuWindow
from packet_information_field_window import PacketInformationFieldWindow
from packet_stream_area_view_window import PacketStreamAreaWindow
from Tkinter import *
import Tkinter as tk
from workspace_save_window import Workspace_save_window
from ttk import *

class MainWindow(tk.Frame):

    def init_window(self):
        self.root.deiconify()
        menu = MenuWindow(root)
        menu.pack()
        psa = PacketStreamAreaWindow(root)
        psa.pack()
        pif = PacketInformationFieldWindow(root)
        pif.pack()
    def init_launcher(self):
        self.launcher = tk.Toplevel(self.root)
        Workspace_save_window(self,self.launcher)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.title('Protocol-Dissector Generator System')
        self.init_launcher()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = MainWindow(root)
    root.mainloop()
