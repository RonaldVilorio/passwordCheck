import requests
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res
    
def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash,count in hashes:
        if hash == hash_to_check:
            return (hash,count)
        else:
            continue
        
def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5char)
    return get_password_leaks_count(response,tail)

# request_api_data("123")
print(pwned_api_check("hello"))
