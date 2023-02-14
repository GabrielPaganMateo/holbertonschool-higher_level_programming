#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines a square, inherits from
    Rectangle which inherits from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        super(__class__, self.__class__).width.__set__(self, size)
