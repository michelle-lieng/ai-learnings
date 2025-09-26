# test 1
# test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(1, 2), 3)
        print("hi")
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertRaises(ValueError, self.calc.divide, 1, 0) # Test for exception