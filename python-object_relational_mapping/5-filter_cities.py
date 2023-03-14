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
    state_name = {argv[4]}

    db = (MySQLdb.connect(host='localhost', port=3306, user=username,
                          passwd=password, db=database))
    cur = db.cursor()
    str1 = f'SELECT cities.name FROM cities JOIN states'
    str2 = f' ON cities.state_id = states.id WHERE states.name = %s'
    str3 = str1 + str2
    cur.execute(str3, state_name)
    states = cur.fetchall()
    for state in states:
        i = 0
        str = ''
        for name in state:
            str = str + name
        if i < len(states) - 1:
            print(str + ', ', end='')
            i += 1
        else:
            print(str)
    cur.close()
    db.close()
