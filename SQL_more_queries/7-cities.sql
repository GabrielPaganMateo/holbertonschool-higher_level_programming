-- create database and table
CREATE DATABASE if not exists hbtn_0d_usa;
CREATE TABLE if not exists hbtn_0d_usa.cities (
    id int serial DEFAULT value primary key,
    foreign key (state_id) references states(id),
    name VARCHAR(256) not null
);