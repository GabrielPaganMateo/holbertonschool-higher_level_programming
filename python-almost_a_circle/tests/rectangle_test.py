import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test """
    def Test_width(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.width, 2)

    def