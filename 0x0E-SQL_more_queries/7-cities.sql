-- A script that creates the database hbtn_0d_usa and the table cities

-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail


CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,

	CONSTRAINT pk_id PRIMARY KEY(id),
	CONSTRAINT fk_state_id FOREIGN KEY(state_id) REFERENCES(states.id)
);
