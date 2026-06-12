#!/usr/bin/python3
"""a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""
"""script should take 4 arguments: mysql username, mysql password, database name and state name searched"""
"""should connect to a MySQL server running on localhost at port 3306"""
"""Results must be sorted in ascending order by states.id"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
