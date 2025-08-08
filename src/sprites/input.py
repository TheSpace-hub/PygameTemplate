from typing import TYPE_CHECKING, Optional
from enum import Enum

import pygame as pg
from pygame import Vector2

from src.sprites import TextSettings, InBlockText

from src.sprite import Sprite

if TYPE_CHECKING:
    from src.app import App


class InputFormatting(Enum):
    NO_FORMATTING = 0
    ONLY_DIGITS = 1
    NORMALIZED = 2
    IP_V4 = 3


class Input(Sprite):
    def __init__(self, app: 'App', position: Vector2, size: tuple[int, int], text: TextSettings,
                 placeholder: Optional[InBlockText], formatting: InputFormatting = InputFormatting.NO_FORMATTING,
                 limit: int = 0,
                 disabled: bool = False):
        super().__init__(app, size, position)
        self.text: TextSettings = text
        self.placeholder: Optional[InBlockText] = placeholder

        self.limit: int = limit
        self.formatting: InputFormatting = formatting
        self.disabled: bool = disabled

        self.selected: bool = False

        text.correct_position(size)
        placeholder.correct_position(size)

        self.update_view()

    def update_view(self):
        self.image.fill((58, 58, 58) if self.selected or self.disabled else (32, 32, 32))

        self.image.blit(self.placeholder.image if self.text.text == '' else self.text.image, self.placeholder.position)

        pg.draw.rect(self.image, (78, 78, 78), pg.Rect(
            0, 0, self.image.get_size()[0], self.image.get_size()[1]
        ), 3)

    def update(self):
        if 1 in self.app.omitted_mouse_buttons:
            self.selected = (self.position.x <= pg.mouse.get_pos()[0] <= self.position.x + self.image.get_size()[0] and
                             self.position.y <= pg.mouse.get_pos()[1] <= self.position.y + self.image.get_size()[1])
            self.update_view()
