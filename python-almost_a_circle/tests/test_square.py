from models.square import Square
import unittest

class TestSquare(unittest.TestCase):

    def test_save_to_file_empty(self):
        Square.save_to_file(None)
        with open("Square.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file_empty_2(self):
        Square.save_to_file([])
        with open("Square.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file(self):
        Square.save_to_file([Square(1)])
        result = '[{"id": 25, "x": 0, "size": 1, "y": 0}]'
        with open("Square.json") as fd:
            self.assertEqual(result, fd.read())