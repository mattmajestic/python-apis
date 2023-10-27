import requests

# Make a GET request to retrieve data
response = requests.get('http://localhost:8000/get')
print(response.status_code)  # Should be 200 if successful
print(response.json())       # Contains the retrieved data

# Make a POST request to add data
response = requests.post('http://localhost:8000/post')
print(response.status_code)  # Should be 201 if successful
