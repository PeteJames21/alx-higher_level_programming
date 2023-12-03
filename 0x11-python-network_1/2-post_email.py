#!/usr/bin/python3
"""
Send a POST request with some attributes.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    params = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(params).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
