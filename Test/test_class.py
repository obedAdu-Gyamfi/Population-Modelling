import unittest
import os, sys

modules_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '~//ProjectWork/New_Project/analysis_data/modules'))
if modules_path not in sys.path:
    sys.path.append(modules_path)

from modules import main 
#from modules import models
class TestDataFunctions(unittest.TestCase):
    def setUp(self):
        self.data1 = [626155, 770087, 1157807, 1924577, 2376021]
        self.data2 = [626155, 923897, 1320474, 1811623, 2367892]
        self.data3 = [626155, 980545, 1393808, 1836394, 2279683]
        return super().setUp()
    def test_take_data(self):
        data = main.take_data(self.data1, self.data2, self.data3)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for item in data:
            self.assertIsInstance(item, int)
    def test_write_data(self):
        main.write_data(self.data1, self.data2, self.data3)
        with open("output.dat", "r") as file:
            lines = file.readlines()
            self.assertTrue(lines[0].startswith("#Year"))
            self.assertEqual(len(lines), 6)
    def test_MSE(self):
        mse_value = main.MSE(self.data1, self.data2)
        self.assertIsInstance(mse_value, float)
        self.assertGreaterEqual(mse_value, 0)
    def test_RMSE(self):
        rmse_value = main.RMSE(self.data1, self.data2)
        self.assertIsInstance(rmse_value, float)
        self.assertGreaterEqual(rmse_value, 0)
    def test_RelativeRMSE(self):
        relative_rmse_value = main.RelativeRMSE(self.data1, self.data2)
        self.assertIsInstance(relative_rmse_value, float)
        self.assertGreaterEqual(relative_rmse_value, 0) 
    

if __name__ == "__main__":
    unittest.main()