import pyautogui
from untils import perform_until_z

def operation():
    pyautogui.click(button='right')
    pyautogui.mouseDown(button='right')

perform_until_z(operation)