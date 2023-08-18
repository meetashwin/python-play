import unittest
from calculations import Calculations

class TestCalculations(unittest.TestCase):
    def test_sum(self):
        """
        Test the sum method of the Calculations class.
        """
        calculation = Calculations()
        result = calculation.sum(6, 4)
        self.assertEqual(result, 10, "Should be 10")

    def test_multiply(self):
        """
        Test the multiply method of the Calculations class.
        """
        calculation = Calculations()
        result = calculation.multiply(6, 4)
        self.assertEqual(result, 24, "Should be 24")

    def test_subtract(self):
        """
        Test the subtract method of the Calculations class.
        """
        calculation = Calculations()
        result = calculation.subtract(6, 4)
        self.assertEqual(result, 2, "Should be 2")

    def test_divide(self):
        """
        Test the divide method of the Calculations class.
        """
        calculation = Calculations()
        result = calculation.divide(6, 4)
        self.assertEqual(result, 1.5, "Should be 1.5")

if __name__ == '__main__':
    unittest.main()