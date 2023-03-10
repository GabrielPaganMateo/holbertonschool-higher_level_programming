-- Create database and table
CASE
    when hbtn_0d_usa not exists then CREATE DATABASE if not exists hbtn_0d_usa;
    when hbtn_0d_use.states not exists then CREATE TABLE if not exists states (
    id int not null unique primary key,
    name VARCHAR(256) not null
    );
