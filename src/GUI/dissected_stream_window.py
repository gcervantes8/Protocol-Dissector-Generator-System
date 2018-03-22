# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:31:20 2018

@author: Gerardo Cervantes
"""

import Tkinter as tk


class Dissected_stream_window(tk.Frame):
    
    def __init__(self, master=None):
        
        self.root = master
        self.root.title("Dissected Stream Area")
        tk.Frame.__init__(self)
        self._create_widgets()
        
    def _create_widgets(self):
        #Frame
        main_window = tk.Frame(self.root)
        main_window.pack(side="top")
        
        #Create text_frame with label instruction and text widget
        text_frame = tk.Frame(self.root)
        text_frame.pack(side = "left")
        
        #Create label with instruction to double click header
        label = tk.Label(text_frame,  text= "Double click header to expand or collapse.")
        label.pack(side = "top")
        
        #Main text
        self.text = tk.Text(text_frame)
        self.text.pack(side="bottom")
        self.add_text("HEADER" ,"DISSECTED STREAM")
        
        #Main text configuration
        self.text.tag_configure("hidden", elide = True) #Hide text
        self.text.tag_configure("header", background = "gray", foreground = "white") #Header look
        self.text.tag_bind("header", "<Double-1>", self._toggle_visibility)
        
        #Scroll bar
        # self.scrollbar = tk.Scrollbar(self, command = self.text.yview)
        # self.scrollbar.pack(side="right", fill="y")
        # self.text.configure(yscrollcommand = self.scrollbar.set)

    #Adds text to the dissected stream window, header and text are both str
    def add_text(self, header, text):
        self.text.insert("end", header, "header")
        self.text.insert("end", text)
        
    #Toggles visibility
    def _toggle_visibility(self, event):
        block_start, block_end = self._get_block("insert")
        next_hidden = self.text.tag_nextrange("hidden", block_start, block_end)
        if next_hidden:
            self.text.tag_remove("hidden", block_start, block_end)
        else:
            self.text.tag_add("hidden", block_start, block_end)


    def _get_block(self, index):
        start = self.text.index("%s lineend+1c" % index)
        #Get index of next header
        next_header = self.text.tag_nextrange("header", start)
        
        #False if is last header
        if next_header:
            end = next_header[0]
        else:
            end = self.text.index("end-1c")
            
        return start, end

if __name__ == "__main__":
    root = tk.Tk()
    app = Dissected_stream_window(root)
    app.pack(fill = "both", expand = True)
    
    #Add text to dissected stream window
    for i in range(10):
            app.add_text("Header %s\n" % i, "Protocol info placeholder\nMore protocol info placeholder\n\n");
    root.mainloop()