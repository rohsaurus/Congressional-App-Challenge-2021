import PySimpleGUI as sg
import cv2
import numpy as np
import os
def main():
    sg.theme("LightGreen")

    # Define the window layout
    layout = [
        [sg.Text("Air Swipe", size=(60, 1), justification="center")],
        [sg.Text(key='-GESTURE-')],
        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Button("Exit", size=(10, 1))],
    ]

    # Create the window and show it without the plot
    window = sg.Window("Air Swipe", layout, location=(800, 400))

    cap = cv2.VideoCapture(0)

    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()
        # window['-GESTURE-'].update("Thumbs up")
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    window.close()

main()
