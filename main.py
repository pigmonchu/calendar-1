from tkinter import *
from tkinter import ttk
from datetime import datetime, date

from calendario import WIDTHBTN, HEIGHTBTN, Calendar

class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Calendario')
        self.configure(bg='white')
        self.geometry("{}x{}+360+25".format(WIDTHBTN*7, HEIGHTBTN*8))
        
        c = Calendar(self)
        c.pack()


    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()
