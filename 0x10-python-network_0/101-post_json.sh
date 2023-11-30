#!/bin/bash
# Send a JSON POST request. The URL is the first arg of the script and the file is the second
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
