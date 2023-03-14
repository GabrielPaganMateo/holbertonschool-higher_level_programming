#!/usr/bin/python3
"""
Write a script that takes in arguments
and displays all values in the states table
where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = (MySQLdb.connect(host='localhost', port=3306, user=username,
                          passwd=password, db=database))
    cur = db.cursor()
    cur.execute(("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                 .format(state_name)))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
