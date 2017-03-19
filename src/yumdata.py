import requests
import csv
import os

username = os.environ['yum_username']
password = os.environ['yum_password']

headers = {'X-Yummly-App-ID':username,'X-Yummly-App-Key':password}
# print headers
url = 'http://api.yummly.com/v1/api/recipes?_app_id=app-id&_app_key=app-key&your_search_parameters'
print("Calling the API...")

# Store result from GET call as new variable called response
response = requests.get(url, headers=headers)

print(response.status_code)

# Convert response into JSON to a nested dictionary so we can interact with it.
print("Parsing JSON")
JSON = response.json()

print JSON

# f = csv.writer(open('YummlyData.csv', 'w'))
# for recipe in JSON['matches']:
