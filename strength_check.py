import requests
from requests.exceptions import HTTPError
import hashlib

"""
hashlib Documentation               : https://docs.python.org/2/library/hashlib.html
request.Reponse Object Documentation: https://www.w3schools.com/python/ref_requests_response.asp
Reponse JSON parsing Pynative       : https://pynative.com/parse-json-response-using-python-requests-library/
"""

password_test = 'e3$52bHg2!'
encoded_password_test = password_test.encode()
# print(password_test)

password_hash = hashlib.sha1(encoded_password_test).hexdigest()
hash_first_five = password_hash[:5]
rest_of_hash = password_hash[5:].upper()
# print(password_hash)

url = f"https://api.pwnedpasswords.com/range/{hash_first_five}"

headers = {
    'x-rapidapi-host': "moocher-io-common-passwords-v1.p.rapidapi.com",
    'x-rapidapi-key': "e219e80c46mshe9f0d1499fa225cp106a16jsn9a2e0122d341"
    }

# response = requests.request("GET", url)
# print(response.text)

try: 
    response = requests.get(url)
    response.raise_for_status()
    # access JSOn content
    text_response = response.text
    lines = text_response.split("\n")
    password_dict = {}

    for line in lines:
        password, times_seen = line.split(":")
        password_dict[password.strip()] = times_seen.strip()
    
    times_found = password_dict.get(rest_of_hash)

    if times_found:
        print(f"Your password {password_test} was found {times_found} times in our list")
        print("Please highly consider changing your password to something more secure")
    else: 
        print("Your password was not found on any of our list and is realitvely safe for now. Great Job!")
    
    # print(password_dict)
    # print(text_response)

except HTTPError as http_err: 
    print(f'HTTP error occurred: {http_err}')
# except Exception as err: 
#     print(f'Other error occurred: {err}')
    
