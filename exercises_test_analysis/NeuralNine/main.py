import myfunctions
import unittest
#import pycharm

class TestMultiply(unittest.TestCase):

    def test_with_two_positives(self):
        self.assertEqual(myfunctions.multiply_with_loop(17,19), 17 * 19)
        self.assertEqual(myfunctions.multiply_with_loop(183457,182359), 183457 * 182359)
        self.assertEqual(myfunctions.multiply_with_loop(1,2),2)

    def test_with_one_zero(self):
        self.assertEqual(myfunctions.multuply_With_loop(17,0), 0)
        self.assertEqual(myfunctions.multuply_With_loop(0,17), 0)

    def test_with_two_zeroes(self):
        self.assertEqual(myfunctions.multuply_With_loop(0,0),0)
    
    def test_with_one_negative(self):
        self.assertEqual(myfunctions.multuply_With_loop(17,-19), 17 * (-19))
        self.assertEqual(myfunctions.multiply_with_loop(-19,17), (-19)*17)
    
    def test_with_two_negatives(self):
        self.assertEqual(myfunctions.multuply_With_loop(-17, -19), 17 * 19)

if __name__ == "__main__":
    unittest.main()
