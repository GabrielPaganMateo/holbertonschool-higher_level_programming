#!/usr/bin/python3
"""
Takes in state name as argument and lists
all cities of that state
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
    str1 = f'SELECT cities.name FROM cities JOIN states'
    str2 = f' ON cities.state_id = states.id'
    str3 = str1 + str2
    cur.execute(str3)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
