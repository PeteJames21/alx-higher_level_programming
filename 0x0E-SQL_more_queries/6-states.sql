-- Create a table with an auto-generated primary key.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);
