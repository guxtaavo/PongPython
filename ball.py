import pygame
from display_config import DisplayConfig
from random import randint

class Ball:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self._color = 'blue'
        self._width = 30
        self._height = 30

    def update(self):
        ...

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))