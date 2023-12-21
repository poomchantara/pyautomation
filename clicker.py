import pyautogui
import time
import keyboard

try:
    while True:
        pyautogui.click()
        time.sleep(1)
        if keyboard.is_pressed('z'):
            break
except KeyboardInterrupt:
    pass