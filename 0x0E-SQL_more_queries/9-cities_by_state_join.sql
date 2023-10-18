-- List all cities in the database

SELECT cities.id, cities.name, states.name
FROM cities
    INNER JOIN states
        ON states.id = cities.id
ORDER BY cities.id ASC;
