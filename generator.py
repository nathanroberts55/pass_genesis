"""
Author: Nate Roberts
Created: September 5, 2020
"""

import random
import string

# TODO: Create variables to store Alphabet in Upper and Lower case, numbers, and special characters
LETTERS = string.ascii_letters     # Contains letters a-z and A-Z
NUMBERS = string.digits            # Contains numbers 0-9
SPECIAL_CHARS = '!@#$%&*?+'


# TODO: Let the user decide the strength of the password (i.e length, alphanumberic, special characters or not)
# TODO: Create variable to hold the combination of letters and numbers

def get_password_length():
    """Function to get the desired password length from the user

    Returns:
        int : Desired length of the password
    """
    
    length = str(input('How long would should the password be?: ')).strip(" ")

    try:
        return int(length)
    except ValueError as e:
        print('No value was entered so the default length will be set to 8')
        print('If password requirement requires length greater than 8 please restart program and enter desired password length')
        return 8


def password_combination_choice():
    """Collects the users desired complexity for the password

    Returns:
        List: contains the boolean values for the whether the users wants letters, numbers, and speical characters
              auto defaults to all true is user input is invalid
    """

    want_letters = str(
        input('Would you like to use letters? (True pr False): '))
    want_numbers = str(
        input('Would you like to use numbers? (True pr False): '))
    want_punct = str(
        input('Would you like to use special characters? (True pr False): '))

    try:
        want_letters = eval(want_letters.title())
        want_numbers = eval(want_numbers.title())
        want_punct = eval(want_punct.title())

        return [want_letters, want_numbers, want_punct]

    except SyntaxError as s:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will generate a password with all available options')

        return [True, True, True]

    except NameError as e:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will generate a password with all available options')

        return [True, True, True]


def get_string_constants(choice_list):
    """[summary]

    Args:
        choice_list (list): Contains the list of password complexity boolean values colelcted in the password_combination_choice method

    Returns:
        string_constant (string): contains a string with all of the potentials values that can be used to create the users password.
    """

    string_constant = ''
    string_constant += LETTERS if choice_list[0] else ''
    string_constant += NUMBERS if choice_list[1] else ''
    string_constant += SPECIAL_CHARS if choice_list[2] else ''

    return string_constant


def password_generator(cbl, length=8):
    """[summary]

    Args:
        cbl (list): Contains the list of password complexity boolean values colelcted in the password_combination_choice method
        length (int, optional): User defined length of the password desired. Defaults to 8.

    Returns:
        random_password (string): random password of desired length and complexity 
    """

    printable = get_string_constants(cbl)

    printable = list(printable)
    random.shuffle(printable)

    try:
        random_password = random.choices(printable, k=length)
        random_password = ''.join(random_password)

        return random_password
    except IndexError as i:
        print('''You have selected to make a password with no letters, numbers or special characters which is not possible. Please restart the program and select to use at LEAST one of the complexity options''')


if __name__ == '__main__':
    length      = get_password_length()
    choice_list = password_combination_choice()
    password    = password_generator(choice_list, length)
    print(password)
