import datetime

class ReminderSholat:
    def __init__(self):
        self.jadwal_sholat = {
            'subuh': '04:00',
            'dzuhur': '12:00',
            'ashar': '15:00',
            'maghrib': '18:00',
            'isya': '20:00'
        }
        self.jadwal_sekarang = self.get_jadwal_sekarang()
    
    def get_jadwal_sekarang(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M")
    
    def get_sisa_waktu(self, target_time):
        now = datetime.datetime.now()
        target = datetime.datetime.strptime(target_time, "%H:%M")
        print(f"Current time: {now.strftime('%H:%M')}, Target time: {target_time}")
        return (target - now).total_seconds() / 60
    
    def notifikasi(self):
        now = datetime.datetime.now()
        menit_terdekat = 1000
        nama_sholat = ''
        for sholat, waktu in self.jadwal_sholat.items():
            sisa_waktu = self.get_sisa_waktu(waktu)
            if sisa_waktu < menit_terdekat and sisa_waktu > 0:
                menit_terdekat = sisa_waktu
                nama_sholat = sholat
        sholat_terdekat = min(self.jadwal_sholat, key=lambda x: abs(datetime.datetime.strptime(self.jadwal_sholat[x], "%H:%M") - now))
        print(f'{int(menit_terdekat)} menit lagi menuju sholat {sholat_terdekat}')
if __name__ == "__main__":
    reminder = ReminderSholat()
    while True:
        reminder.notifikasi()
        import time
        time.sleep(60)  # Tunggu 1 menit sebelum notifikasi berikutnya

