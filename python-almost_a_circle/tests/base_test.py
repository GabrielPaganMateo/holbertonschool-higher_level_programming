import unittest

from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_create(self):
        Create_instance = Rectangle.create(**{'id': 89})
        self.assertTrue(Create_instance)

if __name__ == "__main__":
    unittest.main()