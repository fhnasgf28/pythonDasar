import requests
import json

url = "https://kttx1ae.hashmicro.com/api/v1/check/industries"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "CompanyName": "Google Inc.",
    "Industries": "['Manufacturing', 'Retail', 'F&B', 'Services', 'IT']"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
    response.raise_for_status()
    data = response.json()
    print(f"AI Response: {data}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
