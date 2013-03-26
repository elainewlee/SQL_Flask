import sqlite3
import datetime


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

#Creates a new task, returns the id of theturn the user as a dictionary, like our authenticate method. newly created row. Make sure to populate the created_at field.
def new_task(DB, title, user_id): #(DB, id, title, created_at, completed_at, user_id):
	query = """INSERT INTO Tasks VALUES (NULL, ?,?, NULL, ?)"""#(id, title, created_at, completed_at, user_id)"""
	t = datetime.datetime.utcnow() # t = created_at
	result = DB.execute(query, (title, t, user_id))
	CONN.commit()
	return result.lastrowid


def get_user(DB, id): #Fetch a user's record based on his id. Return the user as a dictionary, like our authenticate method.
	query = """SELECT * FROM Users WHERE id=?"""
	DB.execute(query,(id))
	result = DB.fetchone()
	CONN.commit()
	#Create a dictionary
	if result:
		fields = ["id", "email", "password", "name"] #Fields is the column name of the dictionary
		return dict(zip(fields, result)) #This returns a dictionary created from the zip pairing of the 4 text names in fields with the 4 values in result, which came fron the 4 columns in the Users table.
	else:
		return None #Else no username and password given, resulting in None

def complete_task(DB, id): #Marks a task as being complete, setting the completed_at field.
	completed_at = datetime.datetime.utcnow() 
	query = """UPDATE Tasks SET completed_at = ? WHERE id=?""" # t = completed_at
	result = DB.execute(query,(completed_at, id))

	CONN.commit()
	return id	

def get_tasks(DB, user_id=None): #Gets all the tasks for the given user id. Returns all the tasks in the system if no user_id is given. Returns them as a list of dictionaries.
	
	if user_id == None: #Returns all the tasks in the system if no user_id is given.
		query = """SELECT * FROM Tasks"""
		cursor = DB.execute(query)
		rows = cursor.fetchall()		
		return rows
	else: #Gets all the tasks for the given user id.Returns them as a list of dictionaries.
		query = """SELECT * FROM Tasks WHERE user_id=?"""
		cursor = DB.execute(query,(user_id, )) # Tuple of
		rows = cursor.fetchall()	
		return rows

	tasks = []
	for row in rows: #add individual tasks to task list
		task = dict(zip(["id","title", "created_at", "completed_at", "user_id"], row))
		tasks.append(tasks)
	return tasks


def get_task(DB, id): #Get a single task, given its id. Return the task as a dictionary as above in the authenticate method.
	query = """SELECT * FROM Tasks WHERE id=?"""
	DB.execute(query,(id))
	result = DB.fetchone()
	CONN.commit()
	#Create a dictionary
	if result:
		fields = ["id", "title", "created_at", "completed_at", "user_id"] #Fields is the column name of the dictionary
		return dict(zip(fields, result)) #This returns a dictionary created from the zip pairing of the 4 text names in fields with the 4 values in result, which came fron the 4 columns in the Users table.
	else:
		return None #Else no username and password given, resulting in None

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
