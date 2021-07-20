import PySimpleGUI as sg

podatak = 0

def unos_podataka():
    global podatak
    podatak = 'novi podatak'
    return podatak

def open_window():
    global podatak
    layout = [[sg.Text(podatak, key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

def main():
    global podatak
    layout = [[sg.Text(podatak)],sg.Button("Open Window", key="open")]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            unos_podataka()
            open_window()
    return podatak    
    window.close()
if __name__ == "__main__":
    main()