from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Define a route and its corresponding function
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/prediction', methods = ['GET', 'POST'])
def predict():
    content = request.jsonify

    return content

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()
