#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from
    the database using SQLAlchemy
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy.engine.url import URL

    db_config = {
        "drivername": "mysql+mysqldb",
        "host": "localhost",
        "port": 3306,
        "username": sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
    }

    url = URL(**db_config, query={})
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)  # create db&tables if not present
    Session = sessionmaker(bind=engine)  # create Session class
    session = Session()  # createsession object
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    session.close()
