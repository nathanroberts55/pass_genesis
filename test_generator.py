import unittest
from generator import get_password_length, password_combination_choice, password_generator

class TestGenerator(unittest.TestCase):
    def test_default_length(self):
        """
        Test password length collection method. Enter nothing and the result should be 8
        """
        print(" ")
        print("Please Enter NO VALUE")
        self.assertEqual(get_password_length(), 8)

    def test_length_twelve(self):
        """
        Test password length collection method. Enter 12 and the result should be 12
        """
        
        print(" ")
        print("Please Enter 12")
        self.assertEqual(get_password_length(), 12)

    
    def test_length_string(self):
        """
        Test password length collection method. Enter any string, 
        """

        print(" ")
        print("Please Enter STRING VALUE")
        self.assertEqual(get_password_length(), 8)


if __name__ == '__main__':
    unittest.main()