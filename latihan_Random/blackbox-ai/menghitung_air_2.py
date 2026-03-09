num_houses = int(input("Enter number of houses: "))
daily_water_usage_per_house = float(input("Enter daily water usage per house m3"))

total_water_usage = num_houses * daily_water_usage_per_house
print("Total water usage is {:.2f} m3".format(total_water_usage))

cost_per_cubic_meter = 3000
total_water_cost = total_water_usage * cost_per_cubic_meter
print("Total water cost is IDR {:.2f}.".format(total_water_cost))