#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.orm import declarative_base


# engine = create_engine(
# f"mysql+mysqldb://{sys.argv[1]}:{sys.argv2}@localhost:3306/{sys.argv[3]}")

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)

    def __repr__(self):
        return f"State({self.id}, {self.name})"
