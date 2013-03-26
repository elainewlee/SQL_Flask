from flask import Flask, render_template
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
		return render_template("index.html")

# Start our application server/web server/flask application when we run our program from the command line.
# Start server in debug mode (to keep things simple)
if __name__ == "__main__":
		app.run(debug=True)
