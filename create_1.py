import sqlite3

conn = sqlite3.connect("mydb.sqlite3")
cr = conn.cursor()


query = """CREATE TABLE users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
					first_name TEXT, last_name TEXT DEFAULT NULL, 
					username TEXT UNIQUE DEFAULT NULL, phone_number INTEGER, 
					photo BLOB DEFAULT '',
					bio TEXT DEFAULT '')"""

cr.execute(query)