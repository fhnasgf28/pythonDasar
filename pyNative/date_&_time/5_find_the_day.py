from datetime import datetime

given_date = datetime(2020, 7, 26)

# to get weekday as integer
print(given_date.today().weekday())
# TO GET THE ENGLISH NAME OF THE WEEKDAY
print(given_date.strftime('%A'))