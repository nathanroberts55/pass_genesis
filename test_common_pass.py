import unittest
import hashlib
from common_pass import get_password, hash_password, check_common_passlist

    """
        Unit Testing Documentation (Real Python): https://realpython.com/python-testing/#writing-your-first-test
        Unit Test Module Documentation          : https://docs.python.org/3/library/unittest.html
    """
class TestCommonPass(unittest.TestCase):
    def test_get_password(self):
        """
        Test that checks that results of passing the valid argument "password123" to the method
        """

        test_pass = "password123"
        result    = get_password()

        self.assertEqual(result, test_pass)
    
    def test_hash_password(self):
        """
        Test to see if the password is hashed properly
        """

        test_password = "password123"

        encoded_password = test_password.encode()
        hashed_password  = hashlib.sha1(encoded_password).hexdigest()
        hash_first_five  = hashed_password[:5]
        rest_of_hash     = hashed_password[5:].upper()
        result           = [test_password, hash_first_five, rest_of_hash]

        self.assertEqual(hash_password(test_password), result)

if __name__ == '__main__':
    unittest.main()