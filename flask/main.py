from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Initialize data as an empty list or load from data.json if it exists
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

# Route for the root URL ("/") to handle any requests to the root
@app.route('/')
def root():
    return "Welcome to the Flask API!"

# Route for "/get" to return the data
@app.route('/get', methods=['GET'])
def read_items():
    return jsonify(data)

# Route for "/post" to create an item with a GET request
@app.route('/post', methods=['GET'])
def create_item():
    data.append("Added to json with POST")
    save_data()
    return "Post Made!"

def save_data():
    with open('data.json', 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
