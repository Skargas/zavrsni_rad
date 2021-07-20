#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
import xlrd
import sqlite3

def unos_podataka(event):
    mtext = ment.get()
    workbook = xlrd.open_workbook(mtext)
    sheet = workbook.sheet_by_index(0)
    djelatnik = sheet.cell(4, 2).value
    djelatnikLabel = Label(lf1, text="Djelatnik:", fg='red').grid(row=1, column=0)
    djelatnikLabel1 = Label(lf1, text=djelatnik).grid(row=1, column=1)
    nazivRacunala = sheet.cell(5, 2).value
    nazivRacunalaLabel = Label(lf1, text="Naziv Računala:", fg='red').grid(row=2, column=0)
    nazivRacunalaLabel1 = Label(lf1, text=nazivRacunala).grid(row=2, column=1)
    korisnickoIme = sheet.cell(6, 2).value
    korisnickoImeLabel = Label(lf1, text="Korisničko ime:", fg='red').grid(row=3, column=0)
    korisnickoImeLabel1 = Label(lf1, text=korisnickoIme).grid(row=3, column=1)
    lozinka = sheet.cell(7, 2).value
    lozinkaLabel = Label(lf1, text="Lozinka:", fg='red').grid(row=4, column=0)
    lozinkaLabel1 = Label(lf1, text=lozinka).grid(row=4, column=1)
    inventurniBroj = sheet.cell(8, 2).value
    inventurniBrojLabel = Label(lf1, text="Inventurni broj:", fg='red').grid(row=5, column=0)
    inventurniBrojLabel1 = Label(lf1, text=inventurniBroj).grid(row=5, column=1)
    macAdresa = sheet.cell(9, 2).value
    macAdresaLabel = Label(lf1, text="MAC adresa:", fg='red').grid(row=6, column=0)
    macAdresaLabel1 = Label(lf1, text=macAdresa).grid(row=6, column=1)
    operativniSustav = sheet.cell(13, 2).value
    operativniSustavLabel = Label(lf1, text="Operativni sustav:", fg='red').grid(row=7, column=0)
    operativniSustavLabel1 = Label(lf1, text=operativniSustav).grid(row=7, column=1)
    dodatniProgram1 = sheet.cell(15, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=8, column=0)
    dodatniProgram1Label1 = Label(lf1, text=dodatniProgram1).grid(row=8, column=1)
    dodatniProgram2 = sheet.cell(16, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=9, column=0)
    dodatniProgram2Label = Label(lf1, text=dodatniProgram2).grid(row=9, column=1)
    dodatniProgram3 = sheet.cell(17, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=10, column=0)
    dodatniProgram3Label = Label(lf1, text=dodatniProgram3).grid(row=10, column=1)
    dodatniProgram4 = sheet.cell(18, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=11, column=0)
    dodatniProgram4Label = Label(lf1, text=dodatniProgram4).grid(row=11, column=1)
    dodatniProgram5 = sheet.cell(19, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=12, column=0)
    dodatniProgram5Label = Label(lf1, text=dodatniProgram5).grid(row=12, column=1)
    dodatniProgram6 = sheet.cell(20, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=13, column=0)
    dodatniProgram6Label = Label(lf1, text=dodatniProgram6).grid(row=13, column=1)
    dodatniProgram7 = sheet.cell(21, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=14, column=0)
    dodatniProgram7Label = Label(lf1, text=dodatniProgram7).grid(row=14, column=1)
    dodatniProgram8 = sheet.cell(22, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=15, column=0)
    dodatniProgram8Label = Label(lf1, text=dodatniProgram8).grid(row=15, column=1)
    dodatniProgram9 = sheet.cell(23, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=16, column=0)
    dodatniProgram9Label = Label(lf1, text=dodatniProgram9).grid(row=16, column=1)
    dodatniProgram10 = sheet.cell(24, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=17, column=0)
    dodatniProgram10Label = Label(lf1, text=dodatniProgram10).grid(row=17, column=1)
    dodatniProgram11 = sheet.cell(25, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=18, column=0)
    dodatniProgram11Label = Label(lf1, text=dodatniProgram11).grid(row=18, column=1)
    dodatniProgram12 = sheet.cell(26, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=19, column=0)
    dodatniProgram12Label = Label(lf1, text=dodatniProgram12).grid(row=19, column=1)
    dodatniProgram13 = sheet.cell(27, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=20, column=0)
    dodatniProgram13Label = Label(lf1, text=dodatniProgram13).grid(row=20, column=1)
    dodatniProgram14 = sheet.cell(28, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=21, column=0)
    dodatniProgram14Label = Label(lf1, text=dodatniProgram14).grid(row=21, column=1)
    dodatniProgram15 = sheet.cell(29, 1).value
    dodatniProgram1Label = Label(lf1, text="Dodatni program:", fg='red').grid(row=22, column=0)
    dodatniProgram15Label = Label(lf1, text=dodatniProgram15).grid(row=22, column=1)
    model = sheet.cell(4, 5).value
    modelLabel = Label(rf1, text="Model:", fg='red').grid(row=1, column=0)
    modelLabel1 = Label(rf1, text=model).grid(row=1, column=1)
    cpu = sheet.cell(5, 5).value
    cpuLabel = Label(rf1, text="Cpu:", fg='red').grid(row=2, column=0)
    cpuLabel1 = Label(rf1, text=cpu).grid(row=2, column=1)
    ram = sheet.cell(6, 5).value
    ramLabel = Label(rf1, text="RAM:", fg='red').grid(row=3, column=0)
    ramLabel1 = Label(rf1, text=ram).grid(row=3, column=1)
    mreznaKartica = sheet.cell(7, 5).value
    mreznaKarticaLabel = Label(rf1, text="Mrežna kartica:", fg='red').grid(row=4, column=0)
    mreznaKarticaLabel1 = Label(rf1, text=mreznaKartica).grid(row=4, column=1)
    grafickaKartica = sheet.cell(8, 5).value
    grafickaKarticaLabel = Label(rf1, text="Grafička kartica:", fg='red').grid(row=5, column=0)
    grafickaKarticaLabel1 = Label(rf1, text=grafickaKartica).grid(row=5, column=1)
    glavnaParticija = sheet.cell(9, 5).value
    glavnaParticijaLabel = Label(rf1, text="Glavna particija:", fg='red').grid(row=6, column=0)
    glavnaParticijaLabel1 = Label(rf1, text=glavnaParticija).grid(row=6, column=1)
    dodatneParticije = sheet.cell(10, 5).value
    dodatneParticijeLabel = Label(rf1, text="Dodatne particije:", fg='red').grid(row=7, column=0)
    dodatneParticijeLabel1 = Label(rf1, text=dodatneParticije).grid(row=7, column=1)
    napomena1 = sheet.cell(13, 4).value
    napomena1Label = Label(rf1, text="Napomena:", fg='red').grid(row=8, column=0)
    napomena1Label1 = Label(rf1, text=napomena1).grid(row=8, column=1)
    napomena2 = sheet.cell(14, 4).value
    napomena2Label = Label(rf1, text="Napomena:", fg='red').grid(row=9, column=0)
    napomena2Label1 = Label(rf1, text=napomena2).grid(row=9, column=1)
    napomena3 = sheet.cell(15, 4).value
    napomena3Label = Label(rf1, text="Napomena:", fg='red').grid(row=10, column=0)
    napomena3Label1 = Label(rf1, text=napomena3).grid(row=10, column=1)
    napomena4 = sheet.cell(16, 4).value
    napomena4Label = Label(rf1, text="Napomena:", fg='red').grid(row=11, column=0)
    napomena4Label1 = Label(rf1, text=napomena4).grid(row=11, column=1)
    napomena5 = sheet.cell(17, 4).value
    napomena5Label = Label(rf1, text="Napomena:", fg='red').grid(row=12, column=0)
    napomena5Label1 = Label(rf1, text=napomena5).grid(row=12, column=1)
    napomena6 = sheet.cell(18, 4).value
    napomena6Label = Label(rf1, text="Napomena:", fg='red').grid(row=13, column=0)
    napomena6Label1 = Label(rf1, text=napomena6).grid(row=13, column=1)
    napomena7 = sheet.cell(19, 4).value
    napomena7Label = Label(rf1, text="Napomena:", fg='red').grid(row=14, column=0)
    napomena7Label1 = Label(rf1, text=napomena7).grid(row=14, column=1)
    napomena8 = sheet.cell(20, 4).value
    napomena8Label = Label(rf1, text="Napomena:", fg='red').grid(row=15, column=0)
    napomena8Label1 = Label(rf1, text=napomena8).grid(row=15, column=1)
    napomena9 = sheet.cell(21, 4).value
    napomena9Label = Label(rf1, text="Napomena:", fg='red').grid(row=16, column=0)
    napomena9Label1 = Label(rf1, text=napomena9).grid(row=16, column=1)
    napomena10 = sheet.cell(22, 4).value
    napomena10Label = Label(rf1, text="Napomena:", fg='red').grid(row=17, column=0)
    napomena10Label1 = Label(rf1, text=napomena10).grid(row=17, column=1)
    napomena11 = sheet.cell(23, 4).value
    napomena11Label = Label(rf1, text="Napomena:", fg='red').grid(row=18, column=0)
    napomena11Label1 = Label(rf1, text=napomena11).grid(row=18, column=1)
    napomena12 = sheet.cell(24, 4).value
    napomena12Label = Label(rf1, text="Napomena:", fg='red').grid(row=19, column=0)
    napomena12Label1 = Label(rf1, text=napomena12).grid(row=19, column=1)
    napomena13 = sheet.cell(25, 4).value
    napomena13Label = Label(rf1, text="Napomena:", fg='red').grid(row=20, column=0)
    napomena13Label1 = Label(rf1, text=napomena13).grid(row=20, column=1)
    napomena14 = sheet.cell(26, 4).value
    napomena14Label = Label(rf1, text="Napomena:", fg='red').grid(row=21, column=0)
    napomena14Label1 = Label(rf1, text=napomena14).grid(row=21, column=1)
    napomena15 = sheet.cell(27, 4).value
    napomena15Label = Label(rf1, text="Napomena:", fg='red').grid(row=22, column=0)
    napomena15Label1 = Label(rf1, text=napomena15).grid(row=22, column=1)
    napomena16 = sheet.cell(28, 4).value
    napomena16Label = Label(rf1, text="Napomena:", fg='red').grid(row=23, column=0)
    napomena16Label1 = Label(rf1, text=napomena16).grid(row=23, column=1)
    napomena17 = sheet.cell(29, 4).value
    napomena17Label = Label(rf1, text="Napomena:", fg='red').grid(row=24, column=0)
    napomena17Label1 = Label(rf1, text=napomena17).grid(row=24, column=1)
    datum = sheet.cell(31, 2).value
    datumlabel = Label(lf2, text="Datum:", fg='red').grid(row=0, column=0)
    datumlabel1 = Label(lf2, text=datum).grid(row=0, column=1)
    itDjelatnik = sheet.cell(31, 5).value
    itDjelatnikLabel = Label(rf2, text="IT djelatnik:", fg='red').grid(row=0, column=0)
    itDjelatnikLabel1 = Label(rf2, text=itDjelatnik).grid(row=0, column=1)

    conn = sqlite3.connect('izvjestajiBaza.db')
    c = conn.cursor()

    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS izvjestajTablica(inventurniBroj INTEGER, djelatnik TEXT, "
                  "nazivRacunala TEXT, korisnickoIme TEXT, lozinka TEXT, macAdresa TEXT, operativniSustav TEXT, "
                  "dodatniProgram1 TEXT, dodatniProgram2 TEXT, dodatniProgram3 TEXT, dodatniProgram4 TEXT, "
                  "dodatniProgram5 TEXT, dodatniProgram6 TEXT, dodatniProgram7 TEXT, dodatniProgram8 TEXT, "
                  "dodatniProgram9 TEXT, dodatniProgram10 TEXT, dodatniProgram11 TEXT, dodatniProgram12 TEXT, "
                  "dodatniProgram13 TEXT, dodatniProgram14 TEXT, dodatniProgram15 TEXT, model TEXT, cpu TEXT, "
                  "ram TEXT, mreznaKartica TEXT, grafickaKartica TEXT, glavnaParticija TEXT, dodatneParticije TEXT, "
                  "napomena1 TEXT, napomena2 TEXT, napomena3 TEXT, napomena4 TEXT, napomena5 TEXT, napomena6 TEXT, "
                  "napomena7 TEXT, napomena8 TEXT, napomena9 TEXT, napomena10 TEXT, napomena11 TEXT, napomena12 TEXT, "
                  "napomena13 TEXT, napomena14 TEXT, napomena15 TEXT, napomena16 TEXT, napomena17 TEXT, datum TEXT, "
                  "itDjelatnik TEXT)")

    def data_entry():
        c.execute("INSERT INTO izvjestajTablica(inventurniBroj, djelatnik, nazivRacunala, korisnickoIme, lozinka, "
                  "macAdresa, operativniSustav, dodatniProgram1, dodatniProgram2, dodatniProgram3, dodatniProgram4, "
                  "dodatniProgram5, dodatniProgram6, dodatniProgram7, dodatniProgram8, dodatniProgram9, "
                  "dodatniProgram10, dodatniProgram11, dodatniProgram12, dodatniProgram13, dodatniProgram14, "
                  "dodatniProgram15, model, cpu, ram, mreznaKartica, grafickaKartica, glavnaParticija, "
                  "dodatneParticije, napomena1, napomena2, napomena3, napomena4, napomena5, napomena6, napomena7, "
                  "napomena8, napomena9, napomena10, napomena11, napomena12, napomena13, napomena14, napomena15, "
                  "napomena16, napomena17, datum, itDjelatnik) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                  "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                  "?)", (inventurniBroj, djelatnik, nazivRacunala, korisnickoIme, lozinka, macAdresa,
                        operativniSustav, dodatniProgram1, dodatniProgram2, dodatniProgram3, dodatniProgram4,
                        dodatniProgram5, dodatniProgram6, dodatniProgram7, dodatniProgram8, dodatniProgram9,
                        dodatniProgram10, dodatniProgram11, dodatniProgram12, dodatniProgram13,
                        dodatniProgram14, dodatniProgram15, model, cpu, ram, mreznaKartica,
                        grafickaKartica, glavnaParticija, dodatneParticije, napomena1, napomena2, napomena3,
                        napomena4, napomena5, napomena6, napomena7, napomena8, napomena9, napomena10,
                        napomena11, napomena12, napomena13, napomena14, napomena15, napomena16,
                        napomena17, datum, itDjelatnik))
        conn.commit()


    def run_all(event):
        create_table()
        data_entry()
        gotovoLabel = Label(lf3, text="Pohranjeno!").grid(row=1, column=0)
        return



    pohraniPodatkeButton = Button(lf3, width=15, height=1)
    pohraniPodatkeButton.config(text='Pohrani u BP!', fg='red', bg='silver')
    pohraniPodatkeButton.bind("<Button-1>", run_all)
    pohraniPodatkeButton.bind("<Button-2>", run_all)
    pohraniPodatkeButton.bind("<Button-3>", run_all)
    pohraniPodatkeButton.grid(row=0, column=0)





root = Tk()
root.geometry("1200x800")
root.wm_title('Unesite putanju do izvještaja, sa ekstenzijom:')
frame = Frame(root)
frame.grid()

ment = StringVar()

lf1 = Frame(frame)
lf1.grid(row=1, column=0)

lf2 = Frame(frame)
lf2.grid(row=2, column=0)

lf3 = Frame(frame)
lf3.grid(row=3, column=0)

rf1 = Frame(frame)
rf1.grid(row=1, column=2)

rf2 = Frame(frame)
rf2.grid(row=2, column=2)

rf3 = Frame(frame)
rf3.grid(row=3, column=2)

lokacijaEntry = Entry(frame, textvariable=ment, width=50).grid(row=0, column=1)

ucitajIzvjestajButton = Button(frame, width=15, height=1, text='Učitaj izvještaj', fg='red', bg='silver')
ucitajIzvjestajButton.bind("<Button-1>", unos_podataka)
ucitajIzvjestajButton.bind("<Button-2>", unos_podataka)
ucitajIzvjestajButton.bind("<Button-3>", unos_podataka)
ucitajIzvjestajButton.grid(row=0, column=0)



root.mainloop()
