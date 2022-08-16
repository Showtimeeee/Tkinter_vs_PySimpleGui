from cmath import *
import PySimpleGUI as sg

layout = [
    [sg.Text('Введите выражение:', size=(16, 1)), sg.Input(k='-IN-'), sg.Button('=')],
    [sg.Text('результат', size=(16, 1)), sg.Input(k='-OUT-')]
]
window = sg.Window('PsG calc', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '=':
        window['-OUT-'].update(eval(values['-IN-']))

window.close()




