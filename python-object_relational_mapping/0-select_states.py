#!/usr/bin/python3
"""
List all states from the database htbn_0e_0_usa.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    for row in cursor.fetchall():
        print(row)
    db.close()
