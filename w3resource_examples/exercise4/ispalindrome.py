import unittest

def is_palindrome(string):
    return string == string[::-1]

class TestPalindrome(unittest.TestCase):

    def test_palindrome_string(self):
        #palindrome = "madam"
        palindrome = "hello"
        print("Test palindrome:",palindrome)
        self.assertTrue(is_palindrome(palindrome), "The string is not a palindrome")

    def test_non_palindrome_string(self):
        #non_palindrome = "hello"
        non_palindrome = "madam"
        print("Test non palindrome:",non_palindrome)
        self.assertFalse(is_palindrome(non_palindrome), "The string is a palindrome")
        
if __name__ == '__main__':
    unittest.main()
