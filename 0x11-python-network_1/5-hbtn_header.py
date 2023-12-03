#!/usr/bin/python3
"""
Display the value of a response header
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    r = requests.get(URL)
    print(r.headers.get("X-Request-Id"))
