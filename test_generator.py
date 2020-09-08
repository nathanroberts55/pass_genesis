import unittest
from generator import get_password_length, password_combination_choice, password_generator

    """
        Unit Testing Documentation (Real Python): https://realpython.com/python-testing/#writing-your-first-test
        Unit Test Module Documentation          : https://docs.python.org/3/library/unittest.html
    """
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

    def test_combo_default_invalid(self):
        """
        Test the combination choice method. enter invalid data to get all TRUE output
        """
        print(" ")
        print("Please Enter NON TRUE/FALSE VALUES")
        self.assertEqual(password_combination_choice(), [True, True, True])

    def test_combo_default_empty(self):
        """
        Test the combination choice method. no entries (" ") to get all TRUE output
        """
        print(" ")
        print("Please Enter NO VALUES")
        self.assertEqual(password_combination_choice(), [True, True, True])

    def test_combo_one_invalid(self):
        """
        Test the combination choice method. enter one invalid entry to get all TRUE output
        """
        print(" ")
        print("Please Enter ONE INVALID ENTRY")
        self.assertEqual(password_combination_choice(), [True, True, True])    

    def test_passgen_NONE(self):
        """
        Should return message asking to restart program and value of none
        """
        default_length = 12
        all_false      = [False, False, False]

        self.assertEqual(password_generator(all_false, default_length),  None)




if __name__ == '__main__':
    unittest.main()