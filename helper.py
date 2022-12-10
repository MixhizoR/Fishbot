from PIL import Image
import keyboard
import time
import pyautogui as pag

while keyboard.is_pressed('t') == False:
    if keyboard.is_pressed('q') == True:
        print(pag.pixel(959,491))
        time.sleep(1)