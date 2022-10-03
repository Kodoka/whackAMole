import pyautogui
import time

while True:
    locs = pyautogui.locateAllOnScreen('assets\\logoc.png')
    for loc in locs:
        pyautogui.moveTo(loc, _pause = False)
        pyautogui.click(_pause = 0.01)