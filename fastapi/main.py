from fastapi import FastAPI, HTTPException
import json
import uvicorn

app = FastAPI()

# Initialize data as an empty list or load from data.json if it exists
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

@app.get('/get')
async def read_items():
    return data

@app.post('/post')
async def create_item():
    data.append("1")  # Append the value from the request body to the data list
    save_data()
    return "Post Made!"

def save_data():
    with open('data.json', 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
