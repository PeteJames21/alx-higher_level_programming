# 0x0F-python-object_relational_mapping

## 0-select_states.py
Write a script that lists all states from the database `hbtn_0e_0_usa`:
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- Use the module `MySQLdb` (import MySQLdb)
- The script should connect to a MySQL server running on localhost at port 3306
- The results must be sorted in ascending order by states.id
