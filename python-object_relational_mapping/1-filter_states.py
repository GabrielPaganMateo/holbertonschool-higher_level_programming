#!/usr/bin/python3
"""List all states with a name
starting with N"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = (MySQLdb.connect(host='localhost', port=3306, user=username, 
                          passwd=password, db=database))
    cur = db.cursor()
    states = cur.execute('SELECT * FROM states WHERE name LIKE "[N]%"')
    for state in states:
        print(state)
    cur.close()
    db.close()
