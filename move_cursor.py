# move_cursor.py = Moves mouse's cursor periodicaly.
import pyautogui


for x in range(1, 10):
    pyautogui.move(100, 0, duration=0.25) # right 
    pyautogui.sleep(5)
    pyautogui.move(0, 100, duration=0.25) # down
    pyautogui.sleep(5)
    pyautogui.move(-100, 0, duration=0.25) # left 
    pyautogui.sleep(5)
    pyautogui.move(0, -100, duration=0.25) # up
    pyautogui.sleep(5)
