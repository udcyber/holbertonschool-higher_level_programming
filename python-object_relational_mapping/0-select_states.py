#!/usr/bin/python3
"""lists all states from the database htbn_0e_0_usa
take 3 arguments: <mysql username>, <mysql password> and <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    rows_number = curs.execut("SELECT * FROM states ORDER BY states.id")
    for i in range(rows_number):
        print(curs.fetchone())
