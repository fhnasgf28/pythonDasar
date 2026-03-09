import requests
import json

class TestAPI:
    def fetch_modules_from_ai(self, description_text):
        url_modules = "https://kttx1ae.hashmicro.com/api/v1/check/modules"
        headers = {
            "Content-Type": "application/json"
        }
        payload_modules = {
            "ModulesName": description_text if description_text else "No Description",
            "ModulesList": "[ 'Manufacturing', 'CRM Module', 'Sales Module', 'Purchase Module', 'Construction Module', 'Inventory Module', 'HRM']"
        }

        try:
            response = requests.post(url_modules, headers=headers, data=json.dumps(payload_modules), timeout=10)
            response.raise_for_status()
            response_data = response.json()
            print("Response from API:")
            print(json.dumps(response_data, indent=4))
            return response_data
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return {"error": f"Request failed: {e}"}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {"error": f"Invalid JSON response: {e}"}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"error": f"An unexpected error occurred: {e}"}

    # Fungsi untuk meminta input dari pengguna dan menguji API
    def test_fetch_modules_from_ai(self):
        description_text = input("Masukkan ModulesName: ")
        self.fetch_modules_from_ai(description_text)

if __name__ == "__main__":
    test_api = TestAPI()
    test_api.test_fetch_modules_from_ai()
