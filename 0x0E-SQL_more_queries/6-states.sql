-- A script that creates the database hbtn_0d_usa and the table states

-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail



CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
