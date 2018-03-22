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
from ttk import *

root = Tk()
root.wm_title('Protocol-Dissector Generator System')


menu = MenuWindow(root)
menu.pack()
psa = PacketStreamAreaWindow(root)
psa.pack()
pif = PacketInformationFieldWindow(root)
pif.pack()


root.mainloop()

