"""
contains the class definition of a City
"""

from sqlalchemy import Column, VARCHAR, ForeignKey, INT
from model_state import Base

class City(Base):
    __tablename__ = "cities"
    id = Column(autoincrement=True, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    state_id = Column(INT, ForeignKey("states.id"))

    def __repr__(self):
        return f"State({self.id}, {self.name}, {self.state_id})"
