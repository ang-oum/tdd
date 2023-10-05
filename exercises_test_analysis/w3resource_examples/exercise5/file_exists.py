import os
import unittest

def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

class TestFileExists(unittest.TestCase):
    
    def test_existing_file(self):
        directory = '/path/txt'
        filename = 'test1.txt'
        self.assertTrue(file_exists(directory, filename), "The file does not exist in the specified directory")

    def test_nonexistent_file(self):
        directory = '/path/txt'
        filename = 'test2.txt'
        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")

if __name__ == '__main__':
    unittest.main()