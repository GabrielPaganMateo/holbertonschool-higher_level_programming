#!/usr/bin/python3
"""
Deletes all State objects
wutg a name containing the
letter a
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
    state = session.query(State).filter(State.name.like('%a%'))
    for states in state:
        session.delete(states)
    session.commit()
    session.close()
