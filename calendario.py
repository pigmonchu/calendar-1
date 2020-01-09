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

    def __init__(self, parent, onclic): #<-- Nuevo parámetro de construcción onclic. La función de línea 56
        ttk.Frame.__init__(self, parent, width=WIDTHBTN, height=HEIGHTBTN)

        self.pack_propagate(0)
        self.onClic = onclic #<-- nuevo atributo. Función con firma (self, valor:string) que será llamada al hacer clic sobre el número.

        m = ttk.Style()
        m.theme_use('alt')
        m.configure('my.TLabel', font=('Helvetica', '21', 'bold'), anchor='se', background='white', borderwidth='1', relief='ridge')

        self.monthDay = ttk.Label(self, text=self.cadenaDia, style='my.TLabel', padding=4)
        self.monthDay.pack(side=TOP, fill=BOTH, expand=True)
    
    def valor(self, texto, color):
        self.cadenaDia = texto
        if color in ('red', 'black'):
            labelDia = self.cadenaDia.day
            self.monthDay.config(text=labelDia, foreground=color)
            self.monthDay.bind("<Button-1>", self.changeColor)
        if color in ('grey'):
            self.monthDay.config(text=self.cadenaDia, foreground=color)
       
    def changeColor(self, event):
        try:
            if isinstance(self.cadenaDia, date):
                self.monthDay.config(foreground='blue')
                fechaElegida = str(self.cadenaDia.day) + ' de ' + (self.cadenaDia.strftime("%B")).title() + ' de ' + str(self.cadenaDia.year)
                self.onClic(fechaElegida) #<-- Se invoca onClic (es decir, el método informado en la creación, como el command de Button)
        except:
            return None

    def asignaFx(self, texto):
        print(fechaElegida)


class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=7*WIDTHBTN, height=HEIGHTBTN)

        self.pack_propagate(0)

        fechaElegida = str(date.today().day) + ' de ' + (date.today().strftime("%B")).title() + ' de ' + str(date.today().year)

        self.date = ttk.Label(self, text=fechaElegida, font='Helvetica 12', anchor='center', background='white', foreground='black', borderwidth='1', relief='ridge')
        self.date.pack(side=TOP, fill=BOTH, expand=True)


class Calendar(ttk.Frame):
    listDays = []
    hoy = date.today()
    hoy = hoy.replace(day=1)
    def __createCalendar(self):
        layoutCalendar = ttk.Frame(self, name='layoutCalendar')

        for rowMonth in range(2, 8):
            for columnMonth in range(0, 7):
                self.day = MonthDay(self, self.informaDia) #<-- Creación de MonthDay informando que hacer cuando se haga clic en el
                self.day.grid(row=rowMonth, column=columnMonth)
                self.listDays.append(self.day)

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

        self.fxBox = Display(self)
        self.fxBox.grid(column=0, row=8, columnspan=7)


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
            self.diaCalendar = self.hoy.replace(day=diaMesAct)
            if indMesAct in (5,6,12,13,19,20,26,27,33,34,40,41):
                self.listDays[indMesAct].valor(self.diaCalendar, 'red')
            else:
                self.listDays[indMesAct].valor(self.diaCalendar, 'black')
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

    def informaDia(self, valor): #<-- Método de calendar que relaciona MonthDay con Display. Ya que Calendar controla tanto MonthdDay como Display
        print(valor)
        self.fxBox.date.config(text = valor)