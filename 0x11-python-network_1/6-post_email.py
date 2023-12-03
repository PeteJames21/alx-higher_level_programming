#!/usr/bin/python3
import sys
import requests
"""
Send a POST request
"""


if __name__ == "__main__":
    URL = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(URL, data=value)
    print("Your email is:", r.text)
