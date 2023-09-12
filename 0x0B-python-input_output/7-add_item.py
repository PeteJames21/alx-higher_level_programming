#!/usr/bin/python3
"""
Add all command line arguments passed to this script to the list saved in
add_items.json in the current working directory. Create the file if it
does not exist. If it already exists, append the arguments to the
serialized list in the file.
"""
import sys
import json

FILE_NAME = "add_item.json"

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# Get the commandline arguments
args = sys.argv[1:]

# Load the list
try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        lst = json.load(f)

except FileNotFoundError:
    # Create an empty file if it doesn't exist
    with open(FILE_NAME, "w", encoding="utf-8"):
        pass
    lst = []

# Append args to the list
lst.extend(args)

# Serialize the list to JSON
with open(FILE_NAME, "w", encoding="utf-8") as f:
    json.dump(lst, f)
