#pip3 install forex-python - to install package

from tkinter import *
from tkinter import messagebox
from forex_python.converter import CurrencyRates
from TextWithLabel import *

class NegativeValueError(Exception):
    pass

class Application(object):

    color = "lightgray"
    font = 'Helvetica 10 bold'

    def __init__(self):
        self.window=Tk()
        self.window.configure(background=self.color)
        self.window.geometry("300x300")
        self.window.title("Currency converter")
        self.frame = Frame(self.window, bg=self.color)
        self.frame.grid()
        
        self.createWidgets()
        self.frame.grid_columnconfigure(0, weight=2)
        self.frame.grid_columnconfigure(1, weight=0)
        self.window.mainloop()

    def createWidgets(self):
        label1=Label(self.frame, bg=self.color, text="Enter the amount in PLN", anchor='w',font=self.font)
        label1.grid(row=0,column=0,sticky=W)

        self.field1=Entry(self.frame)
        self.field1.grid(row=0,column=1,sticky=W)
        self.button1=Button(self.frame, bg=self.color,text="Calculate", width=20,font=self.font)
        self.button1.grid(row=1,column=0,sticky=W,pady=10)
        self.button1["command"]=self.changeCurrency

        c = CurrencyRates()

        TextWithLabel.setFirstRow(3)
        TextWithLabel.setFont(self.font)
        TextWithLabel.setBgColor(self.color)

        self.TextWithLabel = []
        self.TextWithLabel.append(TextWithLabel(self.frame, "EUR", c.get_rate('PLN', 'EUR')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "USD", c.get_rate('PLN', 'USD')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "GBP", c.get_rate('PLN', 'GBP')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "CHF", c.get_rate('PLN', 'CHF')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "AUD", c.get_rate('PLN', 'AUD')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "JPY", c.get_rate('PLN', 'JPY')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "SEK", c.get_rate('PLN', 'SEK')))
        self.TextWithLabel.append(TextWithLabel(self.frame, "CZK", c.get_rate('PLN', 'CZK')))

    def refreshView(self, pln):
        for i in self.TextWithLabel:
            i.refresh(pln)
        
    def changeCurrency(self):
        try:
            pln = float(self.field1.get())
            
            if float(self.field1.get())< 0:
                raise NegativeValueError   

        except NegativeValueError:
            messagebox.showerror("Error!","You cannot convert a negative amount")
        except:
            messagebox.showerror("Error!","The given data must be positive numbers!")
        else:
           self.refreshView(pln)

app = Application()
