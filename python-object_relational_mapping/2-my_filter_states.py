#!/usr/bin/python3
"""
Take in an argument and display all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                   WHERE BINARY name = '{}' \
                   ORDER BY states.id ASC".format(sys.argv[4]))
    [print(state) for state in cursor.fetchall()]
    db.close()
