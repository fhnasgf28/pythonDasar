# Sample bus schedule data in a file called "bus_schedule.txt":
# Bus ID,Route,Departure Time,Arrival Time
# 101,Airport Express,06:00,07:00
# 102,City Loop,07:30,08:30
# 103,Suburban Route,09:00,10:00
# 104,Airport Express,12:00,13:00
# 105,City Loop,14:30,15:30

# Python program to manipulate the bus schedule data
def read_bus_schedule(filename):
    bus_schedule = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header row
        for line in file:
            bus_id, route, departure_time, arrival_time = line.strip().split(',')
            bus_schedule.append({
                'bus_id': int(bus_id),
                'route': route,
                'departure_time': departure_time,
                'arrival_time': arrival_time
            })
    return bus_schedule


def find_buses_by_route(bus_schedule, route):
    return [bus for bus in bus_schedule if bus['route'] == route]


def find_buses_by_departure_time(bus_schedule, departure_time):
    return [bus for bus in bus_schedule if bus['departure_time'] == departure_time]


def print_bus_schedule(bus_schedule):
    print("Bus ID\tRoute\tDeparture Time\tArrival Time")
    for bus in bus_schedule:
        print(f"{bus['bus_id']}\t{bus['route']}\t{bus['departure_time']}\t{bus['arrival_time']}")


# Read the bus schedule data from the file
bus_schedule = read_bus_schedule(r'/mnt/7C7452557452126E/pythonDasar/latihan_Random/txt/bus_schedule.txt')

# Print the entire bus schedule
print("Entire Bus Schedule:")
print_bus_schedule(bus_schedule)

# Find buses by route
route = 'Airport Express'
print(f"\nBuses on {route} route:")
buses_on_route = find_buses_by_route(bus_schedule, route)
print_bus_schedule(buses_on_route)

# Find buses by departure time
departure_time = '12:00'
print(f"\nBuses departing at {departure_time}:")
buses_at_departure_time = find_buses_by_departure_time(bus_schedule, departure_time)
print_bus_schedule(buses_at_departure_time)
