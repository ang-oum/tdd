import unittest

class TestFloatingPointCalculations(unittest.TestCase):
    
    def test_addition(self):
        result = 0.3 + 0.5
        self.assertAlmostEqual(result, 0.8, places=6)

    def test_multiplication(self):
        result = 0.3 * 0.5
        self.assertAlmostEqual(result, .15, places=6)

    def test_division(self):
        result = 0.7 / 0.3
        self.assertAlmostEqual(result, 2.333333, places=6)

if __name__ == '__main__':
    unittest.main()
