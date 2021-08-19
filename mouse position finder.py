x=0
try:
 import mouse
except ImportError:
 import os
 print("wait for mouse to get installed, then try running this program again")
 os.system("pip install mouse")
 x+=1
try:
 import keyboard
except ImportError:
 import os
 print("Wait for keyboard to get installed, then try running this program again.")
 os.system("pip install keyboard")
 x+=1
if x>0:
   exit()
else:
 print("press ctrl to get current position of the pointer. press / to exit.")
 keyboard.add_hotkey('ctrl', lambda: print(mouse.get_position()))
 keyboard.wait("/")
