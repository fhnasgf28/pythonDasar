import requests
import json

# URL API
url = "https://kttx1ae.hashmicro.com/api/v1/check/modules"

# Headers
headers = {
    "Content-Type": "application/json"
}

# Payload yang benar
payload = {
    "ModulesName": "Hash Core Package for Following Modules:",
    "ModulesList": [
        "Manufacturing",
        "CRM Module",
        "Sales Module",
        "Purchase Module",
        "Construction Module",
        "Inventory Module",
        "HRM"
    ]  # <- Harus berupa list JSON, bukan string
}

try:
    # Kirim request ke API
    response = requests.post(url, headers=headers, json=payload, timeout=10)
    # Gunakan `json=payload` agar otomatis dikonversi ke JSON valid

    response.raise_for_status()  # Raise error jika status bukan 2xx

    # Parse JSON response
    data = response.json()

    # Cetak hasil untuk debugging
    print("[SUCCESS] API Response:")
    print(json.dumps(data, indent=4))  # Pretty-print JSON
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Gagal mengakses API: {e}")
