import requests
from jsonschema import validate

url = "https://jsonplaceholder.typicode.com/todos/1"

schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "userId": {
      "type": "number"
    },
    "id": {
      "type": "number"
    },
    "title": {
      "type": "string"
    },
    "completed": {
      "type": "boolean"
    }
  },
  "required": [
    "userId",
    "id",
    "title",
    "completed"
  ]
}

response = requests.request("GET", url)
print(response.status_code)
assert response.status_code == 200
validate(instance=response.json(), schema=schema)
