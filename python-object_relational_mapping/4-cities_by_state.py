#!/usr/bin/python3
"""
List all cities from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = (MySQLdb.connect(host='localhost', port=3306, user=username,
                          passwd=password, db=database))
    cur = db.cursor()
    cur.execute(("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id"))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()