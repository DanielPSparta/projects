import sqlite3
from contextlib import closing

def make_table():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE results_db (id INTEGER PRIMARY KEY, number1 INTEGER, number2 INTEGER, addition_func INTEGER, subtraction_func INTEGER, multiply_func INTEGER, division_func INTEGER);")
            connection.commit()

def table_insert(num1,num2,a,s,m,d):
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            command = f"INSERT INTO results_db (number1,number2,addition_func, subtraction_func, multiply_func, division_func ) VALUES ({num1},{num2},{a},{s},{m},{d});"
            cursor.execute(command)
            connection.commit()

def show_results():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM results_db;")
            records = cursor.fetchall()
            print(records)
            for item in records:
                print(item)
