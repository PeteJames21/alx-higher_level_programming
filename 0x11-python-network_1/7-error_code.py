#!/usr/bin/python3
"""
Make a request and check the status code before printing the content.
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    resp = requests.get(URL)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
