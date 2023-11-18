#!/usr/bin/python3
"""
Change the name of the `State` where `id = 2` to `New Mexico`
Usage: ./<script_name> <userName> <password> <dbName>
"""
from model_state import State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./<script_name> <userName> <password> <dbName>")
        exit(1)

    uname, pwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    URL = f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db_name}"
    engine = create_engine(URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update the name of a state
    state = session.query(State).filter(State.id == 2).one()
    state.name = "New Mexico"
    session.commit()

    session.close()
