#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa.
Usage: ./<script_name> <userName> <password> <dbName>
"""
from model_state import State
from sqlalchemy import create_engine
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

    # Get all states
    results = session.query(State.id, State.name).order_by(State.id).all()
    for result in results:
        print(f"{result[0]}: {result[1]}")
