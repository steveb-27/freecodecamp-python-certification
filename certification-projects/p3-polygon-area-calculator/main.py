from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self, ):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return '\n'.join([
            ''.ljust(self.width, '*')
            for line in range(self.height)
        ]) + '\n'

    def get_amount_inside(self, shape):
        across = self.width // shape.width
        adown = self.height // shape.height

        return across * adown


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

        self.height = side
        self.width = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_width(self, value):
        self.set_side(value)

    def set_height(self, value):
        self.set_side(value)

    def set_side(self, value):
        self.width = value
        self.height = value


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))