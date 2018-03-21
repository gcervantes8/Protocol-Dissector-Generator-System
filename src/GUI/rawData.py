# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:31:20 2018
@author: Gerardo Cervantes
"""

import Tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):

        self.root = master
        self.root.title("Dissected Stream Area")
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        # Frame
        main_window = tk.Frame(self)
        main_window.pack(side="top")

        # Create text_frame with label instruction and text widget
        text_frame = tk.Frame(self)
        text_frame.pack(side="left")

        # Main text
        self.text = tk.Text(text_frame)
        self.text.pack(side="bottom")


        # Scroll bar
        self.scrollbar = tk.Scrollbar(self, command=self.text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text.configure(yscrollcommand=self.scrollbar.set)

    # Adds text to the dissected stream window, header and text are both str
    def add_text(self, text):
        self.text.insert("end", text)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.pack(fill="both", expand=True)

    # Add text to dissected stream window
    for i in range(30):
        app.add_text( "0000  00 00 00 00 00 00    00 00 00 00 00 00 ...... ......\n");
    root.mainloop()