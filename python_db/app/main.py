import mysql.connector as sql

print("Welcome to python & db app")

try:
    #
    with sql.connect(host= "localhost", user= "root", password="my_secret_password",database="test_from_python_db") as conn_var:  #opens a connection with a database
        print(conn_var)      #this is used to pass the sql commands
        cursor = conn_var.cursor()
        #cursor.execute("CREATE DATABASE test_from_python_db;")
        #cursor.execute("SHOW DATABASES;")
        #cursor.execute("SHOW TABLES;")

        #command = "CREATE TABLE app_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), score INT);"

        #name_var = "Kali"
        #score_var = 10
        #command = f"INSERT INTO app_table (name,score) VALUES ('{name_var}', {score_var});"
        #cursor.execute(command)
        #conn_var.commit() #commit the data to the table

        command = "SELECT * FROM app_table;"   #get everything from the db
        cursor.execute(command)
        rows = cursor.fetchall()        #cursor fteches all the results
        print(rows)
        for item in rows:
            print(item)
            print(item[0])
            print(item[1])
            print(item[2])

        #print(cursor)
        #for item in cursor:
        #    print(item)
except Exception as e:
    raise
