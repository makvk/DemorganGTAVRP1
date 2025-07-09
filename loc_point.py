import os
import sys
import cv2
import numpy as np
from mss import mss
import win32api

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def find_point_loc():
    template_path = resource_path(rf"sources/probka.png")
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        raise FileNotFoundError(f"Шаблон не найден: {template_path}")

    while True:
        with mss() as sct:
            monitor = sct.monitors[1]
            box = {"left": monitor["width"] // 3, "top":  0, "width": monitor["width"] // 3, "height": monitor["height"] // 2}

            screenshot = np.array(sct.grab(box))
            screen_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
            result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            if max_val > 0.8:
                x = max(0, max_loc[0] + monitor["width"] // 100)
                y = max(0, max_loc[1] + monitor["height"] * 0.13)
                # current = win32api.GetCursorPos()
                win32api.SetCursorPos((int(monitor["width"] // 3 + x), int(monitor["height"] // 3 + y)))
            else: 
                print("Действе завершено!")
                break
                