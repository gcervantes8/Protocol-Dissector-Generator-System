

try:
    from TTkinter import PhotoImage, Frame, Label, Widget
    from Tkconstants import *
except ImportError:
    from Tkinter import PhotoImage, Frame, Label, Widget
    from Tkinter import *


class CollapsibleFrame(Frame):
    def __init__(self, master, text=None, borderwidth=2, width=0, height=16, interior_padx=0, interior_pady=8,
                 background=None, caption_separation=4, caption_font=None, caption_builder=None, icon_x=5):
        Frame.__init__(self, master)
        master.title("Palette")
        self._is_opened = False

        self._interior_padx = interior_padx
        self._interior_pady = interior_pady

        self._iconOpen = PhotoImage(
            data="R0lGODlhEwATAPcAAAAAAAAAAQD/AAIAAQUAAgcFAAoEAAwHABALABQMBBUPARUSAhUTBhgQBBgVCRsUACEWACIcACYgACggACshACwoADElATEpADEtATQkADQpADYxBDctATk0AT8uAEA6AEE1AEU0AUY3AEY7AUc/Ako7AUpFBUxAA1BHAVE6AFRHAFU/AFdGAFdQAFhCAFlUAVpMAFxGAF1DAF5TAGBaAGNIAGRYAGReAmVSAGhMAGpPAGpWAmpfAm1SAG9RAHFXAHFhAXFrAXJbAXJnAHZuA3dYAHxcAnxfAXxkAHxuAH1gAH5qAX5zAIBcAoRiAIRxAIR5AIdmAIhqAIlyAImAAop6AIxmAI9xAY95AY+BAJJtAJRvAJSIAJV5AZWAAJd1AJl0App5AJtxAZuJAJx/AJyKAZyPAJ+UAKB2AKGAAKKIAaSUAKV7AKeAAaeJAKqeA6uQAKuaAKyVAa+BAK+JALCiALOEALORALSWALSiALWaALeqAbmLALuhALyXALyqALywAL6LAMC0AMGfAMGkAMKRAMOWAMOpAMOvAMO6AMqYAMqiAMqyAMunAMuuAMu+AMy5AM2dAs7DANGfAtG7AdKwANPFANWoANXFANihANi4ANi9ANmyANnEANrLANunAN6mAN/MAOC/AODFAOK5AOLRAOOsAOWxAOasAOfFAefWAOm5AenNAOnTAOu/AOyzBezaAO3YAO60Be7dAPDFAPG1APLQAPO9APPLAPPdAPPjAfS2APTBAPTDAPW/APa/APbAAPbDAPbXAPe/APfIAPfPAPi9APjLAPjjAPm9APnXAPnbAPnkAPrRAPrqAPu8APu/APvBAPvDAPvNAPvUAPvXAPvdAPviAPzHAPzLAPzTAfzWAPzdAPzhAPzkAPzlAPzuAP2+AP3MAP3PAP3VAP3ZAP3iAP3kAP3pAP3sAP3tAP3vAP68AP7FAP7IAP7KAP7RAP7TAf7XAP7aAP7dAP7fAP7jAP7lAP7oAP7qAP7xAP/GAP/pAP/uAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFBwACACwAAAAAEwATAAAIuAABCBxIsKDBgwgFRuBhpqHDLCYSjtiTq6LFVmM0aNyoIUKBEoSaiRzZbBSiPyj/EOrzZEKIQr5+AZsJLNgydThzqktEosShZcusCRV6L5/Ro/kSmTjB6J7Tp1CjIiLB1JzVq1izTj3hiJ7Xr2DDHqLaSJ7Zs2jRljtUokSjeHDjyp1LqO2icXjz6t07yK67v4ADC+5bwlC0w4gTKzYkwsMcU5AjS548xwMCDzkya97M2XLCz6ARBgQAIfkEBQYAAgAsAAACABMAEAAAAg+Uj6nL7Q+jnLTai7PeHBUAIfkEBQcAAgAsAAACABIACgAAAgyUj6nL7Q+jnLTaVgAAIfkEBQcAAgAsAwAFAAUAAgAAAgOUjwUAOw==")
        self._iconClose = PhotoImage(
            data="R0lGODlhEwATAPcAAAAAAAAAAgD/AAEAAAEBAAIAAQUEAAoFAAsJAA4LABMOABUSBRcPAhkUABoYBx4XBB8YACEbASQfASgiACoeAC4jAS4nADEsADMvATQnADUuBTYuADk2ATsxADwtAT84AUI7AEQzAEQ5AEZBAEo5Ako9AUpDAU88AVBGAVBLAVQ9AVRCAFZQAVhGAFhLAVtUAV9CAF9LAWFQAmFZAWFaAGJRAGRLAWVHAGVeAGdiAGtTAmtZBGxZAGxkAG1PAG1iAnFdAHFpAXRUAnRWA3RZAXRiAXZeAHhqAXpiAXpvAXtzAYBcAIFrAYJjAoNgAYN1AoV9AYhrAop0AYtlAI2FAY59AY9jAJB4AJFrApFsApJyAZOFAZRoAZSMAZV+AJmCAJuPAJxmAJxzAJ15AJ2IAJ+CAKGQAaGXAaV6AKV7AKeLAKh8AKiRAKmXAatpAqyhAK2BAK+IAbGEALGYALKEBbOlArV6AbWIALaaAbiLALiUArihArqtAb2NAL+uAMCQA8CZAMGkAMGoAMOAAMO1AcWuAMaTAMa7AMeZAcuYA8uZAMunAMy1AM2YAM29Ac6wAM+bANLFAtSeANSoAdS3AdW+AdaCANahAdfMAdmIANqmAN2wAd3EAN3NAt6oAN7BAOCTAOC4AeHWAeKJAOOsAOSaAOStAOXJAOaMAOeQAOqTAOrQAOuyAOu9AOvKAOvWAOvfAuyWAO2gAO6oAO+bAO+2AO+4APGvAPG8APKfAPLeAPPPAPSiAPSoAPS7APTFAPTXAPW1APW4APXAAPXlAPbKAPemAPerAPfOAPfgAPfqAPjVAPjaAPmwAPm8APm/APnMAPq1APq5APrHAPrgAPvCAPvOAPvXAPvrAfzUAPzgAPzmAPztAPzvAP27AP3AAP3FAP3HAP3KAP3MAP3VAP3ZAP3iAP3kAP3qAP3vAP7FAP7IAP7JAP7MAP7PAP7SAP7TAP7XAP7YAP7cAf7eAP7fAP7jAP7nAP7qAP7sAP7uAP/QAP/TAP/bAP/oAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFBwACACwAAAAAEwATAAAIygABCBxIsKDBgwgHGlCwoGFDBQcSAugQRImSJ0+UBPkgEQosYiBB6jojgkRJkx0aCNyyDZ/Ll6sEBZo5c44MgVWuzdvJsyfPZVUEaoHWrqjRduOSjitaTIpALMGkSZ0aTZgwZ1id+dLC4IATVbFo0cpF1teys2iXVWLxotIuZHDRanv5Mh+xHj+SmdvLt6/fVS9kuPJJuOcjEyUWwVvMuLHjOR0yqFFKubLSMREUZKllq7Pnz55rRTEAgMQULKhTq07tJITE17ANBgQAIfkEBQYAAgAsAAACABMADwAACDUABQgcSLCgwYMIExoUIUKhQ4LMHkok2E7gtILRJmo8iMxhvnz4NoocqbCduJMoU6YkyVJAQAAh+QQFBwABACwBAAMAEgANAAAIHgADCBxIsKDBgwgTKlzIkKGVhhAjSpxIMaK4ihEDAgAh+QQFBwABACwCAAMAEAANAAAIIQADCBxIsKDBgwgTKlzIsOFAYQRzOUyYb6LFiwTbYWwYEAA7")

        height_of_icon = max(self._iconOpen.height(), self._iconClose.height())
        width_of_icon = max(self._iconOpen.width(), self._iconClose.width())

        containerFrame_pady = (height_of_icon // 2) + 1

        self._height = height
        self._width = width

        self._containerFrame = Frame(self, borderwidth=borderwidth, width=width, height=height, relief=RIDGE,
                                     background=background)
        self._containerFrame.pack(expand=True, fill=X, pady=(containerFrame_pady, 0))

        self.interior = Frame(self._containerFrame, background=background)

        self._collapseButton = Label(self, borderwidth=0, image=self._iconOpen, relief=RAISED)
        self._collapseButton.place(in_=self._containerFrame, x=icon_x, y=-(height_of_icon // 2), anchor=N + W,
                                   bordermode="ignore")
        self._collapseButton.bind("<Button-1>", lambda event: self.toggle())

        if caption_builder is None:
            self._captionLabel = Label(self, anchor=W, borderwidth=1, text=text)
            if caption_font is not None:
                self._captionLabel.configure(font=caption_font)
        else:
            self._captionLabel = caption_builder(self)

            if not isinstance(self._captionLabel, Widget):
                raise Exception("'caption_builder' doesn't return a Tkinter widget")

        self.after(0, lambda: self._place_caption(caption_separation, icon_x, width_of_icon))


    def _place_caption(self, caption_separation, icon_x, width_of_icon):
        self.update()
        x = caption_separation + icon_x + width_of_icon
        y = -(self._captionLabel.winfo_reqheight() // 2)

        self._captionLabel.place(in_=self._containerFrame, x=x, y=y, anchor=N + W, bordermode="ignore")


    def open(self):
        self._collapseButton.configure(image=self._iconClose)

        self._containerFrame.configure(height=self.interior.winfo_reqheight())
        self.interior.pack(expand=True, fill=X, padx=self._interior_padx, pady=self._interior_pady)

        self._is_opened = True

    def close(self):
        self.interior.pack_forget()
        self._containerFrame.configure(height=self._height)
        self._collapseButton.configure(image=self._iconOpen)

        self._is_opened = False

    def toggle(self):
        if self._is_opened:
            self.close()
        else:
            self.open()


if __name__ == "__main__":
    try:
        from Tkinter import Tk, Button
    except ImportError:
        from Tkinter import Tk, Button

    root = Tk()
    root.wm_geometry("200x300+0+0")

    cf1 = CollapsibleFrame(root, text="Field", interior_padx=6)
    cf1.pack()
    cf2 = CollapsibleFrame(root, text="Construct", interior_padx=6)
    cf2.pack()

    #whats inside folders place holders
    for i in range(3):
        Button(cf1.interior, text="button %s" % i).pack(side=LEFT)

    cf1._containerFrame.configure(width=250)
    cf2._containerFrame.configure(width=350)
    root.mainloop()