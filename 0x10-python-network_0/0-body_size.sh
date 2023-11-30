#!/bin/bash
# Display size of body of a response in bytes
curl -s "$1" | wc -c
