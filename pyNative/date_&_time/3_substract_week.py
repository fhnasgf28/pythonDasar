from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)

day_to_substract = 7
new_date = given_date - timedelta(days=day_to_substract)

print("substract week", new_date)