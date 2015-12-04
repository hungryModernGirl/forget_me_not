from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from facepy import GraphAPI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
access_token = r'CAACEdEose0cBAJX8daxev07ZC2eLXAnDiOM66ORF8KLGwQMYBQocrh8IKyjoLwMCAb0JbyPst5ibcVtrsjbl7BZCrDFZCY6Hby5zSJ8BlE1p3zF94OidD78cQmVCjuUZBlZB82Bhw7eCo3JIqOUFZCpdkPEVM9uY1YUzCb8y5oBZAvR3jpDNEEsaQ6ZCEjk7QYM7OZBJFEzLnDKn3ZCeLgDx0T'

graph = GraphAPI(
    access_token,
    version='2.5',
    timeout=30,
)



class FacebookUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(50))
    birthday_month = db.Column(db.Integer)
    birtday_day = db.Column(db.Integer)
    friends = db.relationship('FacebookUser')
    user_access_token = db.Column(db.String(500))

    def __init__(self, username, email, name, month, day, token, friends_list):
        self.username = username
        self.email = email
        self.name = name
        self.birthday_day = day
        self.birthday_month = month
        self.user_access_token = token


    def __repr__(self):
        return '<User %r>' % self.username

app = Flask(__name__)

@app.route('/join')
def create_():
    return 'Hello World!'


@app.route('/edit')
def configure():
    d = {

    }



if __name__ == '__main__':
    app.run()
