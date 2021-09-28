import pyautogui
import keyboard
import time

on = False

# loop
while True:
    # esc exit
    if keyboard.is_pressed('esc'):
        exit()

    # c key off to on
    if keyboard.is_pressed('c') and on==False:
        on = True

    # autoclicker active
    while on:
        pyautogui.click(pyautogui.position(), clicks=10)

        # v to off
        if keyboard.is_pressed('v'):
            on = False
            
        # esc exit
        if keyboard.is_pressed('esc'):
            exit()
    
    time.sleep(0.2)