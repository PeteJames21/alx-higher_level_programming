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

## 9-cities_by_state_join.sql
Write a script that lists all cities contained in the database `hbtn_0d_usa`.
- Each record should display: `cities.id - cities.name - states.name`
- Results must be sorted in ascending order by `cities.id`
- You can use only one SELECT statement
- The database name will be passed as an argument of the `mysql` command

## 10-genre_id_by_show.sql
Import the database dump from [hbtn_0d_tvshows](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) to your MySQL server.
Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

## 11-genre_id_all_shows.sql
Import the database dump from [hbtn_0d_tvshows](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) to your MySQL server.
Write a script that lists all shows contained in the database hbtn_0d_tvshows.
-Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- If a show doesn’t have a genre, display NULL
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

## 12-no_genre.sql
Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command
