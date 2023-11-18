#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./<script_name> <userName> <password> <dbName>
"""
from model_state import State
from model_city import City
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
    results = (
        session.query(State.name, City.id, City.name)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for result in results:
        print(f"{result[0]}: ({result[1]}) {result[2]}")

    session.close()
