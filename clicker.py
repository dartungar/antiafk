from typing import Tuple
import pyautogui
import random


class Clicker:
    interval_seconds: int = 10
    screen_size: Tuple
    border_px: int = 10

    def __init__(self) -> None:
        self.screen_size = pyautogui.size()
        pyautogui.FAILSAFE = True

    def run(self) -> None:
        while True:
            mouse_position = self.get_random_point_on_screen()
            pyautogui.moveTo(mouse_position)
            pyautogui.leftClick()
            pyautogui.sleep(self.interval_seconds)

    def get_random_point_on_screen(self) -> tuple:
        x = random.randint(
            self.border_px, self.screen_size[0] - self.border_px)
        y = random.randint(
            self.border_px, self.screen_size[1] - self.border_px)
        return (x, y)
