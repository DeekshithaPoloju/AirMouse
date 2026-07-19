import pyautogui
import numpy as np
import time

from config import *

pyautogui.FAILSAFE = True


class MouseController:

    def __init__(self):

        self.prev_x = 0
        self.prev_y = 0

        self.last_click = 0
        self.click_delay = 0.35

        self.dragging = False

    def move_mouse(self, x, y):

        screen_x = np.interp(
            x,
            (FRAME_MARGIN, CAMERA_WIDTH - FRAME_MARGIN),
            (0, SCREEN_WIDTH)
        )

        screen_y = np.interp(
            y,
            (FRAME_MARGIN, CAMERA_HEIGHT - FRAME_MARGIN),
            (0, SCREEN_HEIGHT)
        )

        curr_x = self.prev_x + (screen_x - self.prev_x) / SMOOTHENING
        curr_y = self.prev_y + (screen_y - self.prev_y) / SMOOTHENING

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x = curr_x
        self.prev_y = curr_y

    def can_click(self):
        return (time.time() - self.last_click) > self.click_delay

    def update_click_time(self):
        self.last_click = time.time()

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def double_click(self):
        pyautogui.doubleClick()

    def scroll(self, amount):
        pyautogui.scroll(amount)

    def start_drag(self):
        if not self.dragging:
            pyautogui.mouseDown()
            self.dragging = True

    def stop_drag(self):
        if self.dragging:
            pyautogui.mouseUp()
            self.dragging = False
................................................................................................................................................................