import requests

class Weather:
    def __init__(self,city, api_key):
        self.city = city
        self.api_key = api_key
        self.data = None

    def fetch_weather(self):
        """ Mengambil data cuaca dari API OpenWeatherMap """
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Error fetching weather data: {response.status_code}")

    def display_weather(self):
        """Menampilkan informasi cuaca"""
        if self.data:
            temperature = self.data['main']['temp']
            description = self.data['weather'][0]['description']
            print(f"Cuaca di {self.city}: {temperature}°C, {description}")
            print(f"Cuaca di {self.city}: {temperature}°C, {description}")
            print(f"Deskripsi: {self.data['weather'][0]['description']}")
            print(f"Kecepatan Angin: {self.data['wind']['speed']} m/s")
        else:
            print("Data cuaca belum diambil.")

if __name__ == "__main__":
    city = input("Masukkan nama kota: ")
    api_key = input("Masukkan API key OpenWeatherMap: ")
    weather = Weather(city, api_key)
    weather.fetch_weather()
    weather.display_weather()