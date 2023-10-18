-- Create a table in which all rows have a unique id.

CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
