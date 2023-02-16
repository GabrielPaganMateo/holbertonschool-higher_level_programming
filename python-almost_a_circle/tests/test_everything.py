
import unittest
import json

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestEverything(unittest.TestCase):

    """ Testing width conditions """
    def test_width(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.width, 2)
        square = Square(2)
        self.assertEqual(square.size, 2)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-4, 1)
        with self.assertRaises(ValueError):
            square = Square(-7)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_string_width(self):
        with self.assertRaises(TypeError):
            rec = Rectangle("2", 10)

    """ Testing height conditions """
    def test_height(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.height, 4)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 0)

    def test_str_height(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(35, "15")

    """ Testing x conditions """
    def test_x(self):
        rectangle = Rectangle(10, 2, 3, 5)
        self.assertEqual(rectangle.x, 3)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 5, -9)

    def test_x_zero(self):
        rectangle = Rectangle(3, 2, 0, 1)
        self.assertEqual(rectangle.x, 0)

    def test_x_str(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 5, "1")

    """ Testing y conditions """
    def test_y(self):
        rectangle = Rectangle(2, 3, 2, 2)
        self.assertEqual(rectangle.y, 2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 2, 3, -1)

    def test_y_zero(self):
        rectangle = Rectangle(3, 2, 1, 0)
        self.assertEqual(rectangle.y, 0)

    def test_y_str(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 6, 2, "2")

    """ Testing area """
    def test_area(self):
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.area(), 9)

    def test_area_2(self):
        rec = Rectangle(2, 10)
        self.assertEqual(rec.area(), 20)

    def test_area_3(self):
        rec = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rec.area(), 56)

    """ Testing display """

    """ Testing __str__ """
    def test_str_method(self):
        rec = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rec.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    """ Testing update method """
    def test_update(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(rec.id, 89)
        rec.update(89, 2)
        self.assertEqual(rec.width, 2)
        rec.update(89, 2, 3)
        self.assertEqual(rec.height, 3)
        rec.update(89, 2, 3, 4)
        self.assertEqual(rec.x, 4)
        rec.update(89, 2, 3, 4, 5)
        self.assertEqual(rec.y, 5)

    """  Testing to_dictionary method """
    def test_to_dictionary(self):
        rec = Rectangle(10, 2, 1, 9, 9)
        result = {'x': 1, 'y': 9, 'id': 9, 'height': 2, 'width': 10}
        self.assertDictEqual(rec.to_dictionary(), result)

    """  Testing create method """
    def test_create(self):
        Base_obj = Base(89)
        Rect_obj = Rectangle.create(**{'id': 89})
        self.assertIsNot(Base_obj, Rect_obj)

    """  Testing display method"""

    """ Testing Base for ID"""
    def test_ID(self):
        object_1 = Base()
        self.assertEqual(object_1._Base__nb_objects, 1)
        object_2 = Base()
        self.assertEqual(object_2._Base__nb_objects, 2)

    def test_json_string(self):
        None_list = Base.to_json_string(None)
        self.assertEqual(None_list, '[]')
        empty_list = Base.to_json_string([])
        self.assertEqual(empty_list, '[]')

    def test_from_json_string(self):
        None_list = Base.from_json_string(None)
        self.assertEqual(None_list, [])
        empty_list = Base.to_json_string("[]")
        self.assertEqual(empty_list, '"[]"')

    """Testing save to file"""
    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            self.assertEqual('[]', file.read())
