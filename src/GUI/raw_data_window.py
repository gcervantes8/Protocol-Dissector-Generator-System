# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:31:20 2018
@author: Gerardo Cervantes
"""

import Tkinter as tk
from moving_frame import MovingFrame

class Raw_data_window(MovingFrame):

    def __init__(self, parent):
        self.root = parent
        self.mv = MovingFrame(self.root,"Raw Data View",500,450,300,200)
        self._create_widgets(self.mv.f)

    def _create_widgets(self,parent):
        # Frame
        main_window = tk.Frame(parent)
        main_window.pack()

        # Create text_frame with label instruction and text widget
        text_frame = tk.Frame(main_window)
        text_frame.pack()

        # Main text
        self.text = tk.Text(text_frame)
        self.text.pack()
        self.add_text("RAW DATA")

        # Scroll bar
        # self.scrollbar = tk.Scrollbar(main_window, command=self.text.yview)
        # self.scrollbar.pack(side="right", fill="y")
        # self.text.configure(yscrollcommand=self.scrollbar.set)

    # Adds text to the dissected stream window, header and text are both str
    def add_text(self, text):
        self.text.insert("end", text)


if __name__ == "__main__":
    root = tk.Tk()
    Raw_data_window(root)
    root.mainloop()
