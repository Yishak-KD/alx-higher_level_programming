#!/usr/bin/python3
"""
list the id by taking an argument
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

    u_names = session.query(State).order_by(State.id)

    for i in u_names:
        if i.name == sys.argv[4]:
            print(f"{i.id}")
    else:
        print("Not found")
