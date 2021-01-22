from tkinter import *
from tkinter import messagebox

class TextWithLabel():

    rowInTurn = 0
    width = 20
    height = 1

    currency = 0

    def __init__(self, frame, text, currency):
        self.field=Text(frame, width=self.width, height=self.height)
        self.field.grid(row=TextWithLabel.rowInTurn, column=0, sticky=W, pady=2)
        self.label=Label(frame, bg=self.bgColor, text=text, font=TextWithLabel.font)
        self.label.grid(row=TextWithLabel.rowInTurn, column=1, sticky=W,pady=2)
        self.currency = currency
        TextWithLabel.rowInTurn+=1

    def refresh(self, pln):

        value = pln * self.currency

        self.field.delete(0.0, END)
        self.field.insert(0.0, str(round(value, 4)))

    @staticmethod
    def setFont(font):
        TextWithLabel.font = font

    @staticmethod
    def setBgColor(color):
        TextWithLabel.bgColor = color

    @staticmethod
    def setFirstRow(firstRow):
        TextWithLabel.rowInTurn = firstRow