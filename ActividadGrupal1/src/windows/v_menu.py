import PySimpleGUI as sg
from src.windows.Utilidades import buttons

def build():

    pad = ((20,0),(0,20))

    l_cont = [
        [sg.Text("MENU", font=("Verdana", 25), text_color="#f3f4ed", background_color="#536162",pad = ((0,0),(20,16)), size = (20,1), justification = "c" )],
        buttons("JUGAR",17,"-JUGAR-",pad = pad),
        buttons("CONFIGURACIONES",17,"-CONFIGURACIONES-",pad = pad),
        buttons("TABLA DE PUNTOS",17,"-TABLA_PUNTOS-",pad = pad),
        buttons("ESTADISTICAS",17,"-ESTADISTICAS-",pad = pad),
        buttons("REGLAS",17,"-REGLAS-",pad = pad),
        buttons("AYUDA",17,"-AYUDA-",pad = pad),
        buttons("SALIR",17,"-SALIR-",pad = pad),
    ]

    layout = [
        [sg.Text("MemPy", font=("Helvetica", 45), text_color="#f3f4ed",background_color="#424642",pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color="#536162", element_justification="l", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color="#424642", element_justification="c", margins = (20,20))


"""window = build()
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()"""