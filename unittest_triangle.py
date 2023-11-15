import unittest
from triangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_dimensions(self):
        res_area = area(0, 0)
        res_perimeter = perimeter(0, 0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_dimensions(self):
        res_area = area(5, 6)
        res_perimeter = perimeter(5,6, 7)
        self.assertEqual(res_area, 15.0)
        self.assertEqual(res_perimeter, 18)

if __name__ == '__main__':
    unittest.main()