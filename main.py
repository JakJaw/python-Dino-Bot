import pyautogui
from PIL import Image, ImageGrab
import time
import webbrowser

Url = "https://elgoog.im/t-rex/"
Replay = (950, 404)




def click(key):
    pyautogui.keyDown(key)
    time.sleep(0.3)
    pyautogui.keyUp(key)
    return


def Cacti(data):
    for i in range(725, 790):
        for j in range(400, 435):
            if data[i, j] < 100:
                click("up")
                return
    return


if __name__ == "__main__":
    webbrowser.open(Url)
    time.sleep(4)
    click('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        Cacti(data)

        for i in range(725, 780):
            for j in range(400, 435):
                data[i, j] = 0
