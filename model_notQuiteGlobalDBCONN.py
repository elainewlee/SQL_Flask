import sqlite3
import datetime

DB = None
CONN = None

def connect_DB():
	global DB, CONN
	return sqlite3.connect("tipsy.DB")

def new_user(DB, email, password, name):
	c = DB.cursor()
	query = """INSERT INTO Users VALUES	(NULL, ?,?,?)"""
	result = c.execute(query, (email, password, name))
	DB.commit()
	return result.lastrowid

def authenticate(DB, username, password):
	c = DB.cursor()
	query = """SELECT * FROM Users WHERE email=? AND password=?"""
	c.execute(query, (email, password))
	result = c.fetchone() #return ONE single from Users table matching row to the query
	#Create a dictionary
	if result:
		fields = ["id", "email", "password", "username"] #This is the field/column name of the dictionary
		return dict(zip(fields, result)) #This returns a dictionary created from the zip pairing of the 4 text names in fields with the 4 values in result, which came fron the 4 columns in the Users table.
	else:
		return None #Else no username and password given, resulting in None

def new_task(DB, title, user_id):
	c = DB.cursor()
	query = """SELECT * FROM Users WHERE title=? AND user_id=?"""
	c.execute(query, (title, user_id))
	result = c.execute(query, (title, user_id))
	created_at = datetime.datetime(c)

	return result.lastrowid

def main():
    connect_to_DB()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "new_user":
            new_user(*args) 
        elif command == "authenticate":
            authenticate(*args)
        elif command == "new_task":
            new_task(*args)

    CONN.close()


if __name__ == "__main__":
    main()

