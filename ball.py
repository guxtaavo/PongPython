class Ball:
    def __init__(self, surface, color, center, radius) -> None:
        self._surface = surface
        self._color = color
        self._center = center
        self._radius = radius

    @property
    def surface(self):
        return self._surface

    @property
    def color(self):
        return self._color

    @property
    def center(self):
         return self._center

    @center.setter
    def center(self, center):
        self._center = center

    @property
    def radius(self):
        return self._radius
