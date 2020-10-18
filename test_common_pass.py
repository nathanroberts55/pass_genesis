import unittest
import hashlib
from unittest.mock import patch
from common_pass import get_password, hash_password, check_common_passlist

"""
    Unit Testing Documentation (Real Python): https://realpython.com/python-testing/#writing-your-first-test
    Unit Test Module Documentation          : https://docs.python.org/3/library/unittest.html
"""


class TestCommonPass(unittest.TestCase):
    """
        Test that checks that results of passing the valid argument "password123" to the method
    Args:
        test_get_password ([string]): simulating the raw input of entering "password123"
    """
    @patch('builtins.input', return_value="password123")
    def test_get_password(self, input):
        self.assertEqual(get_password(), "password123")
        
    """
    Test to see if the password is hashed properly
    """
    def test_hash_password(self):
        

        test_password = "password123"

        encoded_password = test_password.encode()
        hashed_password = hashlib.sha1(encoded_password).hexdigest()
        hash_first_five = hashed_password[:5]
        rest_of_hash = hashed_password[5:].upper()
        result = [test_password, hash_first_five, rest_of_hash]

        self.assertEqual(hash_password(test_password), result)


if __name__ == '__main__':
    unittest.main()
