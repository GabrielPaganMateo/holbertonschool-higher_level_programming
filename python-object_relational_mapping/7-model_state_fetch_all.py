#!/usr/bin/python3
"""
Script that lists all State objects from the database
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
    for states in session.query(State).order_by(State.id).all():
        print("{}: {}".format(states.id, states.name))
    session.close()
