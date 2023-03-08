-- no link
SELECT score, name FROM second_table WHERE name IS NOT NULL GROUP BY score ORDER BY score DESC;