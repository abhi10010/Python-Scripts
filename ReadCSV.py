#A simple code that reads a csv file from a sqlite database to display the required information using the library sqlite3

import sqlite3
conn = sqlite3.connect("New.db")
print("Db opened!!")
sql_command = "SELECT field21, Count(*) FROM orders GROUP BY field21 ORDER BY 2"
print("SQL Command Running!")
cursor = conn.execute(sql_command)
for row in cursor:
    print("STYLECODE = ")
    print(row[0])
    print("Count = ", row[1], "\n")
conn.commit()
conn.close()
