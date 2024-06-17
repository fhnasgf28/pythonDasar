from datetime import datetime, timedelta


given_date = datetime(2020, 3, 22, 10, 0,0)
print("given date")
print(given_date)

days_to_add = 7
res_date = given_date + timedelta(days_to_add, hours=12)
print("new Date")
print(res_date)