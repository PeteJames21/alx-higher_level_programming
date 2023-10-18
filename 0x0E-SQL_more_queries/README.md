# 0x0E. SQL - More queries 

## 0-privileges.sql
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

## 1-create_user.sql
Create a MySQL user with all privileges.

## 2-create_read_user.sql
Create a user with only SELECT privileges on a particular database

## 3-force_name.sql
Create a table called force_name in the current database

## 4-never_empty.sql
Create a table called `id_not_null` in the current database with a field containing an explicit default value.

## 5-unique_id.sql
Create a table in which all rows have a unique id.

## 6-states.sql
Create a table with an auto-generated primary key.

## 7-cities.sql
Create a table with a foreign key.

## 8-cities_of_california_subquery.sql
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
- The states table contains only one record where name = California (but the id can be different, as per the example)
- Results must be sorted in ascending order by cities.id
- You are not allowed to use the JOIN keyword
- The database name will be passed as an argument of the mysql command
