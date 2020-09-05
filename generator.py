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
def generate_password():
    length = int(str(input('How long would should the password be?: ')).strip(" "))
    alphanumberic = str(input('Would you like to use numbers? (Y or N): ')).strip(" ").lower()
    use_special_chrs = str(input('Would you like to use special characters? (Y or N): ')).strip(" ").lower()

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