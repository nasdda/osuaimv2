from hack import Hack
from time import sleep
from pynput.mouse import Controller
from threading import Thread
import sys
from pynput import keyboard


file = r"C:\Users\Xin\PycharmProjects\osuaim\venv\hitobjects"

mouse = Controller()

hack = Hack(file)
task = Thread(target=hack.start)

started = False

def on_press(key):
    global started
    try:
        if str(key.char) == 'q':
            task.start()
    except:
        pass



listener = keyboard.Listener(
    on_press=on_press)
listener.start()

listener.join()

