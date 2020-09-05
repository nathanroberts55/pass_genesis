"""
Tool created to help user generate strong passwords
"""
from random import *
import string

#TODO: Create variables to store Alphabet in Upper and Lower case, numbers, and special characters
letters = string.ascii_letters
numbers = string.digits
special_chars = '!@#$%&*?+'

      
#TODO: Let the user decide the strength of the password (i.e length, alphanumberic, special characters or not)
#TODO: Create variable to hold the combination of letters and numbers
def get_passwprd_length():
        length = str(input('How long would should the password be?: ')).strip(" ")
        return int(length)

def password_combination_choice():
    want_letters = str(input('Would you like to use letters? (True pr False): '))
    want_numbers = str(input('Would you like to use numbers? (True pr False): '))
    want_punct   = str(input('Would you like to use special characters? (True pr False): '))

    try:
        want_letters = eval(want_letters.title())
        want_numbers = eval(want_numbers.title())
        want_punct   = eval(want_punct.title())

        return [want_letters, want_numbers, want_punct]
    except NameError as e:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will generate a password with all available options')

        return [True, True, True]
  
def generate_password():
  

    if (alphanumberic == "y" and use_special_chrs == "y"): 
        print('Printing Alphanumberic and Special Character Password\n')
        password = "".join(choice(letters + numbers + special_chars) for x in range(length))
    elif (use_special_chrs == "y"): 
        password = "".join(choice(letters + special_chars) for x in range(length))
        print('Printing Special Character Password\n')
    elif (alphanumberic == "y"): 
        print('Printing Alphanumberic Password\n')
        password = "".join(choice(letters + numbers) for x in range(length))
    else: 
        print('Printing Password\n')
        password = "".join(choice(letters) for x in range(length))
    
    print(password)

generate_password()