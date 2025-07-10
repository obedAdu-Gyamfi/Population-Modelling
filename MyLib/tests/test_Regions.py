#!/usr/bin/python3
"""
This is a test case
"""


import unittest
from Packages import cases as reg


class TestRegions(unittest.TestCase):

    def setUp(self):
        self.p = [626155, 770087, 1157807, 1924577, 2376021]
        self.ex = [626155, 923897, 1320474, 1811623, 2367892]
        self.x = reg.RegionClass(
            self.p,
            5_000_000.0,
            0.1,
            1,
            "verhulst"
            )

        return super().setUp()

    def test_exist(self):
        self.assertIsNotNone(self.x.lmodel())

    #def test_value(self):
    #    self.assertEqual(self.x.lmodel(), self.ex)


if __name__ == "__main__":
    unittest.main()
