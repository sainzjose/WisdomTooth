import requests

# Set the URL for the API endpoint
url = "https://mb-api.abuse.ch/api/v1/sample/"

# Set the API key (replace with your own key)
api_key = "your-api-key"

# Set the parameters for the API call (e.g. a hash value to search for)
params_hash = {"hash": "example-hash-value"}
params_tag = {"tag": "example-tag-1,example-tag-2"}

# Make the API call using the requests module
response = requests.get(url, params=params_hash, headers={"API-Key": api_key})

# Check the status code of the response
if response.status_code == 200:
    # The API call was successful, and the data can be accessed from the "response" object
    data = response.json()
    print(data)
else:
    # The API call was not successful, and an error occurred
    print("Error:", response.status_code)