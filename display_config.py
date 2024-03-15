class DisplayConfig:
    def __init__(self, width, height, color) -> None:
        self._width = width
        self._height = height
        self._color = color

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def heigth(self):
        return self._height
    
    @heigth.setter
    def heigth(self, new_height):
        self._height = new_height

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color