"""A scene module with an intro.
"""
import os.path
from typing import TYPE_CHECKING, Optional
import pygame as pg
from math import sin
import time

from pygame import Vector2

from src.scene import Scene

from src.sprites import Text, Button, InBlockText

if TYPE_CHECKING:
    from src.app import App


class Intro(Scene):
    """A class with an intro.
    """

    def __init__(self, app: 'App'):
        super().__init__(app)

    def boot(self):
        self.app.audio.load_sound('intro', os.path.join('assets', 'sounds', 'intro.wav'))

        self.add_sprite('application_name', Text(self.app, Vector2(960, 540), 'Pygame Application', 48))
        self.add_sprite('tip', Text(self.app, Vector2(960, 600), 'Press any key to quit'))

        self.add_sprite('quit_button',
                        Button(self.app, Vector2(760, 650), (400, 50),
                               InBlockText(self.app, 'Or click on this button'),
                               self._on_quit_button_pressed))

    def update(self):
        self._update_tip_color()

        if True in pg.key.get_pressed():
            self.app.quit()

    def enter(self):
        self.app.audio.play('intro')

    def _update_tip_color(self):
        """Implementation of text flickering.
        """
        tip: Text = self.get_sprite('tip')

        color: tuple[int, int, int] = tuple[int, int, int]([int(155 - (sin(time.time() * 2) * 100))] * 3)

        tip.color = color
        tip.update_view()

    def _on_quit_button_pressed(self, context: Optional[str]):
        """The handler for clicking on the button.
        """
        self.app.quit()

    def exit(self):
        pass
