#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
Results are displayed in the format:
    <state name>: (<city id>) <city name>
"""
if __name__ == "__main__":
    from sys import argv
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import sessionmaker

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
        print(f"{state.name}: ({city.id}) {city.name}")
