"""A scene module with a rocket game.
"""
import os.path
from typing import TYPE_CHECKING
import pygame as pg

from pygame import Vector2

from src.scene import Scene

from src.sprites import Image

if TYPE_CHECKING:
    from src.app import App


class RocketGame(Scene):
    """A class with a rocket game.
    """

    def __init__(self, app: 'App'):
        super().__init__(app)

    async def boot(self):
        self.add_sprite('sun', Image(self.app, Vector2(960, 540), os.path.join('assets', 'images', 'sun.png'),
                                     (56, 56)))
        self.add_sprite('rocket',
                        Image(self.app, Vector2(30, 30), os.path.join('assets', 'images', 'rocket_engine_on.png'),
                              (50, 96)))

    async def update(self):
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.app.quit()

    async def enter(self):
        pass

    async def exit(self):
        pass
