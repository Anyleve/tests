import unittest
from square import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_dimensions(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_dimensions(self):
        res_area = area(5)
        res_perimeter = perimeter(5)
        self.assertEqual(res_area, 25)
        self.assertEqual(res_perimeter, 20)

if __name__ == '__main__':
    unittest.main()