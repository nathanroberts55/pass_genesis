"""
Author: Nate Roberts
Created: Sept. 9, 2020
"""
from password_strength import PasswordPolicy
from password_strength import PasswordStats

"""
    Password Strength Python Module Documentation: https://pypi.org/project/password-strength/
"""

# TODO: Ask if there is a specific policy password


def get_password_policy():
    want_polcy = str(
        input('Is there a password policy requirement (Please enter True or False): '))

    try:
        want_policy = eval(want_polcy.strip().title())
        return want_polcy

    except SyntaxError as s:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will assumed as False')
        return False
    except:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will assumed as False')
        return False
# TODO: If yes, fill in the password policy fields


def get_password_policy(bool_policy):
    default_policy = PasswordPolicy.from_names(
        length     = 8, # min length: 8
        uppercase  = 2, # need min. 2 uppercase letters
        numbers    = 2, # need min. 2 digits
        special    = 2, # need min. 2 special character need min. 
        nonletters = 2, # 2 non-letter characters (digits, specials, anything)
    )

    if bool_policy:
        policy_length     = input("Minimum Password Length (enter number): ")
        policy_uppercase  = input("Minimum Number of Uppercase Letters (enter number): ")
        policy_numbers    = input("Minimum Number of Numbers (enter number): ")
        policy_special    = input("Minimum Number of Special Characters (enter number): ")
        policy_nonletters = input("Minimum Number of Non-Letters [non-letter characters  means digits, specials, anything] (enter number): ")

        try:

            user_policy = PasswordPolicy.from_names(
                length     = int(policy_length), # min length: 8
                uppercase  = int(policy_uppercase), # need min. 2 uppercase letters
                numbers    = int(policy_numbers), # need min. 2 digits
                special    = int(policy_special), # need min. 2 special characters need min. 2 non-letter characters (digits, specials, anything)
                nonletters = int(policy_nonletters),
            )

            return user_policy

        except SyntaxError as s:
            print("Invalid Entry: Default of 8 length, 2 uppercase, 2 numbers, 2 special, and 2 non letters will be entered")
            return default_policy

        except SyntaxError as s:
            print("Invalid Entry: Default of 8 length, 2 uppercase, 2 numbers, 2 special, and 2 non letters will be entered")
            return default_policy

# TODO: Take in the users password
def get_user_password():
    user_password = str(input("What is the password you would like to test?: "))
    return user_password

# TODO: Test the users password against the policy
def password_vs_policy(password, policy):
    policy_test = policy.test(password)
    return policy_test

# TODO: Return the password strength
def password_strength(password):
    stats = PasswordStats(password)
    strength = stats.strength()

    if strength >= 0.80:
        print("This is a very strong password!")
    elif strength >= 0.50 and strength <= 0.80:
        print("This is a medium strength password. Consider increasing complexity.")
    else:
        print("This is a weak password. Highly consider increasing the complexity")
    
    return strength 

# TODO: If there is a password policy, return feedback on the password against the password policy
def policy_feedback(password, policy):
    LENGTH     = "You password fails to meet the length requirement specified by your policy\n"
    UPPERCASE  = "You password fails to meet the uppercase requirement specified by your policy\n"
    NUMBERS    = "You password fails to meet the numbers requirement specified by your policy\n"
    SPECIAL    = "You password fails to meet the special requirement specified by your policy\n"
    NONLETTERS = "You password fails to meet the nonletter requirement specified by your policy\n"

    policy_feedback = ''
    
    if policy:
        password_report = password_vs_policy(password, policy)
    
    if len(password_report) == 0:
        print('Your password meets all of the requirements set by the policy!')

    policy_feedback = ''
    # policy_feedback += LENGTH if f'Length({policy.length})' password_report    


### BEGIN TEST SECTION
default_policy = PasswordPolicy.from_names(
        length     = 8, # min length: 8
        uppercase  = 2, # need min. 2 uppercase letters
        numbers    = 2, # need min. 2 digits
        special    = 2, # need min. 2 special character need min. 
        nonletters = 2, # 2 non-letter characters (digits, specials, anything)
    )

print(default_policy.test[0][0])
### END TEST SECTION

