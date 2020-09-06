import requests
from requests.exceptions import HTTPError
import hashlib

"""
hashlib Documentation               : https: //docs.python.org/2/library/hashlib.html
request.Reponse Object Documentation: https: //www.w3schools.com/python/ref_requests_response.asp
Reponse JSON parsing Pynative       : https://pynative.com/parse-json-response-using-python-requests-library/
"""

password_test = 'password123'.encode()
# password_test = password_test
print(password_test)

password_hash = hashlib.sha1(password_test).hexdigest()
hash_first_five = password_hash[:5]
rest_of_hash = password_hash[5:]
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
    print("Entire Text Format")
    print(text_response)

except HTTPError as http_err: 
    print(f'HTTP error occurred: {http_err}')
except Exception as err: 
    print(f'Other error occurred: {err}')
    
