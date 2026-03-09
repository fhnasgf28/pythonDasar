def calculate_reading_time(num_pages, reading_speed):
    reading_time = num_pages / reading_speed
    return reading_time


def calculate_reading_time_per_day(num_pages, reading_speed, reading_time):
    reading_time = num_pages / reading_speed
    reading_days = reading_time / reading_speed
    return reading_days


num_pages = int(input("Enter Number of pages:"))
reading_speed = float(input("ENter reading speed (pages per hour):"))
reading_time_per_day = float(input("Enter reading time per day (hours): "))

reading_time = calculate_reading_time(num_pages, reading_speed, reading_time_per_day)
print("Waktu membaca buku adalah {:.2f} jam.".format(reading_time))
