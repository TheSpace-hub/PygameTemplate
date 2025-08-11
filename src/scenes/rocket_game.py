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
        self.rocket_velocity: Vector2 = Vector2(15, 0)

    async def boot(self):
        self.add_sprite('sun', Image(self.app, Vector2(904, 484), os.path.join('assets', 'images', 'sun.png'),
                                     (56, 56)))
        self.add_sprite('rocket',
                        Image(self.app, Vector2(400, 100), os.path.join('assets', 'images', 'rocket_engine_on.png'),
                              (50, 96)))

    async def update(self):
        self.physics()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.app.quit()

    def physics(self):
        """Calculating physics for a rocket flying around the sun.
        """
        rocket: Image = self.get_sprite('rocket')
        rocket.position += self.rocket_velocity

        rocket_center_position: Vector2 = rocket.position + Vector2(rocket.image.get_size()[0] // 2,
                                                                    rocket.image.get_size()[1] // 2)
        self.rocket_velocity += (Vector2(960, 540) - rocket_center_position) * .0005

    async def enter(self):
        pass

    async def exit(self):
        pass
