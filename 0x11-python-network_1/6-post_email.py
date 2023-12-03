#!/usr/bin/python3
"""
Send a POST request
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(URL, data=value)
    print(r.text)
