#!/usr/bin/python3
"""
Contains a definition of the `State` model, which maps to the 'state' table.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Models a state"""
    __tablename__ = "state"

    # The primary key is automatically autoincremented if the column is
    #  an integer primary key.
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Return the formal string representation of self."""
        return f"State(id={self.id}, name={state.name})"
