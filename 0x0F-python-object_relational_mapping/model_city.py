#!/usr/bin/python3
"""
contains the class definition of a City
"""
from sqlalchemy import Column, VARCHAR, ForeignKey, INT
from model_state import Base


class City(Base):
    """
    SQLAlchemy model representing the 'cities' table.

    Attributes:
        id (int): Primary key for the city.
        name (str): Name of the city.
        state_id: rrelate to states_id
    """
    __tablename__ = "cities"
    id = Column(autoincrement=True, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    state_id = Column(INT, ForeignKey("states.id"))

    def __repr__(self):
        return f"State({self.id}, {self.name}, {self.state_id})"
