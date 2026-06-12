#!/usr/bin/python3
"""list all states from database"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    rows_number = cursor.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(rows_number):
        print(cursor.fetchone())
