def calculate_water_usage(num_house, daily_water_per_house):
    total_water_usage = num_house * daily_water_per_house
    return total_water_usage


def calculate_water_cost(total_water_usage, cost_per_cubic_meter):
    total_water_cost = total_water_usage * cost_per_cubic_meter
    return total_water_cost

# get user input for number of houses and daily water usage per house
num_houses = int(input("Enter number of houses: "))
daily_water_usage_per_house = float(input("enter daily water usage per house (m^3): "))

# calculate and display the total water usage
total_water_usage = calculate_water_usage(num_houses, daily_water_usage_per_house)
print("Total water usage is {:.2f} m^3.".format(total_water_usage))

# calculate and display the total water cost
cost_per_cubic_meter = 3000
total_water_cost = calculate_water_cost(total_water_usage, cost_per_cubic_meter)
print("Total water cost is IDR {:.2f}.".format(total_water_cost))