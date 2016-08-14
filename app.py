from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#from flask.ext.sqlalchemy import SQLAlchemy
def create_app():
	app = Flask(__name__)
	Bootstrap(app)

	return app


#app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)

@app.route("/")
def main():
	return render_template('index.html')  #render_template('index.html') #all templates in folder

@app.route("/first")
def second():
	return "Hello world"

#returns website
#@app.route("/<username>")
#def profile(username):
#	return render_template('profile.html', name = username)


#@app.route("/second/<username>") #creating username as a variable
#def third(username): #username is ARGV
#	return "Hello " + username + "!!!" #magic!


if __name__ == "__main__":
	app.run(debug = True)

