#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import potrebnih modula
from tkinter import *
from tkinter import ttk
import xlrd, xlwt, sqlite3, os

def ucitavanje_izvjestaja(event):
    os.system("python3 prvi_gui.py")

def unos_podataka(event):
    print("bla")

# stvaranje grafickog prozora
root = Tk()
root.wm_title("Završni rad")
frame = Frame(root)
frame.grid()

ucitajIzvjestajButton = Button(frame, width=15, height=1, text='Učitavanje izvještaja', fg='red', bg='silver')
ucitajIzvjestajButton.bind("<Button-1>", ucitavanje_izvjestaja)
ucitajIzvjestajButton.bind("<Button-2>", ucitavanje_izvjestaja)
ucitajIzvjestajButton.bind("<Button-3>", ucitavanje_izvjestaja)
ucitajIzvjestajButton.grid(row=0, column=0)

izmjeneButton = Button(frame, width=15, height=1, text='Izmjene u BP', fg='red', bg='silver')
izmjeneButton.bind("<Button-1>", unos_podataka)
izmjeneButton.bind("<Button-2>", unos_podataka)
izmjeneButton.bind("<Button-3>", unos_podataka)
izmjeneButton.grid(row=0, column=1)

pretragaButton = Button(frame, width=15, height=1, text='Pretraga BP', fg='red', bg='silver')
pretragaButton.bind("<Button-1>", unos_podataka)
pretragaButton.bind("<Button-2>", unos_podataka)
pretragaButton.bind("<Button-3>", unos_podataka)
pretragaButton.grid(row=1, column=0)

generirajButton = Button(frame, width=15, height=1, text='Generiranje izvještaja', fg='red', bg='silver')
generirajButton.bind("<Button-1>", unos_podataka)
generirajButton.bind("<Button-2>", unos_podataka)
generirajButton.bind("<Button-3>", unos_podataka)
generirajButton.grid(row=1, column=1)

root.mainloop()
