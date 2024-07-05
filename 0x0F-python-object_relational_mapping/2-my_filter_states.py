#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

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
    cont.execute("SELECT * FROM states "
                 "WHERE name LIKE BINARY '%{}%' ORDER BY states.id "
                 "ASC".format(state_name))

    """Fetch all rows"""
    get_all = cont.fetchall()
    for i in get_all:
        print(i)

    """Close cursor and database connection"""
    cont.close()
    db.close()
