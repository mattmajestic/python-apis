import requests

# Make a POST request to add data
response = requests.post('http://localhost:5000/post')
print("POST Code of :")
print(response.status_code)  # Should be 201 if successful

# Make a GET request to retrieve data
response = requests.get('http://localhost:5000/get')
print("GET Request Code of :")
print(response.status_code)  # Should be 200 if successful
print("GET JSON of :")
print(response.json())       # Contains the retrieved data