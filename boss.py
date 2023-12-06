import pyautogui

import time

time.sleep(3)
iter = 1

while True:
  iter += 1
  if iter % 100 == 0: print(iter)

  # Starts fighting boss
  pyautogui.keyDown('e')
  time.sleep(0.8)
  pyautogui.keyDown('e')
  pyautogui.click()
 
  # Starts clicking 50 times with 20 millis delay
  for i in range(35):
    pyautogui.click()
    time.sleep(0.02)
    # if i % 10 == 0: print(i)

  time.sleep(1)
  '''
  pyautogui.click()
  time.sleep(4)
  '''



