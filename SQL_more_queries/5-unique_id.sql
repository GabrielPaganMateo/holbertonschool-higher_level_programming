-- Create table
create table if not exists unique_id (
    id int unique DEFAULT 1,
    name VARCHAR(256)
);