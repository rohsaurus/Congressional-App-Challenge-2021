import PySimpleGUI as sg
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import threading
from IPython.display import clear_output
import pyautogui

run = False
model = load_model("Congressional.h5")
output = 0
imageWidth = 150
imageHeight = 150

def modelCode():
    print("In Method")
    global frame, run
    global imageWidth, imageHeight
    global model
    global output
    while True:
        if run:
            print("Inside if statemtn loop")
            run = False
            frame = cv2.resize(frame, (imageWidth, imageHeight))
            frame = np.reshape(frame, (1, imageWidth, imageHeight, 3))
            pred = model.predict(frame)
            output = pred.argmax()
            print("Gathered output")
            #clear_output(wait=True)
            print("1")
            print(output)


x = threading.Thread(target=modelCode)
x.start()


def main():
    sg.theme("LightGreen")
    # Define the window layout
    layout = [
        [sg.Text("Air Swipe", size=(60, 1), justification="center")],
        [sg.Text("Recognized fingers:", key='-GESTURE-')],
        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Button("Exit", size=(10, 1))],
    ]
    # Create the window and show it without the plot
    print("Before window initilizaiton")
    window = sg.Window("Air Swipe", layout, location=(800, 400))
    print ("After window intilizaiton")
    cap = cv2.VideoCapture(0)
    print("After video caputre")
    global frame, run
    global imageWidth, imageHeight
    global model
    global output
    print("Setting up the globals")
    while True:
        print("Before reading window")
        event, values = window.read(timeout=0)
        print("After reading window")
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        ret, frame = cap.read()
        print("Before run = true")
        run = True
        print("After run = true")
        window['-GESTURE-'].update(output)
        if output == 1:
            #pyautogui.press('right')
            print("Ran output version 1")
        if output == 2:
           # pyautogui.press('left')
            print("Ran output version 2")
        if output == 3:
            pyautogui.press('right')
            print("Ran output version 3")
        if output == 4:
            pyautogui.press('right')
            print("Ran output version 4")
        print("About to output video camera")
        #imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        #window["-IMAGE-"].update(data=imgbytes)

    x.join()
    window.close()


# running main function
main()
