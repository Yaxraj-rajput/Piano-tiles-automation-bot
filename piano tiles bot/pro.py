import pyautogui
import time
from mss import mss


# giving axis for starting x point
axisx = 800

# giving axis for starting x point
axisy = 689

bbox = (axisx, axisy, axisx + 300, axisy + 1)

#defines where cursour should move
cords_x = [0, 100, 200, 299]



# to get location of cursour
def print_mouse():
    while True:
        print(pyautogui.position())
        time.sleep(1)



# code to click
def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0) [0] < 100:
                    pyautogui.click(axisx + cord, axisy)
                    break

time.sleep(5)
start()