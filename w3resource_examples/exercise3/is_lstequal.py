import unittest

def lists_are_equal(nums1, nums2):
    return nums1 == nums2

class TestListsEquality(unittest.TestCase):

    def test_equal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [10, 20, 30, 40]
        #nums1 = [10, 20, 30, 40]
        #nums2 = [10, 20, 30, 50]
        print("\nEqual list test:\n",nums1,"\n",nums2)
        self.assertTrue(lists_are_equal(nums1, nums2), "The lists are not equal")

    def test_unequal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [30, 20, 10, 40]
        #nums1 = [10, 20, 30, 40]
        #nums2 = [10, 20, 30, 40]
        print("\nUnequal list test:\n",nums1,"\n",nums2)
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are equal")
        
if __name__ == '__main__':
    unittest.main()