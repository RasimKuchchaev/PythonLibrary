# pip install pyautogui
# pip install opencv-python

import pyautogui

path = r'C:\Users\Rasim\PycharmProjects\PythonLibrary\PyAutoGui\ImageClick\image_file\my_comp.PNG'

# button = pyautogui.locateOnScreen(path)
button = pyautogui.locateOnScreen(path, confidence=0.8)     # confidence - точность совпадения max=1
# pyautogui.click(button)
pyautogui.doubleClick(button, interval=0.1)

pyautogui.sleep(5)
path2 = r'C:\Users\Rasim\PycharmProjects\PythonLibrary\PyAutoGui\ImageClick\image_file\diskC.PNG'
button2 = pyautogui.locateOnScreen(path2, confidence=0.95)
pyautogui.doubleClick(button2, interval=0.1)