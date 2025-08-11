"""A module for working with lag machine.

The lag machine calculates the pi number, and updates each frame, which heavily loads the application.
"""
from typing import TYPE_CHECKING

from pygame import Vector2

from src.sprite import Sprite

if TYPE_CHECKING:
    from src.app import App


class LagMachine(Sprite):
    """The class responsible for the lag machine.
    """

    def __init__(self, app: 'App', position: Vector2):
        """Initialization.

        Args:
            app: The main class of the application.
            position: The position of the sprite on the screen.
        """
        super().__init__(app, (50, 50), position)

    def update_view(self):
        pass

    async def update(self):
        pass
