#! python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:29:57 2018
@author: Gerardo Cervantes
         Oliver Martinez
         Isaac Hoffman
         Daniel Ornelas
         Christopher Soto
"""

import Tkinter as tk
import sys
sys.path.insert(0, '../Model/')
from Dissector import Dissector
from parse_pdml_xml import parse_pdml_xml

class DissectorSelector(tk.Frame):

    # Function create frame with label on left, and entry on the right
    # Returns the frame with label and entry, and returns the entry
    def _create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)

        entry = tk.Entry(main_frame)
        entry.pack(side="right")

        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")

        return main_frame, entry

    def __init__(self, master):
        self.root = master
        master.title("Dissector Selector")
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()

    def set_main_window(self, main_window):
        self.main_window = main_window
    # Adds all the widgets.
    def _create_widgets(self):
        # Main window
        main_window = tk.Frame(self.root)
        main_window.pack(side="top")

        # Create Label with text, and add to main_window
        project_label = tk.Label(main_window, text="Select Dissector")

        # Create frame with label and entry, and add to main_window
        name_frame, self.name_entry = self._create_frame_with_entry(main_window, "Dissector Name")
        buttons_frame1 = tk.Frame(main_window)
        tk.Button(buttons_frame1, text="Browse", command=self._browse_button).pack(side="right")

        # Create frame and add 2 buttons to it.
        buttons_frame2 = tk.Frame(main_window)
        tk.Button(buttons_frame2, text="Select", command=self._select_button_clicked).pack(side="left")


        # Specify location of widgets on main window
        project_label.grid(row=0, column=0)
        name_frame.grid(row=1, column=0)
        buttons_frame1.grid(row=1, column=1)
        buttons_frame2.grid(row=2, column=1)

    # Function to be called when create button is clicked
    def _select_button_clicked(self):
        dis = Dissector()
        pdml_xml = dis.dissect_packets()
        print(pdml_xml)
        
        field_name_items, field_items_values, headers, dissected_values = parse_pdml_xml(pdml_xml)
        
        packet_stream = self.main_window.psa
        
#        packet_stream.pcap = 
        packet_stream.add_headers(field_name_items)
        packet_stream._display_packets(field_items_values, packet_stream)
        #populate stream window
        stream_window = self.main_window.stream_window
        for i, header in enumerate(headers):
            stream_window.add_text(header, dissected_values[i])
            
        print('headers')
        print(headers)
        self.root.destroy()


    def _browse_button(self):
        from tkFileDialog import askopenfilename

        tk.Tk().withdraw()
        self.filename = askopenfilename()
        print(self.filename)




if __name__ == "__main__":
    root = tk.Tk()
    app = DissectorSelector(master=root)
    app.mainloop()
