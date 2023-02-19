import json
import requests

headers = {"Content-Type": "application/json"}

url = "http://0.0.0.0:8000/process_text"
payload = ('{"text": "This is a sample text"}')
response = requests.request("POST", url, data=payload, headers=headers)
print("POST /process_text")
print(f"{payload}")
print("Response:")
print(json.dumps(response.json(), indent=4))
print()
