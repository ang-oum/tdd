import requests
import unittest
from unittest.mock import patch, Mock


def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/user/{user_id}")
    return response.json()

class TestUserData(unittest.TestCase):


    @patch('requests.get') #given string will be passed/decorated with mock object
    def test_get_user_data(self, mockGet):
        mock_response = Mock()
        response_dict = {'name': 'Bob', 'email': 'bob@protonmail.com'}
        mock_response.json.return_value = response_dict
        #we artificially declare that our response will contain this dict as json response

        mockGet.return_value = mock_response

        user_data = get_user_data(1)
        mockGet.assert_called_with("https://api.example.com/user/1")
        self.assertEqual(user_data, response_dict)

if __name__ == '__main__':
    unittest.main()
