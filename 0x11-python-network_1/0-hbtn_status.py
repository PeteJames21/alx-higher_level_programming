#!/usr/bin/python3
"""
Query a URL using the urllib package
"""
import urllib.request


if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(URL) as response:
        body = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
