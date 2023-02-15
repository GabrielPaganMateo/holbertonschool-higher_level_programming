import unittest

from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_create(self):
        self.assertTrue(Rectangle.create(**{'id': 89}))
        self.assertEqual(Rectangle.create(**{'id': 89}), Rectangle(id=89))
if __name__ == "__main__":
    TestBase.test_create()
    unittest.main()