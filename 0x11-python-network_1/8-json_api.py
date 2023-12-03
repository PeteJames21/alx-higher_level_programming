#!/usr/bin/python3
"""
Make a POST request
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        response_json = response.json()
        if response_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                response_json.get("id"), response_json.get("name"))
            )
    except ValueError:
        print("Not a valid JSON")
