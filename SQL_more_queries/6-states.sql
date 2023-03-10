-- Create database and table
CREATE DATABASE if not exists hbtn_0d_usa;
CREATE TABLE if not exists hbtn_0d_usa.states (
    id int SERIAL DEFAULT VALUE primary key,
    name VARCHAR(256) not null
    );
