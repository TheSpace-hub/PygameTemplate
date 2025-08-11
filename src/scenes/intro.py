"""A scene module with an intro.
"""
from typing import TYPE_CHECKING, Optional
import pygame as pg
from math import sin
import time

from pygame import Vector2

from src.scene import Scene

from src.sprites import Text, LagMachine

if TYPE_CHECKING:
    from src.app import App


class Intro(Scene):
    """A class with an intro.
    """

    def __init__(self, app: 'App'):
        super().__init__(app)

    def boot(self):
        for i in range(1):
            self.add_sprite(f'lag_machine_{i}', LagMachine(self.app, Vector2(30 * i, 0)))

    def update(self):
        if True in pg.key.get_pressed():
            self.app.quit()

    def enter(self):
        self.app.audio.play('intro')

    def exit(self):
        pass
