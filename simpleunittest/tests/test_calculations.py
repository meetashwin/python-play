import unittest
from simpleunittest.calculations import Calculations

class TestCalculations(unittest.TestCase):
    def test_sum(self):
        calculation = Calculations()
        result = calculation.sum(6, 4)
        self.assertEqual(result, 10, "Should be 10")

    def test_multiply(self):
        calculation = Calculations()
        result = calculation.multiply(6, 4)
        self.assertEqual(result, 24, "Should be 24")

    def test_subtract(self):
        calculation = Calculations()
        result = calculation.subtract(6, 4)
        self.assertEqual(result, 2, "Should be 2")

    def test_divide(self):
        calculation = Calculations()
        result = calculation.divide(6, 4)
        self.assertEqual(result, 1.5, "Should be 1.5")

if __name__ == '__main__':
    unittest.main()