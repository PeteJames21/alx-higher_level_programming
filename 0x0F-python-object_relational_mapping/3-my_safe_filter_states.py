#!/usr/bin/python3

"""
List all states in the database whose name matches that provided by the user.
    Usage: <username> <password> <databaseName> <stateName>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get username and password
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <databaseName> <stateName>")
        exit(1)
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(user=uname, password=pwd, database=db_name)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id",
        (name,)
    )
    results = cursor.fetchall()
    for result in results:
        print(result)
    db.close()
