import requests
import json
from datetime import datetime
from typing import Dict, List, Optional

class WeatherPredictor:
    """
    Kelas untuk memprediksi dan menganalisis data cuaca
    menggunakan API OpenWeatherMap (free tier)
    """
    
    def __init__(self, api_key: str):
        """
        Inisialisasi Weather Predictor
        
        Args:
            api_key: API key dari OpenWeatherMap
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.weather_data = None
        
    def get_current_weather(self, city: str, country_code: str = None) -> Optional[Dict]:
        """
        Mendapatkan data cuaca saat ini untuk kota tertentu
        
        Args:
            city: Nama kota
            country_code: Kode negara (opsional)
            
        Returns:
            Dictionary berisi data cuaca atau None jika error
        """
        try:
            location = f"{city},{country_code}" if country_code else city
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'  # Menggunakan Celsius
            }
            
            response = requests.get(f"{self.base_url}/weather", params=params)
            response.raise_for_status()
            
            self.weather_data = response.json()
            return self.weather_data
            
        except requests.exceptions.RequestException as e:
            print(f"Error mengambil data cuaca: {e}")
            return None
    
    def get_forecast(self, city: str, country_code: str = None, days: int = 5) -> Optional[Dict]:
        """
        Mendapatkan prediksi cuaca untuk beberapa hari ke depan
        
        Args:
            city: Nama kota
            country_code: Kode negara (opsional)
            days: Jumlah hari prediksi (max 5 untuk free tier)
            
        Returns:
            Dictionary berisi data prediksi atau None jika error
        """
        try:
            location = f"{city},{country_code}" if country_code else city
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric',
                'cnt': min(days * 8, 40)  # API memberikan data per 3 jam
            }
            
            response = requests.get(f"{self.base_url}/forecast", params=params)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error mengambil prediksi cuaca: {e}")
            return None
    
    def parse_current_weather(self) -> Optional[Dict]:
        """
        Mengparse dan menyederhanakan data cuaca saat ini
        
        Returns:
            Dictionary dengan informasi cuaca yang rapi
        """
        if not self.weather_data:
            return None
        
        data = self.weather_data
        parsed = {
            'kota': data.get('name'),
            'negara': data.get('sys', {}).get('country'),
            'koordinat': {
                'latitude': data.get('coord', {}).get('lat'),
                'longitude': data.get('coord', {}).get('lon')
            },
            'cuaca': data.get('weather', [{}])[0].get('main'),
            'deskripsi': data.get('weather', [{}])[0].get('description'),
            'temperatur': {
                'saat_ini': data.get('main', {}).get('temp'),
                'terasa_seperti': data.get('main', {}).get('feels_like'),
                'minimum': data.get('main', {}).get('temp_min'),
                'maksimum': data.get('main', {}).get('temp_max')
            },
            'kelembaban': data.get('main', {}).get('humidity'),
            'tekanan': data.get('main', {}).get('pressure'),
            'kecepatan_angin': data.get('wind', {}).get('speed'),
            'arah_angin': data.get('wind', {}).get('deg'),
            'awan': data.get('clouds', {}).get('all'),
            'visibilitas': data.get('visibility'),
            'waktu_pengambilan': datetime.fromtimestamp(data.get('dt')).strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return parsed
    
    def predict_weather_condition(self, forecast_data: Dict) -> List[Dict]:
        """
        Memprediksi kondisi cuaca dari data forecast
        
        Args:
            forecast_data: Data forecast dari API
            
        Returns:
            List berisi prediksi cuaca untuk setiap periode
        """
        predictions = []
        
        if 'list' not in forecast_data:
            return predictions
        
        for item in forecast_data['list']:
            prediction = {
                'waktu': datetime.fromtimestamp(item.get('dt')).strftime('%Y-%m-%d %H:%M:%S'),
                'temperatur': item.get('main', {}).get('temp'),
                'cuaca': item.get('weather', [{}])[0].get('main'),
                'deskripsi': item.get('weather', [{}])[0].get('description'),
                'kelembaban': item.get('main', {}).get('humidity'),
                'kemungkinan_hujan': item.get('pop', 0) * 100,  # Probability of precipitation
                'kecepatan_angin': item.get('wind', {}).get('speed')
            }
            predictions.append(prediction)
        
        return predictions
    
    def display_current_weather(self):
        """Menampilkan data cuaca saat ini dengan format yang rapi"""
        parsed = self.parse_current_weather()
        
        if not parsed:
            print("Data cuaca tidak tersedia")
            return
        
        print("\n" + "="*50)
        print("📍 CUACA SAAT INI")
        print("="*50)
        print(f"Kota: {parsed['kota']}, {parsed['negara']}")
        print(f"Waktu: {parsed['waktu_pengambilan']}")
        print(f"Cuaca: {parsed['deskripsi'].title()}")
        print(f"\n🌡️  Temperatur:")
        print(f"   Saat ini: {parsed['temperatur']['saat_ini']}°C")
        print(f"   Terasa seperti: {parsed['temperatur']['terasa_seperti']}°C")
        print(f"   Min: {parsed['temperatur']['minimum']}°C | Max: {parsed['temperatur']['maksimum']}°C")
        print(f"\n💨 Angin: {parsed['kecepatan_angin']} m/s")
        print(f"💧 Kelembaban: {parsed['kelembaban']}%")
        print(f"☁️  Awan: {parsed['awan']}%")
        print(f"🔍 Visibilitas: {parsed['visibilitas']/1000:.1f} km")
        print("="*50 + "\n")
    
    def display_forecast(self, predictions: List[Dict]):
        """Menampilkan prediksi cuaca dengan format yang rapi"""
        print("\n" + "="*70)
        print("📅 PREDIKSI CUACA (5 HARI KE DEPAN)")
        print("="*70)
        
        for idx, pred in enumerate(predictions, 1):
            print(f"\n[{idx}] {pred['waktu']}")
            print(f"    Temperatur: {pred['temperatur']}°C")
            print(f"    Cuaca: {pred['deskripsi'].title()}")
            print(f"    Kelembaban: {pred['kelembaban']}%")
            print(f"    Kemungkinan Hujan: {pred['kemungkinan_hujan']:.1f}%")
            print(f"    Angin: {pred['kecepatan_angin']} m/s")
        
        print("\n" + "="*70 + "\n")


def main():
    """Fungsi utama untuk demonstrasi"""
    # CATATAN: Ganti dengan API key Anda dari https://openweathermap.org/api
    API_KEY = "your_api_key_here"
    
    # Cek apakah API key sudah diset
    if API_KEY == "your_api_key_here":
        print("⚠️  Silakan atur API_KEY terlebih dahulu!")
        print("Dapatkan API key gratis dari: https://openweathermap.org/api")
        return
    
    # Inisialisasi predictor
    predictor = WeatherPredictor(API_KEY)
    
    # Contoh penggunaan
    print("🌤️  Aplikasi Prediksi Cuaca\n")
    
    # Ambil cuaca saat ini untuk Jakarta
    city = "Jakarta"
    print(f"Mengambil data cuaca untuk {city}...")
    
    weather = predictor.get_current_weather(city, "ID")
    if weather:
        predictor.display_current_weather()
    
    # Ambil prediksi cuaca
    print(f"Mengambil prediksi cuaca untuk {city}...")
    forecast = predictor.get_forecast(city, "ID", days=5)
    if forecast:
        predictions = predictor.predict_weather_condition(forecast)
        predictor.display_forecast(predictions)
    
    # Simpan data ke file JSON
    if weather and forecast:
        output_data = {
            'cuaca_saat_ini': predictor.parse_current_weather(),
            'prediksi': predictions,
            'waktu_pengambilan_data': datetime.now().isoformat()
        }
        
        with open('weather_data.json', 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print("✅ Data cuaca berhasil disimpan ke 'weather_data.json'")


if __name__ == "__main__":
    main()
