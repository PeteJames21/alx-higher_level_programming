#!/usr/bin/python3
"""
Get a response and error code.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]

    request = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
