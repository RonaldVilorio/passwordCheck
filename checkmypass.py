import requests
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5char)
    print(response)

# request_api_data("123")
pwned_api_check("hello")
