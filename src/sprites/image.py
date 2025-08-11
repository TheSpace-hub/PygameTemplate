"""The module that adds the image.
"""
from typing import TYPE_CHECKING, Self

import pygame as pg
from pygame import Vector2

from src.sprite import Sprite

if TYPE_CHECKING:
    from src.app import App


class Image(Sprite):
    """Sprite class for loading and displaying images.
    """

    def __init__(self, app: 'App', position: Vector2, path: str, scale: tuple[int, int] | None = None):
        super().__init__(app, (0, 0), position)
        self.image = pg.image.load(path)

        if scale is not None:
            self.change_scale(scale)

    def change_scale(self, scale: tuple[int, int]) -> Self:
        """Change the image scale.

        Args:
            scale: New image scale.

        Returns:
            The image itself.
        """
        self.image = pg.transform.scale(self.image, scale)
        return self

    def flip(self, x: bool, y: bool) -> Self:
        """Flip the image.

        Args:
            x: Reflect the image on the x-axis
            y: Reflect the image on the y-axis

        Returns:
            The image itself.
        """
        self.image = pg.transform.flip(self.image, x, y)
        return self

    def rotate(self, angle: float) -> Self:
        """Flip the image.

        Args:
            angle: Angle of rotation in degrees.

        Returns:
            The image itself.
        """
        self.image = pg.transform.rotate(self.image, angle)
        return self

    async def update_view(self):
        pass

    async def update(self):
        pass
