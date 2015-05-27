-- Table definitions for the tournament project.
-- Guru Shetti 5/25/15 Original submission
-- Guru Shetti 5/26/15 Assessment feedback on Code Quality and Documentation
-- Creating table for storing tournaments so that database is useable across tournaments
-- droping table before creating. Also cascading becasue other tables depending on this one for foreign keys
DROP TABLE tournaments CASCADE;
-- create table fresh
CREATE TABLE tournaments ( tournament_id INTEGER PRIMARY KEY , tournament_name VARCHAR(80) NOT NULL, tournament_date DATE DEFAULT CURRENT_DATE);

-- Here we are inserting a value into the tournaments table so that we can run our program. This is extended feature that can be used in the future
INSERT INTO tournaments VALUES (1,'Udacity',DEFAULT);
-- create table for players

-- droping table before creating. Also cascading becasue other tables depending on this one for foreign keys
DROP TABLE players CASCADE;

-- create table players
CREATE TABLE players (player_id SERIAL PRIMARY KEY, player_name VARCHAR(80) NOT NULL, player_country VARCHAR(3) DEFAULT 'US', player_wins INTEGER DEFAULT 0);
-- test players uncomment if needed during unite testing--
-- insert into players values (DEFAULT,'Lewis Hamilton',DEFAULT);
-- insert into players values (DEFAULT,'Fernando Alonso',DEFAULT);

-- create matcches--
-- droping table before creating. Also cascading becasue other tables depending on this one for foreign keys
DROP TABLE matches;

DROP TYPE result;
-- creating type to make sure we are storing only particular entries
CREATE TYPE result AS ENUM ('won', 'lost', 'tied');
CREATE TABLE matches ( match_id SERIAL PRIMARY KEY, tournament_id INTEGER REFERENCES tournaments(tournament_id), player_id INTEGER REFERENCES players(player_id), player_standings result  , match_date DATE DEFAULT CURRENT_DATE);


