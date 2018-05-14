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
from packet_stream_area_view_window import PacketStreamAreaWindow
import Tkinter as tk
from workspace_save_window import Workspace_save_window
from project_navigator_window import ProjectNavigatorWindow
from dissected_stream_window import Dissected_stream_window
from raw_data_window import Raw_data_window
from console_error_view import ConsoleErrorView
from dissector_builder_area import Dissector_builder_area
from export_project_window import ExportProject

class MainWindow(tk.Frame):

    def init_window(self):
        self.root.deiconify()
        self.menu = MenuWindow(self.root, self)
        self.menu.pack()
        #Need to be moving frames
        self.dba = Dissector_builder_area(self.root)
        self.dba.pack()
        self.psa = PacketStreamAreaWindow(self.root)
        self.psa.pack()
        #READY
        ProjectNavigatorWindow(self.root)
        Dissected_stream_window(self.root)
        Raw_data_window(self.root)
        ConsoleErrorView(self.root)
#        export_project = ExportProject()
#        export_project.set_main_window(self)


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
