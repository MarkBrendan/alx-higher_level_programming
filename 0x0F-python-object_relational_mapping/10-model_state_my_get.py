#!/usr/bin/python3
"""Write a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    arg_name = argv[4]
    """Create a connection and a session to interacte with the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    """print all object from the table State"""
    result = session.query(State).filter(State.name == arg_name)\
        .order_by(State.id).first()

    if result is None:
        print("Not found")
    else:
        print("{}".format(result.id))

    """close the session"""
    session.close()
