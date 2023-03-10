-- all cities
SELECT cities.id, cities.name FROM cities
JOIN states
ON cities.state_id = hbtn_0d_usa.states.id;