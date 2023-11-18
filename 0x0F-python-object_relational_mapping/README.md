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

## 3-my_safe_filter_states.py
Re-write `2-my_filter_states.py` in a way that prevents SQL injection attacks

## 4-cities_by_state.py
Write a script that lists all cities from the database `hbtn_0e_4_usa`

## 5-filter_cities.py
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the `database hbtn_0e_4_usa`

## model_state.py
Write a python file that contains the class definition of a State and an instance Base = declarative_base():
- State class:
   - inherits from Base Tips
   - links to the MySQL table states
   - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
   - class attribute name that represents a column of a string with maximum 128 characters and can’t be null
- Use the module SQLAlchemy
- The script should connect to a MySQL server running on localhost at port 3306


## 7-model_state_fetch_all.py
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

## 8-model_state_fetch_first.py
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

## 9-model_state_filter_a.py
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

## 10-model_state_my_get.p
Write a script that prints the `State` object with the name passed as argument from the database `hbtn_0e_6_usa`

## 11-model_state_insert.py
Write a script that adds the State object “Louisiana” to the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`

## 12-model_state_update_id_2.py
Change the name of the `State` where `id = 2` to `New Mexico`

## 13-model_state_delete_a.py
Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`
