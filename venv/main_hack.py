from hack import Hack
from time import sleep
from pynput import keyboard
import threading
import sys
from pyautogui import position, moveTo


file = r"C:\Users\Xin\AppData\Local\osu!\Songs\12145 Chemistry - Period\Chemistry - Period (KIA) [Harder].osu"



hack = Hack(file)
t = threading.Thread(target=hack.start)


#### r to record and z to start
started = False

def on_press(key):
    global started
    try:
        if (str(key.char) == 'z' or str(key.char) == 'x'):
            hack.next()
    except:
        pass


listener = keyboard.Listener(
    on_press=on_press)
listener.start()
listener.join()

