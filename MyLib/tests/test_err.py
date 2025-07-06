#!/usr/bin/env python3
"""
This module is a test case unit for the error
analysis functions in the MyLib package.
"""


import unittest
import numpy as np
from Packages import Error_Analysis as e


class TestErrorAnalysis(unittest.TestCase):

    def setUp(self):
        self.data1 = np.array((1, 2, 3))
        self.data2 = np.array((4, 5, 6))
        return super().setUp()

    def test_not__none(self):
        self.assertIsNotNone(e.MSE)
        self.assertIsNotNone(e.RMSE)
        self.assertIsNotNone(e.RelativeRMSE)

    def test_value_error(self):
        self.assertRaises(ValueError, e.MSE, None, self.data2)
        self.assertRaises(ValueError, e.MSE, self.data1, None)
        self.assertRaises(ValueError, e.RMSE, None, self.data2)
        self.assertRaises(ValueError, e.RMSE, self.data1, None)
        self.assertRaises(ValueError, e.RelativeRMSE, None, self.data2)
        self.assertRaises(ValueError, e.RelativeRMSE, self.data1, None)
        self.assertRaises(ValueError, e.MSE, None, None)
        self.assertRaises(ValueError, e.RMSE, None, None)
        self.assertRaises(ValueError, e.RelativeRMSE, None, None)
        self.assertRaises(ValueError, e.MSE, self.data1, self.data2[:2])
        self.assertRaises(ValueError, e.RMSE, self.data1, self.data2[:2])
        self.assertRaises(
            ValueError,
            e.RelativeRMSE,
            self.data1,
            self.data2[:2]
            )
        self.assertRaises(
            ValueError,
            e.MSE,
            self.data1[:2],
            self.data2
            )
        self.assertRaises(
            ValueError,
            e.RMSE,
            self.data1[:2],
            self.data2
            )
        self.assertRaises(
            ValueError,
            e.RelativeRMSE,
            self.data1[:2],
            self.data2
            )

    def test_mse(self):
        self.assertEqual(e.MSE(self.data1, self.data2), 9.0)

    def test_rmse(self):
        self.assertEqual(e.RMSE(self.data1, self.data2), 3.0)

    def test_relative_rmse(self):
        self.assertEqual(e.RelativeRMSE(self.data1, self.data2), 150.0)


if __name__ == "__main__":
    unittest.main()
