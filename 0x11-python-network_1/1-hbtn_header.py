#!/usr/bin/python3
"""
Get the value of a response header. The URL is passed as an argument
to this script.
"""
import sys
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        print(dict(response.headers).get("X-Request-Id"))
