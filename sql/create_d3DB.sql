CREATE DATABASE IF NOT EXISTS d3stats;

CREATE TABLE usr (
	id INT(11) NOT NULL AUTO INCREMENT,
	name VARCHAR(30) NOT NULL UNIQUE,
	pass VARCHAR(30) NOT NULL,
	PRIMARY KEY (id)
)

CREATE TABLE difficulty (
	id INT(11) NOT NULL AUTO INCREMENT,
	name VARCHAR(100) NOT NULL UNIQUE,
	PRIMARY KEY (id)
)

CREATE TABLE run (
	id INT(11) NOT NULL AUTO INCREMENT,
	start_time DATETIME,
	end_time DATETIME,
	total_time DATETIME NOT NULL,
	map INT(11) NOT NULL,
	xp_gain INT(20),
	legend_drops INT(11),
	goblin_count INT(11),
	gold_gain INT(20),
	y_mobs INT(11),
	b_mobs INT(11),
	p_mobs INT(11),
	difficulty INT(11),
	notes VARCHAR(5000),
	usr_id INT(11),
	PRIMARY KEY (id)
)
