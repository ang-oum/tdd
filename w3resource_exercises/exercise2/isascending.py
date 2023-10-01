import unittest

def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))


class TestSortedAscending(unittest.TestCase):


    def test_sorted_list(self):
        #lst = [5, 7, 2, 8, 1, 9]
        lst = [1, 2, 3, 4, 5, 6, 7]
        print("Sorted list: ",lst)
        self.assertTrue(is_sorted_ascending(lst), "The list is not sorted in ascending order")

    def test_unsorted_list(self):
        #lst = [1, 2, 3]
        lst = [5, 7, 2, 8, 1, 9] 
        print("Unsorted list: ",lst)
        self.assertFalse(is_sorted_ascending(lst), "The list is sorted in ascending order")



if '__name__' =='__main__':
    unittest.main()