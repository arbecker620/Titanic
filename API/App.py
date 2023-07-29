from flask import Flask, request, jsonify, make_response

# Create a Flask app
app = Flask(__name__)

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
