#!/usr/bin/python3
"""
Contains a definition of the `City` model, which maps to the 'cities' table.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """Models a city"""
    __tablename__ = "cities"

    # The primary key is automatically autoincremented if the column is
    #  an integer primary key.
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)

    def __repr__(self):
        """Return the formal string representation of self."""
        return f"City(id={self.id}, name={self.name}, "\
               "state_id={self.state_id})"
