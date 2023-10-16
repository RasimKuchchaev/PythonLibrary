# pip install keyboard
# pip install pyautogui
# pip install opencv-python

import keyboard
import pyautogui
import os

files = os.listdir('C:\\Users\\Rasim\\PycharmProjects\\PythonLibrary\\PyAutoGui\\ImageClick\\image_file2')

while keyboard.is_pressed('Esc') == False:      # удержание клавиши ESC
    for f in files:
        picture = 'C:\\Users\Rasim\\PycharmProjects\\PythonLibrary\\PyAutoGui\\ImageClick\\image_file2\\' + f

        button = pyautogui.locateOnScreen(picture, confidence=0.9)

        if button:
            pyautogui.click(button)
            # pyautogui.click(button, button='SECONDARY')     # клик правой кнопкой мыши
            # pyautogui.moveTo(10, 10)        # перемещение по координатам
            pyautogui.sleep(1)