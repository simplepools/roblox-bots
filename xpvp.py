import pyautogui
import time
from datetime import datetime
import sys

if sys.argv[3] != 'hit' and sys.argv[3] != 'boss':
  sys.exit('argv[3] should be hit or boss')
till_next_pvp = 60*int(sys.argv[1])

pvp_player_pos = int(sys.argv[2])

print('till next pvp seconds: ' + str(till_next_pvp))

def click(x,y):
  pyautogui.click((x,y))
  time.sleep(1)

def claimgift():
  click(1177,340)
  click(730, 257)
  click(817, 270)
  click(929, 277)
  click(1032, 273)
  click(730, 349)
  click(836, 339)
  click(928, 341)
  click(1047, 340)
  click(721, 417)
  click(823, 417)
  click(935, 416)
  click(1041, 412)
  click(828,417)
  click(1110,215)
  
def hit(secs):
  for i in range(secs):
    time.sleep(1)
    pyautogui.click()

def boss(secs):
  start = time.time()
  while time.time() - start < secs:
   # Starts fighting boss
   pyautogui.keyDown('e')
   time.sleep(0.8)
   pyautogui.keyDown('e')
   time.sleep(1)
   click(1056, 408)
   time.sleep(0.3)
   # Starts clicking 50 times with 20 millis delay
   for i in range(35):
    pyautogui.click()
    time.sleep(0.02)
    # if i % 10 == 0: print(i)
   time.sleep(1)

def smart_delay(secs):
  if sys.argv[3] == 'hit':
    hit(secs)
  else:
    boss(secs)

pvp_pos=(551, 375)
fight_positions=[(939, 319),(935,355),(936,397)]
fight_pos=fight_positions[pvp_player_pos]
ok_pos=(856,425)
x_pos=(984,246)
autotrain_pos=(1112,372)
empty_pos=(955,372)

time.sleep(3)

print('start at', datetime.now())

pvpiter=1

def pvp():
  global pvpiter
  print('enter pvp at ', datetime.now())
  pyautogui.click(pvp_pos)
  for i in range(11):
   print('pvp ',i,datetime.now())
   time.sleep(2)
   pyautogui.click(fight_pos)
   time.sleep(0.7)
   for i in range(50):
    pyautogui.click()
    time.sleep(0.2)
   time.sleep(3)
   pvpiter += 1
   pyautogui.click(ok_pos)
   time.sleep(2)
  pyautogui.click(x_pos)
  time.sleep(2)
  claimgift()

smart_delay(till_next_pvp)
iteration = 1

while True:
   time.sleep(3)
   pvp()
   time.sleep(2)
   pyautogui.click(autotrain_pos)
   time.sleep(1)
   print('iteration',iteration,datetime.now())
   iteration += 1
   pyautogui.click(empty_pos)
   smart_delay(37*60)
   time.sleep(3)
