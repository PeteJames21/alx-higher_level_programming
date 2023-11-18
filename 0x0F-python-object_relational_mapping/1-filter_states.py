#!/usr/bin/python3

"""
List all states in the database beginning with the letter 'N'.
    Usage: <username> <password> <databaseName>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get username and password
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <databaseName>")
        exit(1)
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=uname, password=pwd, database=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    results = cursor.fetchall()
    for result in results:
        # This could alternatively be done using the query:
        #  "SELECT * FROM states WHERE name like 'N%' ORDER BY id"
        if result[1][0] == 'N':
            print(result)
    db.close()
