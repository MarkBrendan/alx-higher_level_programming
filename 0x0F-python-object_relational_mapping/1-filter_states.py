#!/usr/bin/python3
"""1-filter_states.py lists all states with a name N"""

import MySQLdb
import sys

if __name__ == "__main__":
    """establish the connection"""
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])

    """Create an cursor object"""
    cont = db.cursor()
    cont.execute("SELECT * FROM states "
                 "WHERE name LIKE 'N%' ORDER BY states.id ASC")

    """Fetch all rows"""
    get_all = cont.fetchall()
    for i in get_all:
        print(i)

    """Close cursor and database connection"""
    cont.close()
    db.close()
