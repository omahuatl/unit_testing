import unittest
from cuboid_volume import *

"""
Created on May 9th 2022
@author: OAMA

to test, run the file as script:  c:>  python -m unittest test_cuboid_volume.py

unittest documentation: https://docs.python.org/3/library/unittest.html
or use pydoc
c:> python -m pydoc unittest.TestCase.assertCountEqual

"""

class TestCuboId(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2), 8)
        self.assertAlmostEqual(cuboid_volume(1), 1)
        self.assertAlmostEqual(cuboid_volume(0), 0)
        self.assertAlmostEqual(cuboid_volume(5.5), 166.375)

    def test_input_values(self):
        self.assertRaises(TypeError, cuboid_volume,True)


