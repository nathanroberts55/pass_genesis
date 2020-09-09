"""
Author: Nate Roberts
Created: Sept. 9, 2020
"""
from password_strength import PasswordPolicy
from password_strength import PasswordStats

"""
    Password Strength Python Module Documentation: https://pypi.org/project/password-strength/
    Password Strength Python Module Github       : https://github.com/kolypto/py-password-strength
"""

# TODO: Ask if there is a specific policy password
def get_password_policy():
    want_polcy = str(
        input('Is there a password policy requirement (Please enter True or False): '))

    try:
        want_policy = eval(want_polcy.strip().title())
        return want_policy

    except SyntaxError as s:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will assumed as False')
        return False
    except:
        print('Invalid value. Please use either \"True\" or \"False\" as values')
        print('Invalid Values will assumed as False')
        return False

# TODO: If yes, fill in the password policy fields
def get_password_policy_rules(bool_policy):
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
    
    return None

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
    if policy:
        password_report = password_vs_policy(password, policy)

    # Holders for the for loop, tracking the policy failures and the index for the failure list
    password_feedback = ''
    failure_number    = 0


    if len(password_report) == 0:
        password_feedback += "Your password meets all policy requirements\n"
    else:
        for failure in password_report:
            password_feedback += f'Your password fails to meet the {password_report[failure_number]} requirement specified by your policy\n'
            failure_number    += 1
        

    return password_feedback


if __name__ == "__main__":
    # Ask the user if there is a password policy
    is_password_policy = get_password_policy()
    # If there is a password policy, then get the specifications for the password policy
    password_policy    = get_password_policy_rules(is_password_policy)
    # Get the user's password they want to test 
    user_password      = get_user_password()

    # If there is a password policy, see if the user's password meets the policy requirements
    if is_password_policy: 
        print(policy_feedback(user_password, password_policy))

    # Tests the strength of the password
    password_strength(user_password)

