import unittest
from geometry import rectangle, perimetr

class TestGeometry(unittest.TestCase):

    def testRectangle_regular(self):
        self.assertEqual(rectangle(6, 4), 24)

    def testRectangle_zero(self):
        self.assertEqual(rectangle(6, 0), 0)

    def testRectangle_square(self):
        self.assertEqual(rectangle(6, 6), 36)


    def testPerimetr_regular(self):
        self.assertEqual(perimetr(6, 4), 20)

    def testPerimetr_zero(self):
        self.assertEqual(perimetr(6, 0), 12)

    def testPerimetr_square(self):
        self.assertEqual(perimetr(6, 6), 24)