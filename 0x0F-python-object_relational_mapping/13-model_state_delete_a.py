#!/usr/bin/python3
"""Write a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    """Create a connection and a session to interacte with the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    """get and print all object from the table State"""
    results = session.query(State).filter(State.name.like("%a%"))

    for result in results:
        session.delete(result)
    session.commit()

    """close the session"""
    session.close()
