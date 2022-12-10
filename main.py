from PIL import Image
import keyboard
import mouse
import time
import pyautogui as pag

def mouseclick(x,y): # making own mouse click func because pyautogui's click func too fast for the game
    pag.mouseDown(x,y,'left')
    time.sleep(0.15)
    pag.mouseUp(x,y,'left')

while True:
    if keyboard.is_pressed('k') == True: #getting fishing hole's coords
        fishx,fishy=pag.position()
        mouseclick(fishx,fishy)
        break

while keyboard.is_pressed('q') == False: #when 'q' is, pressed stop the fishbot
    pix1=pag.pixel(959,491) #get colors from coords
    pix2=pag.pixel(959,586)
    if 125 <= pix1[0] <= 145 and 126 <= pix1[1] <= 150 and 148 <= pix1[2] <= 170 and 80 <= pix2[0] <= 120 and 80 <= pix2[1] <= 120 and 80 <= pix2[2] <= 120: #if colors match, click
        mouseclick(960,540)
        time.sleep(1.85)
        mouseclick(fishx,fishy)