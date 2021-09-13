import sqlite3
from contextlib import closing

with closing(sqlite3.connect("data.db")) as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("CREATE TABLE operations_db (id INTEGER PRIMARY KEY, name TEXT);")
        cursor.execute("INSERT INTO operations_db (name) VALUES ('addition');")
        connection.commit()

        cursor.execute("SELECT * FROM operations_db;")
        records = cursor.fetchall()
        print(records)
