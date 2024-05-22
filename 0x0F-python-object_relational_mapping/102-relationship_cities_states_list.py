#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
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

    results = session.query(City, State).join(State).order_by(City.id)

    for city, state in results:
        print(f"{city.id}: {city.name} -> {state.name}")

    session.close()
