import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_save_to_file(self):
        Rectangle.save_to_file(None)