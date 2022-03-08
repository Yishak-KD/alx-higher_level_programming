#!/usr/bin/python3
"""
list all State objects from a given database
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    u_names = session.query(State).filter(
        State.name.contains('a')).order_by(asc(State.id))

    for i in u_names:
        print(f"{i.id}: {i.name}")
