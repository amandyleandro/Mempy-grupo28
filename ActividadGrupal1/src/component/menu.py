from src.windows import v_menu
from src.component import configuraciones
import PySimpleGUI as sg


def start():
    
    window = loop()
    window.close()

def loop():
    window = v_menu.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-SALIR-"):
            break
        
        if event == "-CONFIGURACIONES-":
            window.hide()
            configuraciones.start()
            window.un_hide()
    return window