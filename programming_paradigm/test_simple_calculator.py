import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(-1, 3), -4)
        self.assertEqual(self.calc.subtract(3, 3), 0)
        # Add more assertions to thoroughly test the add method.
    def test_multiply(self):
        """Test the Multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Add more assertions to thoroughly test the add method.
    def test_division(self):
        """Test the Division method."""
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-1, 0), None)
        # Add more assertions to thoroughly test the add method.    
