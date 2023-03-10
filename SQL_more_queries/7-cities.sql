-- create database and table
CREATE database if not exists hbtn_0d_usa;
Create table if not exists hbtn_0d_usa.cities (
    id int serial DEFAULT value primary key,
    state_id int not null foreign key references states(id),
    name VARCHAR(256) not null
)