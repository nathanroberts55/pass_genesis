"""
Author: Nate Roberts
Created: September 6, 2020
"""
import requests
from requests.exceptions import HTTPError
import hashlib

"""
hashlib Documentation               : https://docs.python.org/2/library/hashlib.html
request.Reponse Object Documentation: https://www.w3schools.com/python/ref_requests_response.asp
Reponse JSON parsing Pynative       : https://pynative.com/parse-json-response-using-python-requests-library/
pwned passwords API documentation   : https://haveibeenpwned.com/API/v2#PwnedPasswords
pwned passwords overview            : https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/
"""


def get_password():
    """Gets the user's password they would like to check in the most common passwords list

    Returns:
        string: password they would like to check
    """
    
    user_password = str(input('Please enter the password you would like to check: ')).strip()
    return user_password


def hash_password(password):
    """Hashes the password using SHA1 to prepare the password for interaction with the pwnedpasswords API

    Args:
        password (string): password string recieved from get_password()

    Returns:
        list: list contains the password as a string, the first 5 characters of the hashed password to be used in the url for the APi, and the remainder 
        of the hashed password that is used to search the commonly used password list returned by the API.
    """

    password_to_hash = password
    encoded_password = password_to_hash.encode()
    password_hash    = hashlib.sha1(encoded_password).hexdigest()
    hash_first_five  = password_hash[:5]
    rest_of_hash     = password_hash[5:].upper()

    return [password_to_hash, hash_first_five, rest_of_hash]


def check_common_passlist(hashlist):
    """Uses the pwnedpasswords API to discover if the user's suggested password is found on commonly used passwords list

    Args:
        hashlist (list): list contains the password as a string, the first 5 characters of the hashed password to be used in the url for the APi, and the remainder 
        of the hashed password that is used to search the commonly used password list returned by the API. 
    """

    # API url only uses the first 5 characters to find the password
    url = f"https://api.pwnedpasswords.com/range/{hashlist[1]}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # API returns a list of passwords that share the first 5 hash values and the amount of times that they are found
        # Examples can found at https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/
        text_response = response.text
        lines         = text_response.split("\n")
        password_dict = {}

        for line in lines:
            password     , times_seen       = line.split(":")
            password_dict[password.strip()] = times_seen.strip()

        times_found = password_dict.get(hashlist[2])

        if times_found:
            print(f"Your password {hashlist[0]} was found {times_found} times in our list")
            print("Please highly consider changing your password to something more secure")
        else:
            print("Your password was not found on any of our list and is realitvely safe for now. Great Job!")

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


if __name__ == '__main__':
    password        = get_password()
    hashed_password = hash_password(password)
    check_common_passlist(hashed_password)
