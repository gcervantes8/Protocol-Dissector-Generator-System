#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  20  2018

@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

import Tkinter as tk


class OrganizeViews(tk.Frame):
    def __init__(self, parent=None):
        self.root = parent
        root.title("Organize Views")
        tk.Frame.__init__(self)

        # block to control where window opens
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w = w/2
        h = h/2
        root.geometry("450x450+%d+%d" % (w-200, h-200))

        self._create_widgets()

    def _create_widgets(self):
        def sel1():
            selection = var1.get()

        def sel2():
            selection = var2.get()

        def sel3():
            selection = var3.get()

        def sel4():
            selection = var4.get()

        def sel5():
            selection = var5.get()

        def sel6():
            selection = var6.get()

        def sel7():
            selection = var7.get()

        def defaults():
            project_nav_off.select()
            dissector_build_area_off.select()
            palette_off.select()
            packet_stream_area_off.select()
            dissected_stream_area_off.select()
            raw_data_area_off.select()
            console_area_off.select()

        def confirm():
            exit(0)

        def cancel():
            exit(0)

        desc = tk.Label(root, text="Customize the views", pady=10)
        desc.pack()

        frame1 = tk.Frame(root)
        frame1.pack(side = tk.LEFT)

        #label section
        hide_label = tk.Label(frame1, text="Hide")
        show_label = tk.Label(frame1, text="Show")
        project_nav = tk.Label(frame1, text="Project Navigation")
        dissector_build_area = tk.Label(frame1, text="Dissector Building Area")
        palette = tk.Label(frame1, text="Palette")
        packet_stream_area = tk.Label(frame1, text="Packet Stream Area")
        dissected_stream_area = tk.Label(frame1, text="Dissected Stream Area")
        raw_data_area = tk.Label(frame1, text="Raw Data Area")
        console_area = tk.Label(frame1, text="Console Area")

        #for radio buttons - need vars for each button
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        var5 = tk.IntVar()
        var6 = tk.IntVar()
        var7 = tk.IntVar()

        #each radio button saved to unique var, call to unique function on change
        project_nav_off = tk.Radiobutton(frame1, variable=var1, value=0, command=sel1)
        project_nav_on = tk.Radiobutton(frame1, variable=var1, value=1, command=sel1)

        dissector_build_area_off = tk.Radiobutton(frame1, variable=var2, value=0, command=sel2)
        dissected_build_area_on = tk.Radiobutton(frame1, variable=var2, value=1, command=sel2)

        palette_off = tk.Radiobutton(frame1, variable=var3, value=0, command=sel3)
        palette_on = tk.Radiobutton(frame1, variable=var3, value=1, command=sel3)

        packet_stream_area_off = tk.Radiobutton(frame1, variable=var4, value=0, command=sel4)
        packet_stream_area_on = tk.Radiobutton(frame1, variable=var4, value=1, command=sel4)

        dissected_stream_area_off = tk.Radiobutton(frame1, variable=var5, value=0, command=sel5)
        dissected_stream_area_on = tk.Radiobutton(frame1, variable=var5, value=1, command=sel5)

        raw_data_area_off = tk.Radiobutton(frame1, variable=var6, value=0, command=sel6)
        raw_data_area_on = tk.Radiobutton(frame1, variable=var6, value=1, command=sel6)

        console_area_off = tk.Radiobutton(frame1, variable=var7, value=0, command=sel7)
        console_area_on = tk.Radiobutton(frame1, variable=var7, value=1, command=sel7)

        #for buttons
        default_button = tk.Button(frame1, text="Restore to Default", command=defaults)
        confirm_button = tk.Button(frame1, text="Confirm", command=confirm)
        cancel_button = tk.Button(frame1, text="Cancel", command=cancel)

        #pack everything
        # show_label.pack()
        # hide_label.pack()
        # project_nav.pack()
        # dissector_build_area.pack()
        # palette.pack()
        # packet_stream_area.pack()
        # dissected_stream_area.pack()
        # raw_data_area.pack()
        # console_area.pack()
        #
        # project_nav_off.pack()
        # project_nav_on.pack()
        # dissector_build_area_off.pack()
        # dissected_build_area_on.pack()
        # palette_off.pack()
        # palette_on.pack()
        # packet_stream_area_off.pack()
        # packet_stream_area_on.pack()
        # dissected_stream_area_off.pack()
        # dissected_stream_area_on.pack()
        # raw_data_area_off.pack()
        # raw_data_area_on.pack()
        # console_area_off.pack()
        # console_area_on.pack()
        #
        # default_button.pack()
        # confirm_button.pack()
        # cancel_button.pack()

        #grid positioning
        hide_label.grid(row=0, column=1)
        show_label.grid(row=0, column=2)
        project_nav.grid(row=1, column=0, sticky=tk.E, pady=10)
        dissector_build_area.grid(row=2, column=0, sticky=tk.E, pady=10)
        palette.grid(row=3, column=0, sticky=tk.E, pady=10)
        packet_stream_area.grid(row=4, column=0, sticky=tk.E, pady=10)
        dissected_stream_area.grid(row=5, column=0, sticky=tk.E, pady=10)
        raw_data_area.grid(row=6, column=0, sticky=tk.E, pady=10)
        console_area.grid(row=7, column=0, sticky=tk.E, pady=10)

        project_nav_off.grid(row=1, column=1, padx=50)
        project_nav_on.grid(row=1, column=2, padx=50)
        dissector_build_area_off.grid(row=2, column=1)
        dissected_build_area_on.grid(row=2, column=2)
        palette_off.grid(row=3, column=1)
        palette_on.grid(row=3, column=2)
        packet_stream_area_off.grid(row=4, column=1)
        packet_stream_area_on.grid(row=4, column=2)
        dissected_stream_area_off.grid(row=5, column=1)
        dissected_stream_area_on.grid(row=5, column=2)
        raw_data_area_off.grid(row=6, column=1)
        raw_data_area_on.grid(row=6, column=2)
        console_area_off.grid(row=7, column=1)
        console_area_on.grid(row=7, column=2)

        default_button.grid(row=8, column=1, pady=20)
        confirm_button.grid(row=8, column=2)
        cancel_button.grid(row=8, column=3)


if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizeViews(parent=root)
    root.mainloop()