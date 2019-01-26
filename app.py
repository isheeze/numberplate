from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pakistan_786@localhost/invoice_management_DB'
db = SQLAlchemy(app)

@app.route('/')
@app.route('/<user>')
def index(user = None):	
    return render_template("index.html", user=user)

@app.route('/login/<lt>') # login type i.e. signup or login
def login(lt = None):
    return render_template("login.html", lt=lt)

@app.route('/profile/<id>')
def profile(id):
	return render_template("profile.html", id=id)

# url rules
app.add_url_rule('/','index',index)

if __name__ == '__main__':
	app.debug = True
	app.run()