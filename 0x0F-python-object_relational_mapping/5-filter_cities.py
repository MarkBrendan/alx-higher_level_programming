#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    state_name = sys.argv[4]

    """establish the connection"""
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])

    """Create an cursor object"""
    cont = db.cursor()
    cont.execute("SELECT cities.name FROM cities JOIN states ON "
                 "cities.state_id = states.id WHERE states.name = %s "
                 "ORDER BY cities.id ASC", (state_name,))

    """Fetch all rows"""
    get_all = cont.fetchall()
    for i in get_all:
        print(i)

    """Close cursor and database connection"""
    cont.close()
    db.close()
