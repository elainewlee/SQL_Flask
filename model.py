import sqlite3
import datetime
import time


DB = None
CONN = None

def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect("tipsy.db")
	DB = CONN.cursor()
	 

def new_user(DB, id, email, password, name):
	query = """INSERT INTO Users VALUES	(NULL, ?,?,?)"""
	result = DB.execute(query, (id, email, password, name))
	CONN.commit()
	return result.lastrowid

#given a username and password, returns a dictionary of a user's fields pulled from the database, and a None if the credentials do not match
def authenticate(DB, name, password):
	query = """SELECT * FROM Users WHERE name=? AND password=?"""
	DB.execute(query, (name, password))
	result = DB.fetchone() #return ONE single from Users table matching row to the query
	CONN.commit()
	#Create a dictionary
	if result:
		#fields = ["name", "password"]
		fields = ["id", "email", "password", "name"] #This is the field/column name of the dictionary
		return dict(zip(fields, result)) #This returns a dictionary created from the zip pairing of the 4 text names in fields with the 4 values in result, which came fron the 4 columns in the Users table.
	else:
		return None #Else no username and password given, resulting in None

#Created a new task, returns the id of the newly created row. Make sure to populate the created_at field.
def new_task(DB, title, user_id):
	query = """SELECT * FROM Tasks WHERE title=? AND user_id=?"""
	DB.execute(query, (title, user_id))
	result = DB.execute(query, (title, user_id))
	CONN.commit()
	created_at = datetime.datetime(2013, 8, 4, 12, 30, 45)

	return result.lastrowid

# def main():
#     connect_to_db()
#     command = None
#     while command != "quit":
#         input_string = raw_input("HBA Database> ")
#         tokens = input_string.split()
#         command = tokens[0]
#         args = tokens[1:]

#         if command == "new_user":
#             new_user(*args) 
#         elif command == "authenticate":
#             authenticate(*args)
#         elif command == "new_task":
#             new_task(*args)

#     CONN.close()


# if __name__ == "__main__":
#     main()

