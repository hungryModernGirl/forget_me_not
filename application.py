from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class FacebookUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(50))
    birthday_month = db.Column(db.Integer)
    birtday_day = db.Column(db.Integer)

    def __init__(self, username, email, name, month, day):
        self.username = username
        self.email = email
        self.name = name
        self.birthday_day = day
        self.birthday_month = month

    def __repr__(self):
        return '<User %r>' % self.username

app = Flask(__name__)

@app.route('/')
def create_form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
