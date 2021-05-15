from src.windows import v_configuraciones
from src.model.configuracion import configuracion
from src.component import c_textos
import json
import PySimpleGUI as sg


def start(user):
    window = loop(user)
    window.close()

def loop(user):
    # user.imprimir()
    # user.buscarConfig(user.username).imprimir()
    conf = user.buscarConfig(user.username)
    window = v_configuraciones.build(conf)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break
        if event == "-GUARDAR-":
            conf = configuracion(conf.textos , values["-CASILLAS-"], values["-COINCIDENCIAS-"], values["-TIEMPO-"], values["-ESTILO-"], values["-ELEMENTOS-"], values["-AYUDAS-"])
            # user.imprimir()
            # print("----------------------")
            user.setConfig(conf)
            # user.imprimir()
            # user.imprimirConfig()
            user.guardarJson(user.username)
            break
        if event == "-CONF_TXT-":
            window.hide()
            user.textos = c_textos.start(conf)
            window.un_hide()
    return window