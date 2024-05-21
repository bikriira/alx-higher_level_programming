#!/usr/bin/python3
"""
Script to define a SQLAlchemy model representing the 'states' table.
"""

from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

# Uncomment and adjust engine creation if needed
# engine = create_engine(
# f"mysql+mysqldb://{sys.argv[1]}:{sys.argv2}@localhost:3306/{sys.argv[3]}")

Base = declarative_base()


class State(Base):
    """
    SQLAlchemy model representing the 'states' table.

    Attributes:
        id (int): Primary key for the state.
        name (str): Name of the state.
        cities (relationship): One-to-many relationship with City objects.
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref="state"
    )

    def __repr__(self):
        return f"State({self.id}, {self.name})"
