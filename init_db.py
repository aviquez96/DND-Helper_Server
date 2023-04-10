import os
import psycopg2

connection = psycopg2.connect(
    host="localhost", database="postgres", user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"]
)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS character;")

cursor.execute(
    "CREATE TABLE character (id serial PRIMARY KEY,"
    "first varchar (150) NOT NULL,"
    "date_added date DEFAULT CURRENT_TIMESTAMP);"
)

cursor.execute("INSERT INTO character (first)" "VALUES ('Jhazar')")
cursor.execute("INSERT INTO character (first)" "VALUES ('Arras')")

connection.commit()

cursor.close()
connection.close()
