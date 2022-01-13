from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Servis izvještaj")
root.geometry("700x600")

frame = Frame(root)
frame.grid()


#frame, label i entry za osnovne informacije
label_informacije = Label(frame, text="Informacije: ")
label_informacije.grid(row=0, column=0, sticky="e")

label_djelatnik = Label(frame, text="Djelatnik: ")
label_djelatnik.grid(row=1, column=0, sticky="e")

entry_djelatnik = Entry(frame, width = 25)
entry_djelatnik.grid(row=1, column=1)

label_naziv_racunala = Label(frame, text="Naziv računala: ")
label_naziv_racunala.grid(row=2, column=0, sticky="e")

entry_naziv_racunala = Entry(frame, width = 25)
entry_naziv_racunala.grid(row=2, column=1)

label_korisnicko_ime = Label(frame, text="Korisničko ime ")
label_korisnicko_ime.grid(row=3, column=0, sticky="e")

entry_korisnicko_ime = Entry(frame, width = 25)
entry_korisnicko_ime.grid(row=3, column=1)

label_lozinka = Label(frame, text="Lozinka ")
label_lozinka.grid(row=4, column=0, sticky="e")

entry_lozinka = Entry(frame, width = 25)
entry_lozinka.grid(row=4, column=1)

label_inventurni_broj = Label(frame, text="Inventurni broj: ")
label_inventurni_broj.grid(row=5, column=0, sticky="e")

entry_inventurni_broj = Entry(frame, width = 25)
entry_inventurni_broj.grid(row=5, column=1)

label_mac_adresa = Label(frame, text="MAC adresa: ")
label_mac_adresa.grid(row=6, column=0, sticky="e")

entry_mac_adresa = Entry(frame, width = 25)
entry_mac_adresa.grid(row=6, column=1)

label_razmak_a1 = Label(frame, text=" ")
label_razmak_a1.grid(row=7, column=0)


#label i entry za hardware info
label_hardware = Label(frame, text="Hardware: ")
label_hardware.grid(row=0, column=3, sticky="e")

label_model = Label(frame, text="Model: ")
label_model.grid(row=1, column=3, sticky="e")

entry_model = Entry(frame, width = 25)
entry_model.grid(row=1, column=4)

label_cpu = Label(frame, text="CPU: ")
label_cpu.grid(row=2, column=3, sticky="e")

entry_cpu = Entry(frame, width = 25)
entry_cpu.grid(row=2, column=4)

label_ram = Label(frame, text="RAM: ")
label_ram.grid(row=3, column=3, sticky="e")

entry_ram = Entry(frame, width = 25)
entry_ram.grid(row=3, column=4)

label_mrezna = Label(frame, text="Mrežna kartica: ")
label_mrezna.grid(row=4, column=3, sticky="e")

entry_mrezna = Entry(frame, width = 25)
entry_mrezna.grid(row=4, column=4)

label_graficka = Label(frame, text="Grafička kartica: ")
label_graficka.grid(row=5, column=3, sticky="e")

entry_graficka = Entry(frame, width = 25)
entry_graficka.grid(row=5, column=4)

label_glavna_particija = Label(frame, text="Glavna particija: ")
label_glavna_particija.grid(row=6, column=3, sticky="e")

entry_glavna_particija = Entry(frame, width = 25)
entry_glavna_particija.grid(row=6, column=4)

label_dodatne_particije = Label(frame, text="Dodatne particije: ")
label_dodatne_particije.grid(row=7, column=3, sticky="e")

entry_dodatne_particije = Entry(frame, width = 25)
entry_dodatne_particije.grid(row=7, column=4)


#instalacije
label_instalacije = Label(frame, text = "Instalacije: ")
label_instalacije.grid(row=8, column=0, sticky="e")

label_os = Label(frame, text = "OS: ")
label_os.grid(row=9, column=0, sticky="e")

entry_os = Entry(frame, width=25)
entry_os.grid(row=9, column=1)

label_programi = Label(frame, text = "Programi: ")
label_programi.grid(row=10, column=0, sticky="e")

text_programi = Text(frame, width=29, height=20)
text_programi.grid(row=10, column=1)

#napomene
label_napomene = Label(frame, text = "Napomene: ")
label_napomene.grid(row=9, column=4, sticky="w")

text_napomene = Text(frame, width=29, height=20)
text_napomene.grid(row=10, column=4)


#datum
label_datum = Label(frame, text = "Datum: ")
label_datum.grid(row=11, column=0, sticky="e")

entry_datum = Entry(frame, width=25)
entry_datum.grid(row=11, column=1)

#frame, radove izveo
label_radovi = Label(frame, text = "Radove izveo: ")
label_radovi.grid(row=11, column=3, sticky="e")

entry_radovi = Entry(frame, width=25)
entry_radovi.grid(row=11, column=4)



root.mainloop()