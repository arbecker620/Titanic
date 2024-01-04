from flask import Flask, request, jsonify, make_response

# Create a Flask app
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from os import environ

DB_URL= 'postgresql://postgres:postgres@flask_db:5432/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL


db = SQLAlchemy(app)


class Passenger(db.Model):
    __tablename__ = 'Passengers'

    PassengerId =  db.Column(db.Integer, primary_key =True)
    Name= db.Column(db.String(80), unique=True, nullable=False)
    Pclass = db.Column(db.String(80), unique=False, nullable=False)
    Sex = db.Column(db.String(80), unique=False, nullable=False)
    Age = db.column(db.Float)
    SibSp = db.Column(db.Integer, primary_key=False)
    Parch = db.Column(db.Integer, primary_key =False)
    Ticket = db.Column(db.String(80), unique=False, nullable=False)
    Fare = db.Column(db.Integer, primary_key =False)
    Cabin = db.Column(db.String(80), unique=False, nullable=False)
    Embarked = db.Column(db.String(80), unique=True, nullable=False)
# Define a route and its corresponding function
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/prediction', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        content = request.get_json()
        

    return make_response(jsonify(content), 200)

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()
