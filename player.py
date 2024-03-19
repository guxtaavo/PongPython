import pygame
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.height = 70
        self.width = 5
        self.speed = 5
    
    @abstractmethod
    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, 'white', (self.x, self.y, self.width, self.height))