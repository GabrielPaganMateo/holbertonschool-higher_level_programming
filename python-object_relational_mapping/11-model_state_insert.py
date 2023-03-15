#!/usr/bin/python3
"""
Adds the State object Louisiana
to the databas
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
    table_len = len(states) + 1
    new_state = State(id=table_len, name="Louisiana")
    print(new_state.id)
    session.add(new_state)
    session.commit()
    session.close()
