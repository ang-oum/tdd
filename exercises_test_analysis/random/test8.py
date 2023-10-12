import unittest

from code8 import sameparity as this_func


class Code8Test(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(this_func([]), [])

    def test_single_element(self):
        self.assertEqual(this_func([1]), [1])

    def test_odd_elements(self):
        self.assertEqual(this_func([1, 2, 3, 4, 5, 6, 7, 8]), [1, 3, 5, 7])

    def test_even_elements(self):
        self.assertEqual(this_func([2, 3, 4, 5, 6, 7, 8]), [2, 4, 6, 8])

    def test_list_of_zeros(self):
        self.assertEqual(this_func([0, 0, 0, 0]), [0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()