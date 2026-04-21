import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@9771",
    database="day3_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

for row in cursor:
    print(row)