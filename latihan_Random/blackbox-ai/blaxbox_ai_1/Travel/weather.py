import requests


def get_weather(location):
    api_key = 'YOUR_API_KEY'  # Ganti dengan API key Anda dari OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f"{temperature}°C, {description}"
        else:
            return "Lokasi tidak ditemukan."
    except Exception as e:
        return str(e)