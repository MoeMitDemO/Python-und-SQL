from os import P_WAIT
import sqlite3, mysql.connector
from sqlite3 import Error
from mysql.connector import Error
from io import open


host = input("Hostadresse: ")
user = input("Benutzer: ")
pw = input("Passwort: ")
db = input("Datenbank: ")

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Verbindung zur MEINEFORTSETZUNG DATENBANK erfolgreich aufgebaut")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#"localhost", "root", "", "python-test"
connection = create_connection(host, user, pw, db)

mycursor = connection.cursor()

ziel = input("Name der auszugebenden Tabelle:")
executeString = "SELECT * FROM " + ziel
mycursor.execute(executeString)
ausgabe = ""
for x in mycursor:
    ausgabe += str(x) + "\n"

print(ausgabe)

f = open("log.txt", mode="w", encoding="utf-8")
f.write(ausgabe)