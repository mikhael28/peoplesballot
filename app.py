from flask import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route("/")
def main():
	return render_template('index.html') #all templates in folder

@app.route("/first")
def second():
	return "Hello World"

#returns website
@app.route("/<username>")
def profile(username):
	return render_template('profile.html', name = username)

#returns piece of Data in JSON, uses dictionary
@app.route("/lotsofdata")
def people():
	my_people = {'Alice':25,
				'Bob':21,
				'Charlie':20,
				'Doug':28}
	return jsonify(my_people)


@app.route("/second/<username>") #creating username as a variable
def third(username): #username is ARGV
	return "Hello " + username + "!!!" #magic!


if __name__ == "__main__":
	app.run(debug = True)

