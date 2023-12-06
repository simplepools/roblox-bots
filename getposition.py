import pyautogui
import time

for i in range(12):
 time.sleep(3)
 pos = pyautogui.position()
 print(' click({0}, {1}).'.format(pos[0], pos[1]))

