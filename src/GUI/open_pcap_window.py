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

class OpenPcapWindow(tk.Frame):

    # Function create frame with label on left, and entry on the right
    # Returns the frame with label and entry, and returns the entry
    def _create_frame_with_entry(self, parent_frame, label_str):
        main_frame = tk.Frame(parent_frame)

        entry = tk.Entry(main_frame)
        entry.pack(side="right")

        label = tk.Label(main_frame, text=label_str)
        label.pack(side="left")

        return main_frame, entry

    def __init__(self, master=None):
        self.root = master
        master.title("PCAP")
	w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w/2
        h = h/2
        self.root.geometry("400x90+%d+%d" % (w-150, h-100))
        tk.Frame.__init__(self)
        self.pack()
        self._create_widgets()


    # Adds all the widgets.
    def _create_widgets(self):
        # Main window
        main_window = tk.Frame(self.root)
        main_window.pack(side="top")

        # Create Label with text, and add to main_window
        project_label = tk.Label(main_window, text="Open a PCAP file")

        # Create frame with label and entry, and add to main_window
        name_frame, self.name_entry = self._create_frame_with_entry(main_window, "PCAP Name")
        buttons_frame1 = tk.Frame(main_window)
        tk.Button(buttons_frame1, text="Browse", command=self._browse_button).pack(side="right")

        # Create frame and add 2 buttons to it.
        buttons_frame2 = tk.Frame(main_window)
        tk.Button(buttons_frame2, text="Launch", command=self._create_button_clicked).pack(side="left")
        tk.Button(buttons_frame2, text="Cancel", command=self._cancel_button_clicked).pack(side="right")

        # Specify location of widgets on main window
        project_label.grid(row=0, column=0)
        name_frame.grid(row=1, column=0)
        buttons_frame1.grid(row=1, column=1)
        buttons_frame2.grid(row=2, column=1)

    # Function to be called when create button is clicked
    def _create_button_clicked(self):
        print('Launch button clicked')
        Workspace_name = self.name_entry.get()

    def _browse_button(self):
        from tkFileDialog import askopenfilename

        tk.Tk().withdraw()
        self.filename = askopenfilename()
        print(self.filename)


# Function to be called when cancel button is clicked
    def _cancel_button_clicked(self):
        print('Cancel button clicked')
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = OpenPcapWindow(master=root)
    app.mainloop()
