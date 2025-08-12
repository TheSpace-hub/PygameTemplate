"""The module that adds the wait sprite.
"""
import time
from typing import TYPE_CHECKING
from math import sin, cos

import pygame as pg

from pygame import Vector2

from src.sprite import Sprite

if TYPE_CHECKING:
    from src.app import App


class Waiting(Sprite):
    """Sprite class for waiting for something.

    Attributes:
        done: Loading animation flag.
    """

    def __init__(self, app: 'App', position: Vector2, size: tuple[int, int] | None = None, done: bool = False):
        """Initialization.

        Args:
            app: The main class of the application.
            position: The position of the sprite on the screen.
            size: Sprite scale.
            done: Loading animation flag.
        """
        super().__init__(app, size, position)
        self.done: bool = done

    def update_view(self):
        self.image.fill((32, 32, 32))

        dimensions_of_loading_plate: tuple[float, float] = self.get_dimensions_of_loading_plate()

        pg.draw.line(self.image, (255, 255, 255),
                     [
                         self.image.get_size()[0] * (dimensions_of_loading_plate[0] + 1) / 2,
                         self.image.get_size()[1] / 2
                     ],
                     [
                         self.image.get_size()[0] * (dimensions_of_loading_plate[1] + 1) / 2,
                         self.image.get_size()[1] / 2
                     ], self.image.get_size()[1])

        pg.draw.rect(self.image, (78, 78, 78), pg.Rect(
            0, 0, self.image.get_size()[0], self.image.get_size()[1]
        ), 3)

    async def update(self):
        self.update_view()

    @staticmethod
    def get_dimensions_of_loading_plate() -> tuple[float, float]:
        """Gets the width coordinate [-1; 1] of the animated element depending on the time.

        Returns:
            Tuple with start and end coordinates [-1; 1].
        """
        return sin(time.time() * 1.5), cos(time.time() * 1.5)
