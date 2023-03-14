#!/usr/bin/python3
"""
Script that lists all states 
from the database hbtn_0e_0_usa
"""
import MySQLdb
"""
I am currently trying to
document this module so the
checkers pass
"""

db = MySQLdb.connect(host="localhost", port=3306, user="gabriel", passwd="password", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states")