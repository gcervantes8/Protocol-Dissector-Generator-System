from Tkinter import *

def clamp(lo, hi, x):
    return min(max(x, lo), hi)

class MovingFrame:
    all = []
    def MoveWindowStart(self, event):
        self.move_lastx = event.x_root
        self.move_lasty = event.y_root
        self.focus()
    def MoveWindow(self, event):
        self.root.update_idletasks()

        dx = event.x_root - self.move_lastx
        dy = event.y_root - self.move_lasty
        self.move_lastx = event.x_root
        self.move_lasty = event.y_root
        self.x = clamp(0, 1640-200, self.x + dx) # should depend on
        self.y = clamp(0, 1480-200, self.y + dy) # actual size here
        self.f.place_configure(x=self.x, y=self.y)

    def minimize_maximize(self):
        self.root.iconify()
    def close_window(self):
        self.destroy()
    def __init__(self, root, title, x, y,w,h):
        self.root = root

        self.x = x; self.y = y
        self.f = Frame(self.root, bd=1, relief=RAISED)
        self.f.place(x=x, y=y, width=w, height=h)


        self.l = Label(self.f, bd=1, bg="#08246b", fg="white",text=title)


        self.l.pack(fill=X)

        self.min_max_btn = Button(self.l,text='-',command=self.minimize_maximize)

        self.close_btn = Button(self.l,text='X',command=self.close_window)
        self.close_btn.pack(side=RIGHT)
        self.min_max_btn.pack(side=RIGHT)
        self.l.bind('<1>', self.MoveWindowStart)
        self.f.bind( '<1>', self.focus)
        self.l.bind( '<B1-Motion>', self.MoveWindow)
        # self.f.bind('<B1-Motion>', self.MoveWindow)
        self.all.append(self)
        self.focus()

    def focus(self, event=None):
        self.f.tkraise()
        for w in self.all:
            if w is self:
                w.l.configure(bg="#08246b", fg="white")
            else:
                w.l.configure(bg="#d9d9d9", fg="black")
if __name__ == "__main__":
    root = Tk()
    root.title("...")
    root.geometry("%dx%d%+d%+d"%(640, 480, 0, 0)) #useful for main window size
    x = MovingFrame(root, "Window 1", 10, 10,100,100)

    root.mainloop()