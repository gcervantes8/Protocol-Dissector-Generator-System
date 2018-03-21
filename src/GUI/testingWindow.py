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
from Tkinter import *
import Tkinter as tk

from menu import MenuWindow
from dissector_script_window import DissectorScriptWindow
from packet_information_field_window import PacketInformationFieldWindow
from packet_stream_area_view_window import PacketStreamAreaWindow

from Tkinter import *
import Tkinter as tk
from ttk import *

menu = MenuWindow()
ds = DissectorScriptWindow()
psa = PacketStreamAreaWindow()
pif = PacketInformationFieldWindow()


# ds.init_window()
# psa.init_window()

root = tk.Tk()
root.wm_title('PDGS')

#menu.init_window(root)
frame = psa.init_window(root)

menu.init_window(root)











