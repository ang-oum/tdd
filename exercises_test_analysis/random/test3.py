import unittest

from src.code3 import gcd as this_func


class Code2Test(unittest.TestCase):

    def test_gcd_n_and_0_is_0(self):
        self.assertEqual(this_func(2, 0), 2)

    def test_gcd_0_and_n_is_n(self):
        self.assertEqual(this_func(0, 2), 2)

    def test_n_gcd_12(self):
        self.assertEqual(this_func(206, 40), 2)


if __name__ == "__main__":
    unittest.main()