import pyautogui
import time
from untils import perform_until_z

up = True

def operation():
    global up

    # mine
    pyautogui.click()
    time.sleep(3)

    # move
    current_x, current_y = pyautogui.position()

    if up:
        move_up_pixels = 80
    else:
        move_up_pixels = -80

    new_x = current_x
    new_y = current_y - move_up_pixels

    pyautogui.moveTo(new_x, new_y)
    up = not up

perform_until_z(operation)

