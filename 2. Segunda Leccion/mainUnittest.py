import unittest
from main import Calculator

class CalculatorTestCase(unittest.TestCase):
    
    def setUp(self):
        """First method that is being called when running unittests, instantiates
        the entity for avoiding having to instantiate it for each test."""
        self.calculator = Calculator()

    def test_isDigit(self):
        self.assertTrue(self.calculator.isDigit(1))
        self.assertTrue(self.calculator.isDigit(1.0))
        self.assertFalse(self.calculator.isDigit("NotDigit"))
        self.assertFalse(self.calculator.isDigit(None))

    def test_sum(self):
        self.assertEqual(self.calculator.sum(1, 2, 3), 6.0)
        self.assertEqual(self.calculator.sum(1.0, 2, 3.5), 6.5)
        self.assertEqual(self.calculator.sum(1, 2.3, "NonDigit"), 3.3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(1, 2, 3), 6.0)
        self.assertEqual(self.calculator.multiply(1.0, 2, 3.5), 7.0)
        self.assertEqual(self.calculator.multiply(1, 2.3, "NonDigit"), 2.3)

    def test_elevate(self):
        self.assertEqual(round(self.calculator.elevate(2.2, 2), 2), 4.84)
        self.assertEqual(round(self.calculator.elevate(5, -1), 2), 0.2)
        self.assertIsNone(self.calculator.elevate("NonDigit", 1))
        self.assertIsNone(self.calculator.elevate(1, "NonDigit"))

    def test_divide(self):
        self.assertAlmostEqual(self.calculator.divide(2.5, -3), -0.8333333333333334)
        self.assertIsNone(self.calculator.divide(1, 0))
        self.assertEqual(self.calculator.divide(0, 5), 0.0)
        self.assertIsNone(self.calculator.divide("NonDigit", 1))

if __name__ == '__main__':
    unittest.main()
