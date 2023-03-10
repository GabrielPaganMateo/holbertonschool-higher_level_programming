-- Create database and table
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE states (
    id int not null unique primary key,
    name VARCHAR(256) not null
);