#!/usr/bin/bash
# Send a request to a URL and display the size of the body of the response in bytes.
curl -sI "$1" | grep Content-Length | cut --delimiter=" " -f 2
