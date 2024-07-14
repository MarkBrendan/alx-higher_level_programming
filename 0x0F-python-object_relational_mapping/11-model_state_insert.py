#!/usr/bin/python3
"""Write a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa"""


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
    result = session.query(State).filter(State.name == "Louisiana").first()

    """Check if the State already exist else add the state object"""
    if result:
        print("Louisiana already exist")
    else:
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print("{}".format(new_state.id))

    """close the session"""
    session.close()
