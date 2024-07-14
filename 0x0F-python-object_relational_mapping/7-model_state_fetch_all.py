#!/usr/bin/python3
"""Write a script that lists all State objects from the
database hbtn_0e_6_usa"""


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

    """print all object from the table State"""
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

        """close the session"""
    session.close()
