import requests
import json

url = "https://kttx1ae.hashmicro.com/api/v1/check/modules"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "ModulesName": "<p>Hash Core Package for Following Modules: </p> <ul> <li> <p>Manufacture Management</p></li> <li> <p>CRM Sales Management<p><li><li><p>Inventory Management</p></li><li> <p>Accounting Management</p></li><li><p>Purchase Management</p></li> <li><p>Implementation Service</p></li><li> <p>Cloud Server &amp; Storage</p></li></ul>",
    "ModulesList": '["Manufacturing", "CRM Module", "Sales Module","Purchase Module","Construction Module","Inventory Module","HRM"]'
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
    response.raise_for_status()
    data = response.json()
    print(f"AI Response: {data}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
