import requests
import json

# Endpoint API
url = "https://kttx1ae.hashmicro.com/api/v1/check/modules"

# Data yang dikirim ke API
payload = {
    "ModulesName": 1,
    "ModulesList": 1,
    "Sales Module": 1,
    "Purchase Module": 1,
    "Construction Module": 0,
    "Inventory Module": 1,
    "HRM": 0
}

# Header (tidak perlu auth jika tidak dibutuhkan)
headers = {
    "Content-Type": "application/json"
}

try:
    # Kirim request ke API
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)

    # Cek status response
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
