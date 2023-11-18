#!/usr/bin/python3
"""
Get the id of a particular state from the database hbtn_0e_6_usa.
Usage: ./<script_name> <userName> <password> <dbName> <stateName>
"""
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./<script_name> <userName> <password> <db> <stateName>")
        exit(1)

    uname, pwd, db, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    URL = f"mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}"
    engine = create_engine(URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the id of the state
    try:
        result = session.query(State.id).filter(State.name == state).one()
        print(result[0])
    except NoResultFound:
        print("Not found")

    session.close()
