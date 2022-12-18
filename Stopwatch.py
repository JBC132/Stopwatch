import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key = '-CLOSE-')],
    [sg.VPush()],
    [sg.Text('time', font='Young 50', key='-TIME-')],
    [
        sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width=0, key='-STARTSTOP-'), 
        sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width=0, key='-LAP-')]
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