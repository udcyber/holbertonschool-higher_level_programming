#!/usr/bin/python3
"""A script that lists all states from the database htbn_0e_0_usa.
should take 3 arguments: mysql username, mysql password, database name
hould connect to a MySQL server running on localhost at port 3306
results must be sorted in ascending order by states.id
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
