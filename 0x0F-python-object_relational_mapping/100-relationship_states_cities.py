#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    url = URL(
        drivername="mysql+mysqldb",
        username=argv[1],
        password=argv[2],
        host="localhost",
        port=3306,
        database=argv[3],
        query={},
    )

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California"
    california = State(name="California")

    # Create the City "San Francisco" and associate it
    # with the State "California"
    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
