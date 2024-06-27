#!/usr/bin/python3
"""0-select_states lists all states from the database hbtn_0e_0_usa:"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",port=3306,user=sys.argv[1],password=sys.argv[2], database=sys.argv[3])
    cus = db.cursor()
    cus.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_row = cus.fetchall()
    for row in query_row:
        print(row)
    cus.close()
    db.close()
