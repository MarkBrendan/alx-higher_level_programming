#!/usr/bin/python3
"""Once again, write a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""

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
                 "WHERE name LIKE BINARY %s ORDER BY states.id "
                 "ASC", (state_name,))

    """Fetch all rows"""
    get_all = cont.fetchall()
    for i in get_all:
        print(i)

    """Close cursor and database connection"""
    cont.close()
    db.close()
