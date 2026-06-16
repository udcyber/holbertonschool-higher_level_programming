#!/usr/bin/python3
"""
A script, safe from MySQL injections, that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
# %s tells the library to treat the input as data, not code
# the comma after sys.argv[4] turns the value into a tuple
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    for state in cursor.fetchall():
        print(state)
    db.close()
