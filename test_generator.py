import unittest
from unittest.mock import patch
from generator import get_password_length, password_combination_choice, password_generator

"""
    Unit Testing Documentation (Real Python): https://realpython.com/python-testing/#writing-your-first-test
    Unit Test Module Documentation          : https://docs.python.org/3/library/unittest.html
"""


class TestGenerator(unittest.TestCase):
    """Test password length collection method. Enter nothing and the result should be 8

    Args:
        unittest ([type]): [description]

    Returns:
        [type]: [description]
    """
    @patch('builtins.input', return_value="")
    def test_default_length(self, input):
        self.assertEqual(get_password_length(), 8)

    """
    Test password length collection method. Enter 12 and the result should be 12

    Returns:
        [type]: [description]
    """
    @patch('builtins.input', return_value="12")
    def test_length_twelve(self, input):
        self.assertEqual(get_password_length(), 12)

    """
    Test password length collection method. Enter any string,

    Returns:
        [type]: [description]
    """
    @patch('builtins.input', return_value="8")
    def test_length_string(self, input):
        self.assertEqual(get_password_length(), 8)

        
    """
    Test the combination choice method. enter invalid data to get all TRUE output
    """
    @patch('builtins.input', side_effect=["h", "e", "w"])
    def test_combo_default_invalid(self, input):
        self.assertEqual(password_combination_choice(), [True, True, True])

        
    """
    Test the combination choice method. no entries (" ") to get all TRUE output
    """
    @patch('builtins.input', side_effect=["", "", ""])
    def test_combo_default_empty(self, input):
        self.assertEqual(password_combination_choice(), [True, True, True])

    
    """
    Test the combination choice method. enter one invalid entry to get all TRUE output
    """
    @patch('builtins.input', side_effect=["True", "Nope", "True"])
    def test_combo_one_invalid(self, input):
        self.assertEqual(password_combination_choice(), [True, True, True])

    """
    Should return message asking to restart program and value of none
    """
    def test_passgen_NONE(self):
        default_length = 12
        all_false = [False, False, False]

        self.assertEqual(password_generator(all_false, default_length),  None)


if __name__ == '__main__':
    unittest.main()
