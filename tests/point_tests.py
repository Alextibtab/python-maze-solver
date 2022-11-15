import unittest

from maze_solver.graphics import Point

class Tests(unittest.TestCase):
    def test_points(self):
        point = Point(2, 5)
        self.assertEqual(point.get_x(), 2)
        self.assertEqual(point.get_y(), 5)