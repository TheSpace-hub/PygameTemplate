"""The module that adds the wait sprite.
"""
from typing import TYPE_CHECKING

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

        pg.draw.rect(self.image, (78, 78, 78), pg.Rect(
            0, 0, self.image.get_size()[0], self.image.get_size()[1]
        ), 3)

    async def update(self):
        self.update_view()
