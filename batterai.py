"""
Script untuk menghitung kemungkinan baterai habis
Kondisi awal: 100%
"""

class BatteryCalculator:
    """Kelas untuk menghitung proyeksi baterai"""
    
    def __init__(self, current_percentage=100):
        """
        Inisialisasi Battery Calculator
        
        Args:
            current_percentage (int): Persentase baterai saat ini (default: 100)
        """
        self.current_percentage = current_percentage
        self.consumption_history = []
    
    def add_consumption_rate(self, rate_per_hour):
        """
        Tambahkan rate konsumsi baterai per jam
        
        Args:
            rate_per_hour (float): Persentase baterai yang habis per jam
        """
        self.consumption_history.append(rate_per_hour)
    
    def calculate_time_remaining(self, consumption_rate):
        """
        Hitung waktu sisa hingga baterai habis
        
        Args:
            consumption_rate (float): Persentase baterai yang habis per jam
            
        Returns:
            dict: Informasi waktu sisa dalam jam dan menit
        """
        if consumption_rate <= 0:
            return {
                "hours": float('inf'),
                "minutes": float('inf'),
                "status": "Tidak ada konsumsi"
            }
        
        total_minutes = (self.current_percentage / consumption_rate) * 60
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        
        return {
            "hours": hours,
            "minutes": minutes,
            "total_minutes": total_minutes,
            "status": "OK"
        }
    
    def predict_battery_level(self, hours_passed, consumption_rate):
        """
        Prediksi level baterai setelah durasi tertentu
        
        Args:
            hours_passed (float): Jam yang telah berlalu
            consumption_rate (float): Persentase baterai yang habis per jam
            
        Returns:
            dict: Level baterai yang diprediksi
        """
        battery_lost = hours_passed * consumption_rate
        remaining_percentage = self.current_percentage - battery_lost
        
        if remaining_percentage < 0:
            remaining_percentage = 0
        
        return {
            "hours_passed": hours_passed,
            "battery_lost": battery_lost,
            "remaining_percentage": remaining_percentage,
            "is_empty": remaining_percentage == 0
        }
    
    def get_average_consumption(self):
        """
        Hitung rata-rata konsumsi dari history
        
        Returns:
            float: Rata-rata konsumsi per jam
        """
        if not self.consumption_history:
            return 0
        return sum(self.consumption_history) / len(self.consumption_history)
    
    def estimate_empty_probability(self, duration_hours, consumption_rate):
        """
        Estimasi kemungkinan baterai akan habis dalam durasi tertentu
        
        Args:
            duration_hours (float): Durasi waktu yang ingin diperiksa (jam)
            consumption_rate (float): Persentase baterai yang habis per jam
            
        Returns:
            dict: Informasi probabilitas baterai habis
        """
        battery_needed = duration_hours * consumption_rate
        time_to_empty = (self.current_percentage / consumption_rate) if consumption_rate > 0 else float('inf')
        
        # Probabilitas baterai habis (0-100%)
        if time_to_empty <= 0:
            probability = 100
        else:
            probability = min(100, (battery_needed / self.current_percentage) * 100)
        
        return {
            "duration_hours": duration_hours,
            "battery_needed": battery_needed,
            "time_to_empty_hours": time_to_empty,
            "probability_empty": probability,
            "will_empty": battery_needed >= self.current_percentage
        }


# ============ CONTOH PENGGUNAAN ============

if __name__ == "__main__":
    print("=" * 50)
    print("BATTERY CALCULATOR - Simulasi Baterai")
    print("=" * 50)
    
    # Inisialisasi dengan baterai 100%
    battery = BatteryCalculator(current_percentage=100)
    
    # Contoh consumption rate: 5% per jam
    consumption_rate = 5  # % per jam
    
    print(f"\n📱 Kondisi Awal: {battery.current_percentage}%")
    print(f"⚡ Consumption Rate: {consumption_rate}% per jam")
    
    # 1. Hitung waktu sisa hingga habis
    print("\n" + "-" * 50)
    print("1. WAKTU SISA HINGGA BATERAI HABIS")
    print("-" * 50)
    time_remaining = battery.calculate_time_remaining(consumption_rate)
    print(f"   Waktu Sisa: {time_remaining['hours']} jam {time_remaining['minutes']} menit")
    print(f"   Total: {time_remaining['total_minutes']:.2f} menit")
    
    # 2. Prediksi level baterai setelah 5 jam
    print("\n" + "-" * 50)
    print("2. PREDIKSI LEVEL BATERAI")
    print("-" * 50)
    prediction = battery.predict_battery_level(hours_passed=5, consumption_rate=consumption_rate)
    print(f"   Setelah {prediction['hours_passed']} jam:")
    print(f"   Baterai Habis: {prediction['battery_lost']}%")
    print(f"   Level Sisa: {prediction['remaining_percentage']}%")
    
    # 3. Estimasi kemungkinan baterai habis dalam 10 jam
    print("\n" + "-" * 50)
    print("3. ESTIMASI KEMUNGKINAN BATERAI HABIS")
    print("-" * 50)
    estimate = battery.estimate_empty_probability(duration_hours=10, consumption_rate=consumption_rate)
    print(f"   Durasi: {estimate['duration_hours']} jam")
    print(f"   Baterai yang Dibutuhkan: {estimate['battery_needed']}%")
    print(f"   Waktu hingga Habis: {estimate['time_to_empty_hours']} jam")
    print(f"   Kemungkinan Habis: {estimate['probability_empty']:.2f}%")
    print(f"   Status: {'⚠️ AKAN HABIS' if estimate['will_empty'] else '✅ AMAN'}")
    
    # 4. Tambah consumption history dan hitung rata-rata
    print("\n" + "-" * 50)
    print("4. RATA-RATA KONSUMSI")
    print("-" * 50)
    battery.add_consumption_rate(5)
    battery.add_consumption_rate(4.5)
    battery.add_consumption_rate(5.5)
    avg_consumption = battery.get_average_consumption()
    print(f"   Rata-rata Konsumsi: {avg_consumption:.2f}% per jam")
    
    # 5. Simulasi berbagai skenario
    print("\n" + "-" * 50)
    print("5. SIMULASI BERBAGAI SKENARIO")
    print("-" * 50)
    
    scenarios = [
        ("Light Usage (2% per jam)", 2),
        ("Normal Usage (5% per jam)", 5),
        ("Heavy Usage (10% per jam)", 10),
        ("Very Heavy (15% per jam)", 15)
    ]
    
    for scenario_name, rate in scenarios:
        result = battery.calculate_time_remaining(rate)
        print(f"\n   {scenario_name}")
        print(f"   → Waktu: {result['hours']}h {result['minutes']}m")
