import pyautogui
import time


def get_cursor_position():
    while True:
        x, y = pyautogui.position()

        print(f"A posição atual do cursor é: X = {x}, Y = {y}")

        time.sleep(1)


if __name__ == "__main__":
    get_cursor_position()
