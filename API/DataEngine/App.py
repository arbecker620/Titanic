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
    Age = db.column(db.float)
    SibSp = db.Column(db.Integer, primary_key=False)
    Parch = db.Column(db.Integer, primary_key =False)
    Ticket = db.Column(db.String(80), unique=False, nullable=False)
    Fare = db.Column(db.Integer, primary_key =False)
    Cabin = db.Column(db.String(80), unique=False, nullable=False)
    Embarked = db.Column(db.String(80), unique=True, nullable=False)

# Define a route and its corresponding function
@app.route('/home')
def hello():
    return 'Hello, World!'


@app.route('/passengers', methods = ['GET'])
"""
This returns back of all of the Passengers, if there is no data to return we get a 500 error.

"""
def get_passengers():
    try:
        passengers = Passenger.query.all()
        return make_response(jsonify([passengers.json() for passenger in passengers]), 200)
    except e:
        return make_response(jsonify(content), 500)

@app.route('/passengers/<int:id>', methods=['GET'])
def get_passenger(id):
    try:
        passenger = Passenger.query.filter_by(id=id).first()
        if passernger:
            return make_response(jsonify({'user': passenger.json()}), 200)
        else:
            return make_response(jsonify({'message': 'user not found'}), 404)
    except e:
        return make_response(jsonify({'message': 'error getting user'}), 500)

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=443)
