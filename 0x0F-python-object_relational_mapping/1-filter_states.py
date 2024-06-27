#!/usr/bin/python3
"""1-filter_states lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])

    cont = db.cursor()
    cont.execute("SELECT * FROM states
                 WHERE name LIKE 'N%' ORDER BY states.id ASC")
    get_all = cont.fetchall()
    for i in get_all:
        print(i)
    cont.close()
    db.close()
