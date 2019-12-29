from tkinter import *
from tkinter import ttk

from calendario import WIDTHBTN, HEIGHTBTN, Calendar

class ControlWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Ventana de Control')
        self.geometry("{}x{}+60+25".format(WIDTHBTN*4, HEIGHTBTN*2))
        self.btn = ttk.Button(self, text='Calendario', command=CalendarWindow)
        self.btn.place(x=40, y=20)
        self.etiqueta = ttk.Label(self, text='', font='Helvetica 11', anchor='center', width=20, background='white', foreground='black', borderwidth='1', relief='groove', padding=3)
        self.etiqueta.place(x=40, y=50)

    def start(self):
        self.mainloop()


class CalendarWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Calendario')
        self.configure(bg='white')
        self.geometry("{}x{}+360+25".format(WIDTHBTN*7, HEIGHTBTN*7))
        
        c = Calendar(self)
        c.pack() 


if __name__ == '__main__':
    app = ControlWindow()
    app.start()