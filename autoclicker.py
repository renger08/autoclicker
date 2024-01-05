from pynput import keyboard
from pynput.mouse import Controller, Button
import time
import threading
import os

Clicking = False
mouse = Controller()
# Toggle_Key = keyboard.Key.f6
print("Starting Service...")

def clicker():
    while True:
        if Clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.35)
        # 0.35 => 3 CPS  |  0.00001 => 130 ~ 167 CPS


def on_activate():
    global Clicking
    Clicking = not Clicking
    if Clicking == False:
        print("Disable")
    else:
        print("Enable")
    # print(Clicking)


def stop_script():
    print("Exiting program...")
    os._exit(0)


click_thread = threading.Thread(target=clicker)
click_thread.start()

# hotkey = keyboard.HotKey( keyboard.HotKey.parse('<ctrl>+q'),on_activate)
# exit_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+w'), stop_script)
# with keyboard.Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)) as l:
#     l.join()

with keyboard.GlobalHotKeys({
        '<alt>+q': on_activate,
        '<alt>+r': stop_script}) as h:
    h.join()