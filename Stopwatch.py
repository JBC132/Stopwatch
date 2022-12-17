import PySimpleGUI as sg

layout = [
    [sg.Text('time')],
    [sg.Button('Start'), sg.Button('Lap')]
]

window = sg.Window(
    'Stopwatch', 
    layout,
    size = (300,300),
    no_titlebar = True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()