#!/usr/bin/python3
"""
Add the state `Louisiana` to the database.
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

    # Add a new state and print its id.
    state_name = "Louisiana"
    state = State(name=state_name)
    session.add(state)
    session.commit()
    # Print the ID of the newly added state. Get the last ID since
    #  the IDs are autoincremented and that of the newly inserted state
    #  is guaranteed to have the highest index.
    id_ = (
        session.query(State.id)
        .filter(State.name == state_name)
        .order_by(State.id.desc())
        .first()[0]
    )
    print(id_)

    session.close()
