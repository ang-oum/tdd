# https://www.youtube.com/watch?v=UL0opWf3DeM

import myfunctions
import unittest
#import pycharm
'''
class TestMultiply(unittest.TestCase):

    def test_with_two_positives(self):
        self.assertEqual(myfunctions.multiply_with_loop(17,19), 17 * 19)
        self.assertEqual(myfunctions.multiply_with_loop(183457,182359), 183457 * 182359)
        self.assertEqual(myfunctions.multiply_with_loop(1,2),2)

    def test_with_one_zero(self):
        self.assertEqual(myfunctions.multiply_with_loop(17,0), 0)
        self.assertEqual(myfunctions.multiply_with_loop(0,17), 0)

    def test_with_two_zeroes(self):
        self.assertEqual(myfunctions.multiply_with_loop(0,0),0)
    
    def test_with_one_negative(self):
        self.assertEqual(myfunctions.multiply_with_loop(17,-19), 17 * (-19))
        self.assertEqual(myfunctions.multiply_with_loop(-19,17), (-19)*17)
    
    def test_with_two_negatives(self):
        self.assertEqual(myfunctions.multiply_with_loop(-17, -19), 17 * 19)

    ######################################################################################
        
'''

class TestMultiplyBetter(unittest.TestCase):

    def test_with_two_positives(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(17,19), 17 * 19)
        self.assertEqual(myfunctions.multiply_with_loop_better(183457,182359), 183457 * 182359)
        self.assertEqual(myfunctions.multiply_with_loop_better(1,2),2)

    def test_with_one_zero(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(17,0), 0)
        self.assertEqual(myfunctions.multiply_with_loop_better(0,17), 0)

    def test_with_two_zeroes(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(0,0),0)
    
    def test_with_one_negative(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(17,-19), 17 * (-19))
        self.assertEqual(myfunctions.multiply_with_loop_better(-19,17), (-19)*17)
    
    def test_with_two_negatives(self):
        self.assertEqual(myfunctions.multiply_with_loop_better(-17, -19), 17 * 19)



class TestIntLength(unittest.TestCase):

    def test_with_positive_integer(self):
        self.assertEqual(myfunctions.length_of_integer(987235), 6)
        self.assertEqual(myfunctions.length_of_integer(1), 1)
        self.assertEqual(myfunctions.length_of_integer(10), 2)

    def test_with_negative_integer(self):
        self.assertEqual(myfunctions.length_of_integer(-134), 4)
        self.assertEqual(myfunctions.length_of_integer(-1), 42)
        self.assertEqual(myfunctions.length_of_integer(-134746), 7)

    def test_with_zero(self):
        self.assertEqual(myfunctions.length_of_integer(0), 1)

    def test_with_invalid_type(self):
        self.assertRaises(TypeError, myfunctions.length_of_integer, "18376")
        self.assertRaises(TypeError, myfunctions.length_of_integer, "Hello")
        self.assertRaises(TypeError, myfunctions.length_of_integer, True)
        self.assertRaises(TypeError, myfunctions.length_of_integer, 183.7676)
        self.assertRaises(TypeError, myfunctions.length_of_integer, [1,2,3,4])
    # self.assertRaises(TypeError, myfunctions.length_of_integer, True)
    # AssertionError: TypeError not raised by length_of_integer

if __name__ == "__main__":
    unittest.main()
