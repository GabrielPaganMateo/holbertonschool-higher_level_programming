#!/usr/bin/python3
"""
Prints the State object with tha name passed
as argument
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = (create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2],
                                    sys.argv[3]), pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    found = 0
    for state in states:
        if state.name.find(sys.argv[4]) != -1:
            print("{}".format(state.id))
            notfound = 0
            found = 1
        else:
            notfound = 1
    if notfound == 1 and found == 0:
        print("Not found")
    session.close()
