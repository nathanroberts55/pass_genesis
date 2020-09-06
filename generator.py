"""
Tool created to help user generate strong passwords
"""
import random
import string

#TODO: Create variables to store Alphabet in Upper and Lower case, numbers, and special characters
LETTERS = string.ascii_letters
NUMBERS = string.digits
SPECIAL_CHARS = '!@#$%&*?+'

      
#TODO: Let the user decide the strength of the password (i.e length, alphanumberic, special characters or not)
#TODO: Create variable to hold the combination of letters and numbers
def get_password_length():
    """Function to get the desired password length from the user

    Returns:
        int : Desired length of the password
    """
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

def get_string_constants(choice_list):
    string_constant = ''
    string_constant += LETTERS if choice_list[0] else ''
    string_constant += NUMBERS if choice_list[1] else ''
    string_constant += SPECIAL_CHARS if choice_list[2] else ''

    return string_constant
  
def password_generator(cbl, length=8):
    printable = get_string_constants(cbl)

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)

    return random_password



if __name__ == '__main__':
    length = get_password_length()
    choice_list = password_combination_choice()
    password = password_generator(choice_list, length)
    print(password)

# # testing password generator with it's default length of 8
# password_one = password_generator()

# # testing password generator using user's input as length
# password_length = get_password_length()
# password_two = password_generator(password_length)

# print("password one (" + str(len(password_one)) + "):\t\t" + password_one )
# print("password one (" + str(len(password_two)) + "):\t\t" + password_two )




# def generate_password():
  

#     if (alphanumberic == "y" and use_special_chrs == "y"): 
#         print('Printing Alphanumberic and Special Character Password\n')
#         password = "".join(choice(letters + numbers + special_chars) for x in range(length))
#     elif (use_special_chrs == "y"): 
#         password = "".join(choice(letters + special_chars) for x in range(length))
#         print('Printing Special Character Password\n')
#     elif (alphanumberic == "y"): 
#         print('Printing Alphanumberic Password\n')
#         password = "".join(choice(letters + numbers) for x in range(length))
#     else: 
#         print('Printing Password\n')
#         password = "".join(choice(letters) for x in range(length))
    
#     print(password)

# generate_password()