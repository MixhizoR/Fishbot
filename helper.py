from PIL import Image
import keyboard
import time
import pyautogui as pag

while keyboard.is_pressed('t') == False:
    if keyboard.is_pressed('q') == True:
        x,y=pag.position()
        print(f"coords, x={x}, y={y}")
        print(pag.pixel(x,y))
        time.sleep(1)