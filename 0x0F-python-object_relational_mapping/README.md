# 0x0F-python-object_relational_mapping

## 0-select_states.py
Write a script that lists all states from the database `hbtn_0e_0_usa`:
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- Use the module `MySQLdb` (import MySQLdb)
- The script should connect to a MySQL server running on localhost at port 3306
- The results must be sorted in ascending order by states.id

## 1-filter_states.py
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

## 2-my_filter_states.py
Write a script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where `name` matches the argument.
- The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` 
