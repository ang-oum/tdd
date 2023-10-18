import unittest


def parse_and_validate_input(data):

    # Function to parse and validate input data
    if isinstance(data, str) and data.isnumeric():
        return int(data) > 0
    return False


class TestInputParsing(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_valid_input(self):
        data = "100"
        result = parse_and_validate_input(data)
        self.assertTrue(result)
    
    def test_invalid_input(self):
        data = "Hello"
        result = parse_and_validate_input(data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
