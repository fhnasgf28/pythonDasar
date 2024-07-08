from datetime import datetime, date
import time

now = datetime.now()
print('Current DateTime:', now)
print('Type:', type(now))

current_date = now.date()
print('Date', current_date)
print(type(current_date))

current_time = now.time()
print('Time', current_time)
print(type(current_time))

print("Year", now.year)
print('Month', now.month)
print('Day =', now.day)

# get current  date using the date class
today = date.today()
print('current Date', today)

# get current time in python
t = time.time
print('time',t)
