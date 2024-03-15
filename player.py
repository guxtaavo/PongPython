from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, rect) -> None:
        self._rect = rect
    
    @property
    def rect(self):
        return self._rect

    @abstractmethod
    def movimentar():
        ...