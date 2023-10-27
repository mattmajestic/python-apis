from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

data_file = 'data.json'

# Initialize data as an empty list or load from data.json if it exists
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        data = json.load(file)
else:
    data = []

@app.route('/get', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/post', methods=['POST'])
def add_item():
    data.append("1")  # Append "1" to the data
    save_data()
    return "Post Made!", 201

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
