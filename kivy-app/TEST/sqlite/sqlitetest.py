"""This code was created to test the sqlite DB creation test. The issue in question is when moving the application around the
table manga_list will likely not prexist in the same directory as specified especially after packaging up the application
to resolve this I will create an exception handler where instead of using an existing sqlite.db file I will have the application
create a *.db file along with the table manga_list and have it store it in the file directory system of the application"""
import sqlite3
from sqlite3 import Error
import os.path

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "sqlite.db")
    database = db_path
    conn = sqlite3.connect(database)
    cur = conn.cursor()  # create sqlite cursor object allowing sql statements to be executed
    cur.execute("SELECT * FROM manga_list")
except sqlite3.OperationalError as e:
    with conn:
        cur.execute("CREATE TABLE manga_list (id    INTEGER PRIMARY KEY,name  STRING,url   STRING,image STRING);")
    print(e)

    


cur = conn.cursor()  # create sqlite cursor object allowing sql statements to be executed
cur.execute("SELECT * FROM manga_list")
# creates list of manga_list table allowing for loop to run and populate the BoxLayout
db_list = cur.fetchall()
print(db_list)
