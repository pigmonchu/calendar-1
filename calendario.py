from tkinter import *
from tkinter import ttk
from datetime import datetime, date
import locale

locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
HEIGHTBTN = 50
WIDTHBTN = 68

class Header(ttk.Frame):
    cadena = ''
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=7*WIDTHBTN, height=0.7*HEIGHTBTN)

        self.pack_propagate(0)

        self.__lbl = ttk.Label(self, text=self.cadena, anchor='center', font=('Helvetica', '21', 'bold'), background='white', foreground='black', borderwidth='1', relief='ridge')
        self.__lbl.pack(side=TOP, fill=BOTH, expand=True)

    def valor(self, texto):
        self.cadena = texto
        self.__lbl.config(text=self.cadena)


class CalendButton(ttk.Frame):
    def __init__(self, parent, text, command, wbtn=0.5, hbtn=0.5):
        ttk.Frame.__init__(self, parent, width=wbtn*WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TButton', font=('Helvetica', '11', 'bold'))

        self.__b = ttk.Button(self, style='my.TButton', text=text, command=command)
        self.__b.pack(side=TOP, fill=BOTH, expand=True)


class WeekDay(ttk.Frame):
    def __init__(self, parent, text):
        ttk.Frame.__init__(self,parent, width=WIDTHBTN, height=0.3*HEIGHTBTN)

        self.pack_propagate(0)

        self.__weekDay = ttk.Label(self, text=text, font='Helvetica 7', anchor='center', background='white', foreground='black', borderwidth='1', relief='ridge')
        self.__weekDay.pack(side=TOP, fill=X, expand=False)


class MonthDay(ttk.Frame):
    cadenaDia = ''

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTHBTN, height=HEIGHTBTN)

        self.pack_propagate(0)

        m = ttk.Style()
        m.theme_use('alt')
        m.configure('my.TLabel', font=('Helvetica', '21', 'bold'), anchor='se', background='white', borderwidth='1', relief='ridge')

        self.__monthDay = ttk.Label(self, text=self.cadenaDia, foreground='black', style='my.TLabel', padding=4)
        self.__monthDay.pack(side=TOP, fill=BOTH, expand=True)
    
    def valor(self, texto, color):
        self.cadenaDia = texto
        if color in ('red', 'black'):
            labelDia = self.cadenaDia.day
            self.__monthDay.config(text=labelDia, foreground=color)
            self.__monthDay.bind("<Button-1>", self.selectDate)
        if color in ('grey'):
            self.__monthDay.config(text=self.cadenaDia, foreground=color)

    def selectDate(self, event):
        self.__monthDay.config(foreground='blue')

'''
    def newWindow(self, texto):
        window = Toplevel()
        window.title('Fecha Elegida')
        window.geometry("{}x{}".format(WIDTHBTN*4, HEIGHTBTN*2))
        hoy = self.cadenaDia
        texto = str(hoy.day) + ' de ' + (hoy.strftime("%B")).title() + ' de ' + str(hoy.year)
        etiqueta = ttk.Label(window, text=texto, font='Helvetica 11', anchor='center', background='white', foreground='black', borderwidth='1', relief='groove', padding=3)
        etiqueta.place(x=40, y=15)
'''

class Calendar(ttk.Frame):
    listDays = []
    hoy = date.today()
    def __createCalendar(self):
        layoutCalendar = ttk.Frame(self, name='layoutCalendar')

        self.Day0 = MonthDay(self)
        self.Day0.grid(column=0, row=2)
        self.listDays.append(self.Day0)

        self.Day1 = MonthDay(self)
        self.Day1.grid(column=1, row=2)
        self.listDays.append(self.Day1)

        self.Day2 = MonthDay(self)
        self.Day2.grid(column=2, row=2)
        self.listDays.append(self.Day2)

        self.Day3 = MonthDay(self)
        self.Day3.grid(column=3, row=2)
        self.listDays.append(self.Day3)

        self.Day4 = MonthDay(self)
        self.Day4.grid(column=4, row=2)
        self.listDays.append(self.Day4)

        self.Day5 = MonthDay(self)
        self.Day5.grid(column=5, row=2)
        self.listDays.append(self.Day5)

        self.Day6 = MonthDay(self)
        self.Day6.grid(column=6, row=2)
        self.listDays.append(self.Day6)

        self.Day7 = MonthDay(self)
        self.Day7.grid(column=0, row=3)
        self.listDays.append(self.Day7)

        self.Day8 = MonthDay(self)
        self.Day8.grid(column=1, row=3)
        self.listDays.append(self.Day8)

        self.Day9 = MonthDay(self)
        self.Day9.grid(column=2, row=3)
        self.listDays.append(self.Day9)

        self.Day10 = MonthDay(self)
        self.Day10.grid(column=3, row=3)
        self.listDays.append(self.Day10)
        
        self.Day11 = MonthDay(self)
        self.Day11.grid(column=4, row=3)
        self.listDays.append(self.Day11)

        self.Day12 = MonthDay(self)
        self.Day12.grid(column=5, row=3)
        self.listDays.append(self.Day12)

        self.Day13 = MonthDay(self)
        self.Day13.grid(column=6, row=3)
        self.listDays.append(self.Day13)

        self.Day14 = MonthDay(self)
        self.Day14.grid(column=0, row=4)
        self.listDays.append(self.Day14)

        self.Day15 = MonthDay(self)
        self.Day15.grid(column=1, row=4)
        self.listDays.append(self.Day15)

        self.Day16 = MonthDay(self)
        self.Day16.grid(column=2, row=4)
        self.listDays.append(self.Day16)

        self.Day17 = MonthDay(self)
        self.Day17.grid(column=3, row=4)
        self.listDays.append(self.Day17)

        self.Day18 = MonthDay(self)
        self.Day18.grid(column=4, row=4)
        self.listDays.append(self.Day18)

        self.Day19 = MonthDay(self)
        self.Day19.grid(column=5, row=4)
        self.listDays.append(self.Day19)

        self.Day20 = MonthDay(self)
        self.Day20.grid(column=6, row=4)
        self.listDays.append(self.Day20)

        self.Day21 = MonthDay(self)
        self.Day21.grid(column=0, row=5)
        self.listDays.append(self.Day21)

        self.Day22 = MonthDay(self)
        self.Day22.grid(column=1, row=5)
        self.listDays.append(self.Day22)

        self.Day23 = MonthDay(self)
        self.Day23.grid(column=2, row=5)
        self.listDays.append(self.Day23)

        self.Day24 = MonthDay(self)
        self.Day24.grid(column=3, row=5)
        self.listDays.append(self.Day24)

        self.Day25 = MonthDay(self)
        self.Day25.grid(column=4, row=5)
        self.listDays.append(self.Day25)

        self.Day26 = MonthDay(self)
        self.Day26.grid(column=5, row=5)
        self.listDays.append(self.Day26)

        self.Day27 = MonthDay(self)
        self.Day27.grid(column=6, row=5)
        self.listDays.append(self.Day27)

        self.Day28 = MonthDay(self)
        self.Day28.grid(column=0, row=6)
        self.listDays.append(self.Day28)

        self.Day29 = MonthDay(self)
        self.Day29.grid(column=1, row=6)
        self.listDays.append(self.Day29)

        self.Day30 = MonthDay(self)
        self.Day30.grid(column=2, row=6)
        self.listDays.append(self.Day30)

        self.Day31 = MonthDay(self)
        self.Day31.grid(column=3, row=6)
        self.listDays.append(self.Day31)

        self.Day32 = MonthDay(self)
        self.Day32.grid(column=4, row=6)
        self.listDays.append(self.Day32)

        self.Day33 = MonthDay(self)
        self.Day33.grid(column=5, row=6)
        self.listDays.append(self.Day33)

        self.Day34 = MonthDay(self)
        self.Day34.grid(column=6, row=6)
        self.listDays.append(self.Day34)

        self.Day35 = MonthDay(self)
        self.Day35.grid(column=0, row=7)
        self.listDays.append(self.Day35)

        self.Day36 = MonthDay(self)
        self.Day36.grid(column=1, row=7)
        self.listDays.append(self.Day36)

        self.Day37 = MonthDay(self)
        self.Day37.grid(column=2, row=7)
        self.listDays.append(self.Day37)

        self.Day38 = MonthDay(self)
        self.Day38.grid(column=3, row=7)
        self.listDays.append(self.Day38)

        self.Day39 = MonthDay(self)
        self.Day39.grid(column=4, row=7)
        self.listDays.append(self.Day39)

        self.Day40 = MonthDay(self)
        self.Day40.grid(column=5, row=7)
        self.listDays.append(self.Day40)

        self.Day41 = MonthDay(self)
        self.Day41.grid(column=6, row=7)
        self.listDays.append(self.Day41)

        return layoutCalendar

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        cadena = self.rellenaCab(self.hoy)

        self.cabecera = Header(self)
        self.cabecera.grid(column=0, row=0, columnspan=7)
        self.cabecera.valor(cadena)

        self.forwYear = CalendButton(self, text='>>', command=lambda: self.operar('>>', self.hoy)).grid(column=6, row=0, sticky=W, ipadx=3)
        self.forwMonth = CalendButton(self, text='>', command=lambda: self.operar('>', self.hoy)).grid(column=5, row=0, sticky=E, ipadx=3, padx=5)
        self.backYear = CalendButton(self, text='<<', command=lambda: self.operar('<<', self.hoy)).grid(column=0, row=0, sticky=E, ipadx=3)
        self.backMonth = CalendButton(self, text='<', command=lambda: self.operar('<', self.hoy)).grid(column=1, row=0, sticky=W, ipadx=3, padx=5)

        self.Monday = WeekDay(self, text='Lunes').grid(column=0, row=1)
        self.Tuesday = WeekDay(self, text='Martes').grid(column=1, row=1)
        self.Wednesday = WeekDay(self, text='Miércoles').grid(column=2, row=1)
        self.Thursday = WeekDay(self, text='Jueves').grid(column=3, row=1)
        self.Friday = WeekDay(self, text='Viernes').grid(column=4, row=1)
        self.Saturday = WeekDay(self, text='Sábado').grid(column=5, row=1)
        self.Sunday = WeekDay(self, text='Domingo').grid(column=6, row=1)

        self.layoutCalendar = self.__createCalendar()
        self.generaCalendar(self.hoy)


    def generaCalendar(self, hoy):
        mes = self.hoy.month
        if mes == 1:
            mesAnt = 12
        else:
            mesAnt = self.hoy.month - 1

        diasMesAct = self.calcDiasMes(mes)
        diasMesAnt = self.calcDiasMes(mesAnt)
  
        firstDay = self.hoy.replace(day=1)
        indMesAct = firstDay.weekday()
        indMesAnt = indMesAct - 1

        for diaMesAnt in range(diasMesAnt, diasMesAnt-indMesAnt-1, -1):
            self.listDays[indMesAnt].valor(diaMesAnt, 'grey')
            indMesAnt -= 1

        for diaMesAct in range(1, diasMesAct+1):
            diaCalendar = self.hoy.replace(day=diaMesAct)
            if indMesAct in (5,6,12,13,19,20,26,27,33,34,40,41):
                self.listDays[indMesAct].valor(diaCalendar, 'red')
            else:
                self.listDays[indMesAct].valor(diaCalendar, 'black')
            indMesAct += 1
        
        diaMesNew = 1
        while indMesAct < 42:
            self.listDays[indMesAct].valor(diaMesNew, 'grey')
            diaMesNew += 1
            indMesAct += 1
                   
    
    def rellenaCab(self, hoy):
        return (hoy.strftime("%B")).title() + ' ' + str(hoy.year)


    def calcDiasMes(self, month):
        if month in (1,3,5,7,8,10,12):
            diasMes = 31
        elif month in (4,6,9,11):
            diasMes = 30
        elif month == 2:
            anno = self.hoy.year
            if self.esBisiesto(anno):
                diasMes = 29
            else:
                diasMes = 28
        
        return diasMes


    def esBisiesto(self, year):
        return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


    def operar(self, operacion, hoy):
        self.layoutCalendar.destroy()
        if operacion == '>>':
            newDate = self.hoy.replace(year=self.hoy.year+1)
            self.hoy = newDate
            newCab = self.rellenaCab(self.hoy)
            self.cabecera.valor(newCab)
            self.generaCalendar(self.hoy)

        elif operacion == '>':
            if self.hoy.month == 12:
                newDate = self.hoy.replace(year=self.hoy.year+1, month=1)
            else:
                newDate = self.hoy.replace(month=self.hoy.month+1)
            self.hoy = newDate
            newCab = self.rellenaCab(self.hoy)
            self.cabecera.valor(newCab)
            self.generaCalendar(self.hoy)

        elif operacion == '<<':
            newDate = self.hoy.replace(year=self.hoy.year-1)
            self.hoy = newDate
            newCab = self.rellenaCab(self.hoy)
            self.cabecera.valor(newCab)
            self.generaCalendar(self.hoy)

        elif operacion == '<':
            if self.hoy.month == 1:
                newDate = self.hoy.replace(year=self.hoy.year-1, month=12)
            else:
                newDate = self.hoy.replace(month=self.hoy.month-1)
            self.hoy = newDate
            newCab = self.rellenaCab(self.hoy)
            self.cabecera.valor(newCab)
            self.generaCalendar(self.hoy)
