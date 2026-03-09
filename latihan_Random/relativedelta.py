from datetime import datetime
from dateutil.relativedelta import relativedelta

# Tanggal lahir
birth_date_str = '2000-08-28'
birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')

# tanggal hari ini
today = datetime.today()

# menghitung selisih usia
age = relativedelta(today, birth_date).years

print(f"Usia: {age} tahun")