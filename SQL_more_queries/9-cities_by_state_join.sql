-- all cities
SELECT cities.id, name FROM cities
JOIN states
ON cities.state_id = states.id;