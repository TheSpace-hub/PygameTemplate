"""A scene module with a rocket game.
"""
import os.path
import time
from typing import TYPE_CHECKING
from math import atan2, pi
from random import randint

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
        self.rocket_velocity: Vector2 = Vector2(5, 0)
        self.previous_turn_of_sun: float = 0

    async def boot(self):
        self.add_sprite('sun', Image(self.app, Vector2(904, 484), os.path.join('assets', 'images', 'sun.png'),
                                     (56, 56)))
        self.add_sprite('rocket',
                        Image(self.app, Vector2(400, 100), os.path.join('assets', 'images', 'rocket.png'),
                              (50, 96)))

    async def update(self):
        self.physics()
        self.sun_animation()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.app.quit()

    def physics(self):
        """Calculating physics for a rocket flying around the sun.
        """
        rocket: Image = self.get_sprite('rocket')
        rocket.position += self.rocket_velocity
        rocket.rotate(180 + atan2(self.rocket_velocity[0], self.rocket_velocity[1]) * 180 / pi)

        rocket_center_position: Vector2 = rocket.position + Vector2(rocket.image.get_size()[0] // 2,
                                                                    rocket.image.get_size()[1] // 2)
        self.rocket_velocity += (Vector2(960, 540) - rocket_center_position) * .0001

    def sun_animation(self):
        """Rotates the sun making a kind of animation.
        """
        if time.time() - self.previous_turn_of_sun >= .25:
            sun: Image = self.get_sprite('sun')
            sun.rotate(90 * randint(0, 3))

            self.previous_turn_of_sun = time.time()

    async def enter(self):
        pass

    async def exit(self):
        pass
