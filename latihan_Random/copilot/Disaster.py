import json
from datetime import datetime
from enum import Enum

class DisasterType(Enum):
    """Enum untuk tipe-tipe bencana"""
    EARTHQUAKE = "Gempa Bumi"
    FLOOD = "Banjir"
    LANDSLIDE = "Tanah Longsor"
    TSUNAMI = "Tsunami"
    VOLCANO = "Gunung Berapi"
    STORM = "Badai"
    DROUGHT = "Kekeringan"
    FIRE = "Kebakaran"

class DisasterDetector:
    """Kelas untuk mendeteksi bencana berdasarkan parameter lingkungan"""
    
    def __init__(self):
        self.alerts = []
    
    def check_earthquake(self, magnitude: float) -> bool:
        """
        Mendeteksi gempa bumi berdasarkan magnitudo
        magnitude < 3.0: Lemah
        3.0 - 5.0: Sedang
        > 5.0: Kuat (Bencana)
        """
        if magnitude > 5.0:
            self.log_alert(DisasterType.EARTHQUAKE, f"Magnitude: {magnitude}")
            return True
        return False
    
    def check_flood(self, rainfall_mm: float, water_level_cm: float) -> bool:
        """
        Mendeteksi banjir berdasarkan curah hujan dan ketinggian air
        """
        if rainfall_mm > 100 or water_level_cm > 200:
            self.log_alert(DisasterType.FLOOD, 
                          f"Curah Hujan: {rainfall_mm}mm, Level Air: {water_level_cm}cm")
            return True
        return False
    
    def check_landslide(self, slope_angle: float, soil_saturation: float) -> bool:
        """
        Mendeteksi tanah longsor berdasarkan sudut lereng dan saturasi tanah
        slope_angle: derajat
        soil_saturation: 0-100 (persentase)
        """
        if slope_angle > 45 and soil_saturation > 80:
            self.log_alert(DisasterType.LANDSLIDE,
                          f"Sudut Lereng: {slope_angle}°, Saturasi Tanah: {soil_saturation}%")
            return True
        return False
    
    def check_tsunami(self, earthquake_magnitude: float, depth_km: float, 
                     distance_from_coast_km: float) -> bool:
        """
        Mendeteksi tsunami berdasarkan parameter gempa
        """
        if earthquake_magnitude > 7.0 and depth_km < 70 and distance_from_coast_km < 100:
            self.log_alert(DisasterType.TSUNAMI,
                          f"Mag: {earthquake_magnitude}, Kedalaman: {depth_km}km, Jarak Pantai: {distance_from_coast_km}km")
            return True
        return False
    
    def check_volcano(self, tremor_frequency: int, gas_emission_ppm: float) -> bool:
        """
        Mendeteksi aktivitas gunung berapi
        tremor_frequency: jumlah gempa dalam 1 jam
        gas_emission_ppm: emisi gas dalam PPM
        """
        if tremor_frequency > 10 or gas_emission_ppm > 500:
            self.log_alert(DisasterType.VOLCANO,
                          f"Frekuensi Gempa: {tremor_frequency}/jam, Emisi Gas: {gas_emission_ppm}ppm")
            return True
        return False
    
    def check_storm(self, wind_speed_kmh: float, temperature_celsius: float) -> bool:
        """
        Mendeteksi badai berdasarkan kecepatan angin dan suhu
        """
        if wind_speed_kmh > 100 or temperature_celsius < 0:
            self.log_alert(DisasterType.STORM,
                          f"Kecepatan Angin: {wind_speed_kmh}km/h, Suhu: {temperature_celsius}°C")
            return True
        return False
    
    def check_drought(self, rainfall_mm_monthly: float, humidity_percent: float) -> bool:
        """
        Mendeteksi kekeringan
        """
        if rainfall_mm_monthly < 50 and humidity_percent < 30:
            self.log_alert(DisasterType.DROUGHT,
                          f"Curah Hujan Bulanan: {rainfall_mm_monthly}mm, Kelembaban: {humidity_percent}%")
            return True
        return False
    
    def check_fire(self, temperature_celsius: float, humidity_percent: float, 
                  wind_speed_kmh: float) -> bool:
        """
        Mendeteksi potensi kebakaran
        """
        if temperature_celsius > 35 and humidity_percent < 20 and wind_speed_kmh > 20:
            self.log_alert(DisasterType.FIRE,
                          f"Suhu: {temperature_celsius}°C, Kelembaban: {humidity_percent}%, Angin: {wind_speed_kmh}km/h")
            return True
        return False
    
    def log_alert(self, disaster_type: DisasterType, details: str):
        """Mencatat alert bencana"""
        alert = {
            "timestamp": datetime.now().isoformat(),
            "disaster_type": disaster_type.value,
            "details": details
        }
        self.alerts.append(alert)
        print(f"⚠️  ALERT BENCANA: {disaster_type.value}")
        print(f"   Waktu: {alert['timestamp']}")
        print(f"   Detail: {details}\n")
    
    def get_alerts(self) -> list:
        """Mendapatkan semua alert"""
        return self.alerts
    
    def clear_alerts(self):
        """Menghapus semua alert"""
        self.alerts = []


# Contoh penggunaan
if __name__ == "__main__":
    detector = DisasterDetector()
    
    print("=" * 50)
    print("SISTEM DETEKSI BENCANA SEDERHANA")
    print("=" * 50 + "\n")
    
    # Test: Deteksi gempa bumi
    print("🔍 Test 1: Deteksi Gempa Bumi")
    detector.check_earthquake(magnitude=6.5)
    
    # Test: Deteksi banjir
    print("🔍 Test 2: Deteksi Banjir")
    detector.check_flood(rainfall_mm=150, water_level_cm=250)
    
    # Test: Deteksi tanah longsor
    print("🔍 Test 3: Deteksi Tanah Longsor")
    detector.check_landslide(slope_angle=50, soil_saturation=85)
    
    # Test: Deteksi tsunami
    print("🔍 Test 4: Deteksi Tsunami")
    detector.check_tsunami(earthquake_magnitude=7.8, depth_km=50, distance_from_coast_km=80)
    
    # Test: Deteksi aktivitas gunung berapi
    print("🔍 Test 5: Deteksi Gunung Berapi")
    detector.check_volcano(tremor_frequency=15, gas_emission_ppm=600)
    
    # Test: Deteksi badai
    print("🔍 Test 6: Deteksi Badai")
    detector.check_storm(wind_speed_kmh=120, temperature_celsius=5)
    
    # Test: Deteksi kekeringan
    print("🔍 Test 7: Deteksi Kekeringan")
    detector.check_drought(rainfall_mm_monthly=30, humidity_percent=15)
    
    # Test: Deteksi kebakaran
    print("🔍 Test 8: Deteksi Kebakaran")
    detector.check_fire(temperature_celsius=40, humidity_percent=10, wind_speed_kmh=30)
    
    # Tampilkan semua alert
    print("=" * 50)
    print("RINGKASAN ALERT")
    print("=" * 50)
    print(f"Total Alert: {len(detector.get_alerts())}")
    print(json.dumps(detector.get_alerts(), indent=2, ensure_ascii=False))
