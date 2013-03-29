from flask import Flask, render_template, request, redirect
import model


# Initialize program to be a Flask application
# Flask is a class
# App is instantation of Flask class
# First parameter is name of the module(file) that we're doing this from
app = Flask(__name__)

# Tells Flask what URL (route) is attached to this function
# Return value sent to browser
@app.route("/") #'decorator' that tells Flask what url (route) is attached to this function
def index():
	return render_template("index.html", name="Lani")

@app.route("/tasks")
def list_tasks():
	db = model.connect_to_db() # connect to the database
	tasks_from_db = model.get_tasks(db, None) # get a list of all the tasks
	return render_template("list_tasks.html", tasks= tasks_from_db) #send that list to the list_tasks template as a parameter named "tasks"

@app.route("/new_task")
def new_tasks():
	return render_template("new_task.html")

@app.route("/save_task", methods=["POST"]) #This url will respond to POSTed forms, rather than plain url requests.
def save_task():
	task_title = request.form['task_title']
	db = model.connect_to_db()
	#Assume that all tasks are attached to user 1.
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")
# Start our application server/web server/flask application when we run our program from the command line.
# Start server in debug mode (to keep things simple)
if __name__ == "__main__":
		app.run(debug=True)