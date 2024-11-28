import socket
import requests

def get_ip_address():
    try:
        # mencoba mendapatkan IP public
        ip_public = requests.get('https://api.ipify.org').text.strip()
        return ip_public

    except requests.connectionError:
        # jika gagal, mencoba mendapatkan IP private
        ip_private = socket.gethostbyname(socket.gethostname())
        return ip_private

if __name__ == "__main__":
    ip_address = get_ip_address()
    print(f"IP address: {ip_address}")