import time
import pyautogui

i = 160  # ????

time.sleep(1)

while True:
    pyautogui.moveTo(x=1800, y=265)  # altere estes valores rodando o arquivo test.py
    pyautogui.click()
    time.sleep(100)
    pyautogui.moveTo(x=1800, y=265 + i)
    pyautogui.click()
    pyautogui.moveTo(x=1514, y=620)
    pyautogui.click()

    time.sleep(2)
    pyautogui.scroll(-200)
    pyautogui.moveTo(x=1800, y=265 + i)
