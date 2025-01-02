from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
