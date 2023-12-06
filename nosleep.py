import pyautogui

import time

iter = 1

while True:
  iter += 1
  if iter % 1000 == 0: print(iter)

  pyautogui.keyDown('e')
  pyautogui.click()
  time.sleep(4)



