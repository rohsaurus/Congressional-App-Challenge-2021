import PySimpleGUI as sg
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
import threading
from IPython.display import clear_output

run = False
model = load_model("Congressional.h5")
output = ""


def main():
    print("Before theme initilizaiton")
    sg.theme("LightGreen")
    global frame, run
    global image_width, image_height
    global model
    global output
    print("global var intilization")
    # Define the window layout
    layout = [
        [sg.Text("Air Swipe", size=(60, 1), justification="center")],
        [sg.Text(key='-GESTURE-')],
        [sg.Text('Thumbs Up')],
        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Button("Exit", size=(10, 1))],
    ]
    print("Creating layout")
    # Create the window and show it without the plot
    window = sg.Window("Air Swipe", layout, location=(800, 400))
    print("Making window")
    # initializing thread so one thread doesn't get overwhelmed by ML model and video input
    x = threading.Thread(target=modelCode, daemon=True)
    # running the model code
    x.start()
    cap = cv2.VideoCapture(0)
    print("Start threading and video capture")
    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()
        run = True
        window['-GESTURE-'].update(output)
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
    x.join()
    window.close()


def modelCode():
    print("MAde it to model code method")
    global frame, run
    global image_width, image_height
    global model
    global output
    while True:
        if run:
            run = False
            frame = cv2.resize(frame, (image_width, image_height))
            frame = np.reshape(frame, (1, image_width, image_height, 3))
            pred = model.predict(frame)
            output = pred.argmax()


main()
